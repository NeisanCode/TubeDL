import customtkinter as ctk
from view.screen.widget.sidebar import Sidebar
from view.screen.home_page import HomePage

# Configuration du thème
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("YouTube Downloader Pro")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        
        # Couleurs personnalisées - LIGHT MODE
        self.colors = {
            "bg_primary": "#f5f7fa",
            "bg_secondary": "#ffffff",
            "bg_card": "#e8ecf1",
            "accent_primary": "#0066cc",
            "accent_secondary": "#00a8e8",
            "accent_hover": "#0052a3",
            "text_primary": "#1a1a2e",
            "text_secondary": "#64748b",
            "sidebar": "#1e293b",
            "sidebar_text": "#e2e8f0",
            "success": "#10b981",
            "border": "#cbd5e1"
        }
        
        self.configure(fg_color=self.colors["bg_primary"])
        
        # Configuration du grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.create_widgets()
    
    def create_widgets(self):
        # ===== SIDEBAR =====
        self.sidebar = Sidebar(
            self,
            colors=self.colors,
            on_nav_click=self.handle_nav_click
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        # ===== MAIN LAYOUT =====
        self.main_layout = HomePage(self, colors=self.colors)
        self.main_layout.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
    
    def handle_nav_click(self, page):
        """Gère les clics de navigation"""
        print(f"Navigation vers: {page}")
        # Ici tu peux ajouter la logique pour changer de page
        # Ex: self.main_layout.switch_page(page)

