import sqlite3

conn = sqlite3.connect("images.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT
)
""")

image_paths = [
    "images/img1.jpg",
    "images/img2.png",
    "images/img3.jpg"
]

cur.execute("DELETE FROM images")  # old data clear (important)

for path in image_paths:
    cur.execute("INSERT INTO images (path) VALUES (?)", (path,))

conn.commit()
conn.close()

print("Cartoon images added to database")
