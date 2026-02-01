from utils.db_api.sqlite import Database

def populate_wisdom():
    db = Database()
    db.create_table_wisdom()
    wisdom_list = [
        ("Albatta, qiyinchilik bilan birga yengillik bordir.", "Sharh surasi, 6-oyat"),
        ("Sizlarning yaxshilaringiz - boshqalarga foydasi tegadiganlaringizdir.", "Hadis"),
        ("Alloh sizlarning suratingizga va molingizga emas, qalbingizga va amalingizga qaraydi.", "Hadis"),
        ("Yaxshilik qiling, zero Alloh yaxshilik qiluvchilarni sevadi.", "Baqara surasi, 195-oyat"),
        ("Sabr jannat kalitidir.", "Hikmat"),
        ("Ikki ne'mat borki, ko'p odamlar uning qadriga yetmaydilar: sog'lik va bo'sh vaqt.", "Hadis")
    ]
    
    for content, source in wisdom_list:
        db.add_wisdom(content, source)
    print("Wisdom table populated!")

if __name__ == "__main__":
    populate_wisdom()
