import platform

system = platform.system()


class Config:
    if system == "Windows":
        DEBUG = True
    else:
        DEBUG = False


print(Config.DEBUG)
