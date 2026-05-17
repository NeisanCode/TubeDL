from CTkMessagebox import CTkMessagebox
from functools import wraps


def handle_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            CTkMessagebox(
                title="Error",
                message=f"Erreur inattendu\n{str(e)}",
                icon="cancel",
            )
            return
    return wrapper
