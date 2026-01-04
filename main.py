import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("900x600")
        self.root.configure(bg="#1e1e2f")

        self.image_paths = []
        self.index = 0
        self.zoom = 1.0

        # Image Display
        self.image_label = tk.Label(root, bg="#1e1e2f")
        self.image_label.pack(expand=True)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e1e2f")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Browse Folder",
                  bg="#03a9f4", fg="white", font=("Arial", 12, "bold"),
                  width=14, height=2, command=self.browse_folder).grid(row=0, column=0, padx=5)

        tk.Button(btn_frame, text="Previous",
                  bg="#ff5722", fg="white", font=("Arial", 12, "bold"),
                  width=12, height=2, command=self.prev_image).grid(row=0, column=1, padx=5)

        tk.Button(btn_frame, text="Next",
                  bg="#4caf50", fg="white", font=("Arial", 12, "bold"),
                  width=12, height=2, command=self.next_image).grid(row=0, column=2, padx=5)

        tk.Button(btn_frame, text="Zoom +",
                  bg="#9c27b0", fg="white", font=("Arial", 12, "bold"),
                  width=10, height=2, command=self.zoom_in).grid(row=0, column=3, padx=5)

        tk.Button(btn_frame, text="Zoom -",
                  bg="#795548", fg="white", font=("Arial", 12, "bold"),
                  width=10, height=2, command=self.zoom_out).grid(row=0, column=4, padx=5)

        tk.Button(btn_frame, text="Exit",
                  bg="#607d8b", fg="white", font=("Arial", 12, "bold"),
                  width=10, height=2, command=root.quit).grid(row=0, column=5, padx=5)

    # -------- FUNCTIONS --------

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if not folder:
            return

        self.image_paths = [
            os.path.join(folder, f) for f in os.listdir(folder)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))
        ]

        if not self.image_paths:
            messagebox.showerror("Error", "No image files found!")
            return

        self.index = 0
        self.zoom = 1.0
        self.show_image()

    def show_image(self):
        img = Image.open(self.image_paths[self.index])
        w, h = img.size
        img = img.resize((int(w*self.zoom), int(h*self.zoom)),
                          Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.photo)

    def next_image(self):
        if self.image_paths:
            self.index = (self.index + 1) % len(self.image_paths)
            self.show_image()

    def prev_image(self):
        if self.image_paths:
            self.index = (self.index - 1) % len(self.image_paths)
            self.show_image()


    def zoom_in(self):
        self.zoom += 0.1
        self.show_image()

    def zoom_out(self):
        if self.zoom > 0.2:
            self.zoom -= 0.1
            self.show_image()

# -------- RUN --------
root = tk.Tk()
app = ImageViewer(root)
root.mainloop()
