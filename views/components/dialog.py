import customtkinter as ctk
from views.themes.color import *

class ConfirmDialog(ctk.CTkToplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.result = None
        
        self.title("Confirmation")
        self.geometry("340x160")
        self.resizable(False, False)
        self.configure(fg_color=BG_WHITE)
        
        ctk.CTkLabel(
            self, 
            text=message,
            font=ctk.CTkFont(family="Segoe UI", size=14),
            text_color=TEXT_DARK,
            wraplength=300
        ).pack(pady=(24, 16))
        
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=10)
        
        # Annuler (Style discret)
        ctk.CTkButton(
            frame, 
            text="Annuler", 
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color=BG_INPUT, 
            text_color=TEXT_DARK,
            hover_color=BORDER,
            width=100,
            height=34,
            corner_radius=8,
            command=self._non
        ).pack(side="left", padx=8)

        # Confirmer (Style Action)
        ctk.CTkButton(
            frame, 
            text="Continuer", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            fg_color=PRIMARY_ACCENT, 
            text_color=TEXT_LIGHT,
            hover_color=HOVER_ACCENT,
            width=100,
            height=34,
            corner_radius=8,
            command=self._oui
        ).pack(side="left", padx=8)
        
        self.grab_set()
        self.wait_window()
    
    def _oui(self):
        self.result = True
        self.destroy()
    
    def _non(self):
        self.result = False
        self.destroy()