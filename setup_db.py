import sqlite3
import os
import shutil

DB_FILE = "database.db"
IMAGE_FOLDER = "images"

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()

# Create table if not exists
c.execute('''
CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    path TEXT
)
''')

# Copy images from 'images' folder and insert into database
for filename in os.listdir(IMAGE_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
        path = os.path.join(IMAGE_FOLDER, filename)
        # Insert only if not already in DB
        c.execute("SELECT * FROM images WHERE path=?", (path,))
        if not c.fetchall():
            c.execute("INSERT INTO images (name, path) VALUES (?, ?)", (filename, path))

conn.commit()
conn.close()
print("Database setup completed with initial images!")
