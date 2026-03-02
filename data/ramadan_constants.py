# Ramadan 2026 Data (Official Uzbekistan timings from Gazeta.uz)

# Toshkent timings (Kun 1 to Kun 30)
# Start date: Feb 19, 2026
RAMADAN_2026_TASHKENT = [
    {"day": 1, "date": "19-fev", "sahar": "05:54", "iftor": "18:05"},
    {"day": 2, "date": "20-fev", "sahar": "05:53", "iftor": "18:07"},
    {"day": 3, "date": "21-fev", "sahar": "05:51", "iftor": "18:08"},
    {"day": 4, "date": "22-fev", "sahar": "05:50", "iftor": "18:09"},
    {"day": 5, "date": "23-fev", "sahar": "05:49", "iftor": "18:10"},
    {"day": 6, "date": "24-fev", "sahar": "05:47", "iftor": "18:11"},
    {"day": 7, "date": "25-fev", "sahar": "05:46", "iftor": "18:12"},
    {"day": 8, "date": "26-fev", "sahar": "05:44", "iftor": "18:14"},
    {"day": 9, "date": "27-fev", "sahar": "05:43", "iftor": "18:15"},
    {"day": 10, "date": "28-fev", "sahar": "05:41", "iftor": "18:16"},
    {"day": 11, "date": "1-mar", "sahar": "05:40", "iftor": "18:17"},
    {"day": 12, "date": "2-mar", "sahar": "05:38", "iftor": "18:19"},
    {"day": 13, "date": "3-mar", "sahar": "05:37", "iftor": "18:20"},
    {"day": 14, "date": "4-mar", "sahar": "05:35", "iftor": "18:21"},
    {"day": 15, "date": "5-mar", "sahar": "05:34", "iftor": "18:22"},
    {"day": 16, "date": "6-mar", "sahar": "05:32", "iftor": "18:23"},
    {"day": 17, "date": "7-mar", "sahar": "05:31", "iftor": "18:24"},
    {"day": 18, "date": "8-mar", "sahar": "05:29", "iftor": "18:25"},
    {"day": 19, "date": "9-mar", "sahar": "05:27", "iftor": "18:27"},
    {"day": 20, "date": "10-mar", "sahar": "05:26", "iftor": "18:28"},
    {"day": 21, "date": "11-mar", "sahar": "05:24", "iftor": "18:29"},
    {"day": 22, "date": "12-mar", "sahar": "05:22", "iftor": "18:30"},
    {"day": 23, "date": "13-mar", "sahar": "05:21", "iftor": "18:31"},
    {"day": 24, "date": "14-mar", "sahar": "05:19", "iftor": "18:32"},
    {"day": 25, "date": "15-mar", "sahar": "05:17", "iftor": "18:33"},
    {"day": 26, "date": "16-mar", "sahar": "05:15", "iftor": "18:34"},
    {"day": 27, "date": "17-mar", "sahar": "05:14", "iftor": "18:35"},
    {"day": 28, "date": "18-mar", "sahar": "05:12", "iftor": "18:37"},
    {"day": 29, "date": "19-mar", "sahar": "05:10", "iftor": "18:38"},
    {"day": 30, "date": "20-mar", "sahar": "05:08", "iftor": "18:39"},
]

# Regional offsets (in minutes) relative to Tashkent
# Some regions have separate sahar and iftor offsets
REGIONAL_OFFSETS = {
    "Andijon": {"sahar": -12, "iftor": -13},
    "Namangan": {"sahar": -9, "iftor": -10},
    "Farg'ona": {"sahar": -9, "iftor": -10},
    "Samarqand": {"sahar": 10, "iftor": 10},
    "Jizzax": {"sahar": 6, "iftor": 6},
    "Buxoro": {"sahar": 20, "iftor": 20},
    "Navoiy": {"sahar": 16, "iftor": 16},
    "Qashqadaryo": {"sahar": 15, "iftor": 15},
    "Surxondaryo": {"sahar": 8, "iftor": 9},
    "Sirdaryo": {"sahar": 3, "iftor": 2},
    "Xorazm": {"sahar": 35, "iftor": 34},
    "Qoraqalpog'iston": {"sahar": 38, "iftor": 37},
    "Toshkent": {"sahar": 0, "iftor": 0}
}

# Ramadan Duas
RAMADAN_DUAS = {
    "Saharlik duosi": (
        "🌙 **Saharlik (Og'iz yopish) duosi**\n\n"
        "`Navaytu an asuma sovma shahri ramazona minal fajri ilal mag'ribi, xolisan lillaxi ta'ala. Ollohu akbar.`\n\n"
        "**Ma'nosi:** Ramazon oyining ro'zasini subhdan kun botguncha xolis Alloh uchun tutishni niyat qildim. Alloh buyukdir."
    ),
    "Iftorlik duosi": (
        "🌟 **Iftorlik (Og'iz ochish) duosi**\n\n"
        "`Allohumma laka sumtu va bika amantu va a'layka tavakkaltu va a'la rizqika aftartu, fag'firli ya g'offaru ma qoddamtu va ma axxortu.`\n\n"
        "**Ma'nosi:** Ey Alloh, Sen uchun ro'za tutdim, Senga iymon keltirdim, Senga tavakkal qildim va bergan rizqing bilan iftor qildim. Ey gunohlarni afv etuvchi Zot, mening avvalgi va keyingi gunohlarimni mag'firat qil."
    )
}
