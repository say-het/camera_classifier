import tkinter as tk
from app import App

def main():
    window = tk.Tk()
    app = App(window, "Camera Classifier")
    window.mainloop()

if __name__ == "__main__":
    main()
