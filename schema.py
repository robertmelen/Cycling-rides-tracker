import sqlite3


conn = sqlite3.connect('cycling.db')
c = conn.cursor()


#REMEMBER- DATE is formatted year, month, data

c.execute('''CREATE TABLE IF NOT EXISTS cyclist
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, dob DATE, skill_level TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS ride
             (id INTEGER PRIMARY KEY, name TEXT, date DATE, length REAL, location TEXT, start TEXT, finish TEXT,
             start_time REAL, cyclist_id INTEGER,
             FOREIGN KEY (cyclist_id) REFERENCES cyclist(id))''')

c.execute('''CREATE TABLE IF NOT EXISTS ride_cyclist
             (ride_id INTEGER, cyclist_id INTEGER,
             FOREIGN KEY (ride_id) REFERENCES ride(id),
             FOREIGN KEY (cyclist_id) REFERENCES cyclist(id),
             PRIMARY KEY (ride_id, cyclist_id))''')
