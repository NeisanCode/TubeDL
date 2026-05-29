from views import App
from core import setup_check

setup_startup = setup_check()
if setup_startup:
    app = App()
    app.mainloop()
