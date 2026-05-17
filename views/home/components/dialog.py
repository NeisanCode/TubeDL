import customtkinter as ctk

class ConfirmDialog(ctk.CTkToplevel):
    def __init__(self, parent, message):
        super().__init__(parent)
        self.result = None
        
        self.title("Confirmation")
        self.geometry("300x150")
        self.resizable(False, False)
        
        ctk.CTkLabel(self, text=message).pack(pady=20)
        
        frame = ctk.CTkFrame(self)
        frame.pack(pady=10)
        
        ctk.CTkButton(frame, text="Oui", command=self._oui).pack(side="left", padx=10)
        ctk.CTkButton(frame, text="Non", command=self._non).pack(side="left", padx=10)
        
        self.grab_set()  # bloque la fenêtre parent
        self.wait_window()  # attend la fermeture
    
    def _oui(self):
        self.result = True
        self.destroy()
    
    def _non(self):
        self.result = False
        self.destroy()