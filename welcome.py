import tkinter as tk
from PIL import Image, ImageTk

class WelcomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome")
        self.root.geometry("800x600")
        self.root.configure(bg="white")

        # Title Label
        title_label = tk.Label(self.root, text="Metro Rail Management System", font=("Arial", 20, "bold"), bg="white")
        title_label.pack(pady=20)

        # Image
        img = Image.open("./Image/metro.png")
        img = img.resize((400, 350))
        self.photo = ImageTk.PhotoImage(img) 
        img_label = tk.Label(self.root, image=self.photo, bg="white")
        img_label.pack(pady=10)

        # Book Ticket Button
        book_btn = tk.Button(self.root, text="Book Ticket", font=("Arial", 14), bg="blue", fg="white", command=self.open_main)
        book_btn.pack(pady=20)

    def open_main(self):
        self.root.destroy()       # close window
        import main # open main file
        


# Run
root = tk.Tk()
app = WelcomePage(root)
root.mainloop()