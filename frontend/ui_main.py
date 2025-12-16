import tkinter as tk
from frontend.ui_addClient import AddClientFrame
from frontend.ui_cleanTable import CleanFrame
from frontend.ui_home import HomeFrame
from frontend.ui_login import LoginFrame
from frontend.ui_addClean import AddCleanFrame
from frontend.ui_clientTable import ClientFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FgaSistem")
        self.geometry("800x600")

        self.frames = {}

        self.frame_classes = {
            "LoginFrame": LoginFrame,
            "HomeFrame": HomeFrame,
            "CleanFrame": CleanFrame,
            "AddCleanFrame": AddCleanFrame,
            "ClientFrame": ClientFrame,
            "AddClientFrame": AddClientFrame,
        }

        for name, F in self.frame_classes.items():
            frame = F(self)
            self.frames[name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("LoginFrame")

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        if hasattr(frame, "refresh"):
            try:
                frame.refresh()
            except Exception as e:
                print(f"Erro ao atualizar frame {frame_name}: {e}")
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()