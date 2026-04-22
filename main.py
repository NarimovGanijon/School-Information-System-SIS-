import sqlite3 as sql

with sql.connect("data.db") as con:
    cur = con.cursor()

    # создание таблицы
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_data(
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        father_name TEXT
    )
    """)

    # данные
    users = [
        (1, "G'anijon", "Norimov", "Baxdir o'g'li"),
        (2, "Bobur", "Jovliyev", "Nuriddin o'g'li"),
        (3, "Maqsadbek", "Qurbanbayev", "Ixtiyor o'g'li"),
        (4, "Madadbek", "Odilbekov", "Odilbek o'g'li"),
        (5, "Sanjarbek", "Kamilanov", "Muzaffar o'g'li"),
        (6, "Muzrobbek", "Kvandikov", "Maqsud o'g'li"),
        (7, "Temurbek", "Xabibullayev", "N/A"),
        (8, "Shoxjahon", "Egamberdiyev", "N/A"),
        (9, "Rustmov", "Mominjon", "N/A"),
        (10, "Javoxir", "Samandarov", "N/A"),
        (11, "Asadbek", "Ikromov", "Orifjon o'g'li"),
        (12, "Yoqubek", "Ruzmamtv", "N/A"),
        (13, "Sherali", "Ortiqboyev", "N/A"),
        (14, "Sarvinoz", "Xamroyeva", "Sardorbek qizi"),
        (15, "Umida", "Bozorova", "N/A"),
        (16, "Feruza", "Alaerganova", "N/A"),
        (17, "Zuxra", "Yusupova", "N/A"),
        (18, "Kumushoy", "Rustamova", "N/A"),
        (19, "Zebuniso", "Raabboyeva", "N/A"),
        (20, "Xadicha", "Rustamova", "N/A"),
        (21, "Jahonabonu", "Matyoqubova", "N/A")
    ]

    # вставка данных
    cur.executemany("""
    INSERT OR IGNORE INTO user_data (id, first_name, last_name, father_name)
    VALUES (?, ?, ?, ?)
    """, users)

    con.commit()

    # # проверка
    # cur.execute("SELECT * FROM user_data")
    # for row in cur.fetchall():
    #     print(row)

#     user_id = int(input())

# cur.execute(
#     "SELECT * FROM user_data WHERE id = ?",
#     (user_id,)
# )

# print(*cur.fetchone())  # только одна запись
    cur.execute("""CREATE TABLE IF NOT EXISTS fanlar(
                ID INTEGER PRIMARY KEY,
                Subjects_name TEXT,
                Teachers_name TEXT,
                Count INTEGER
                )""")
    subjects=[
        (1,"CS (Computer Science)","Nodirbek", 3),
        (2,"English", "Feruza",3),
        (3,"Mathematics","Temurbek",7),
        (4,"Physics","Vohidjon",3),
        (5,"History","Farzona",2),
        (6,"Geography","Hamzabek",1)
    ]
    cur.executemany("""INSERT OR IGNORE INTO fanlar(id, Subjects_name, Teachers_name, Count )
    VALUES (?,?,?,?)
    """, subjects)
    con.commit()



    cur.execute("""CREATE TABLE IF NOT EXISTS baholar(
                
                )""")