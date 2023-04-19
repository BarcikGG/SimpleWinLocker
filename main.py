from tkinter import *
import ctypes

def callback(hwnd, msg, wparam, lparam):
    if msg == 0x0010: # WM_CLOSE
        return 0
    else:
        return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

class PasswordWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Введите пароль")
        self.master.attributes("-fullscreen", True)

        self.master.protocol("WM_DELETE_WINDOW", lambda: None)

        self.label = Label(master, text="Пароль:", font=("Arial", 24))
        self.label.pack(pady=20)

        self.password_entry = Entry(master, show="*", font=("Arial", 24))
        self.password_entry.pack(pady=20)

        self.login_button = Button(master, text="Вход", font=("Arial", 24), command=self.check_password)
        self.login_button.pack(pady=20)

    def check_password(self):
        password = self.password_entry.get()

        if password == "171":
            self.master.destroy()

        else:
            messagebox.showerror("Ошибка", "Неверный пароль")

root = Tk()

password_window = PasswordWindow(root)

root.mainloop()