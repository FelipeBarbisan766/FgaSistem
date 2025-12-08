from frontend.ui_main import App
from database.models import create_tables

if __name__ == "__main__":
    create_tables()
    app = App()
    app.mainloop()