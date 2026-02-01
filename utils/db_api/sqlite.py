import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
            id int NOT NULL,
            full_name varchar(255) NOT NULL,
            region varchar(255),
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    def create_table_wisdom(self):
        sql = """
        CREATE TABLE IF NOT EXISTS wisdom (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            source VARCHAR(255)
            );
        """
        self.execute(sql, commit=True)

    def add_wisdom(self, content: str, source: str = None):
        sql = """
        INSERT INTO wisdom(content, source) VALUES(?, ?)
        """
        self.execute(sql, parameters=(content, source), commit=True)

    def get_random_wisdom(self):
        sql = """
        SELECT content, source FROM wisdom ORDER BY RANDOM() LIMIT 1
        """
        return self.execute(sql, fetchone=True)

    def create_table_tasbih(self):
        sql = """
        CREATE TABLE IF NOT EXISTS tasbih (
            user_id INTEGER PRIMARY KEY,
            count INTEGER DEFAULT 0
            );
        """
        self.execute(sql, commit=True)

    def update_tasbih(self, user_id: int, count: int):
        sql = """
        INSERT INTO tasbih(user_id, count) VALUES(?, ?)
        ON CONFLICT(user_id) DO UPDATE SET count=EXCLUDED.count
        """
        self.execute(sql, parameters=(user_id, count), commit=True)

    def get_tasbih(self, user_id: int):
        sql = """
        SELECT count FROM tasbih WHERE user_id=?
        """
        result = self.execute(sql, parameters=(user_id,), fetchone=True)
        return result[0] if result else 0

    def create_table_tracker(self):
        sql = """
        CREATE TABLE IF NOT EXISTS prayer_tracker (
            user_id INTEGER,
            date TEXT,
            fajr INTEGER DEFAULT 0,
            dhuhr INTEGER DEFAULT 0,
            asr INTEGER DEFAULT 0,
            maghrib INTEGER DEFAULT 0,
            isha INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, date)
            );
        """
        self.execute(sql, commit=True)

    def update_prayer_status(self, user_id: int, date: str, prayer: str, status: int):
        # First ensure row exists
        sql_init = f"INSERT OR IGNORE INTO prayer_tracker(user_id, date) VALUES(?, ?)"
        self.execute(sql_init, parameters=(user_id, date), commit=True)
        
        # Then update specific prayer
        sql_update = f"UPDATE prayer_tracker SET {prayer}=? WHERE user_id=? AND date=?"
        self.execute(sql_update, parameters=(status, user_id, date), commit=True)

    def get_daily_tracker(self, user_id: int, date: str):
        sql = "SELECT fajr, dhuhr, asr, maghrib, isha FROM prayer_tracker WHERE user_id=? AND date=?"
        return self.execute(sql, parameters=(user_id, date), fetchone=True)

    def add_user(self, id: int, full_name: str, region: str = None):
        sql = """
        INSERT OR IGNORE INTO users(id, full_name, region) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(id, full_name, region), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def update_user_region(self, id: int, region: str):
        sql = """
        UPDATE users SET region=? WHERE id=?
        """
        self.execute(sql, parameters=(region, id), commit=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
