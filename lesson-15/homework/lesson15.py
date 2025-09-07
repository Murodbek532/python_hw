import sqlite3

# 1. Create database and table
conn = sqlite3.connect("starfleet.db")  
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Populate table with given values
characters = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)
conn.commit()

# 3. Update Jadzia Dax → Ezri Dax
cursor.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ("Ezri Dax", "Jadzia Dax"))
conn.commit()

# 4. Display Name and Age of Bajorans
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
results = cursor.fetchall()

print("Bajorans in roster:")
for row in results:
    print(row)

conn.close()

Bajorans in roster:
('Kira Nerys', 29)
