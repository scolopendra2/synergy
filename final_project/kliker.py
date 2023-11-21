import time
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk


class ClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clicker Game")
        self.root.geometry("400x300")
        self.root.configure(bg='#66ccff')

        self.money = 0
        self.timer_start = time.time()

        self.money_label = tk.Label(root, text=f"Money: {self.money}", font=("Arial", 14), bg='#66ccff')
        self.money_label.pack(pady=10)

        image = Image.open("rubl.jpg")
        image = image.resize((100, 100))
        self.click_img = ImageTk.PhotoImage(image)

        self.click_button = tk.Button(root, image=self.click_img, command=self.click_money)
        self.click_button.pack(pady=20)

        self.timer_label = tk.Label(root, text="Time: 0 seconds", font=("Arial", 12), bg='#66ccff')
        self.timer_label.pack(side="left", padx=10)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(side="right", padx=10)

        self.update_timer()

    def click_money(self):
        self.money += 1
        self.money_label.config(text=f"Money: {self.money}")

    def update_timer(self):
        elapsed_time = int(time.time() - self.timer_start)
        self.timer_label.config(text=f"Time: {elapsed_time} seconds")
        self.root.after(1000, self.update_timer)

    def reset_game(self):
        self.money = 0
        self.money_label.config(text=f"Money: {self.money}")
        self.timer_start = time.time()


if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerApp(root)
    root.mainloop()
