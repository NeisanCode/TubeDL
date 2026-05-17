from controllers import Controller
from queue import Queue

# url = "https://youtu.be/1fx1hh3m1Fw?list=RD1fx1hh3m1Fw"
# media = Controller.analyse_url(url)
# queue = Queue()
# Controller.download(media, queue)

# while not queue.empty():
#     item = queue.get()
from tkinter import messagebox
import customtkinter as ctk

result = ctk.CTkInputDialog(
    text="Quel est votre nom ?",
    title="Nom"
).get_input()

print(result)
