import customtkinter as ctk

class TubeDLApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configuration de la fenêtre
        self.title("TubeDL - Téléchargement")
        self.geometry("1200x700")
        
        # Couleurs
        self.COLOR_NIGHT_BLUE = "#1a1f2e"  # Bleu nuit très foncé
        self.COLOR_DARK_GRAY = "#2d3035"   # Gris foncé pour sidebar
        self.COLOR_BLUE = "#0066cc"        # Bleu principal
        self.COLOR_WHITE = "#ffffff"       # Blanc
        self.COLOR_LIGHT_GRAY = "#d1d5db"  # Gris clair
        self.COLOR_MEDIUM_GRAY = "#4a4a4a" # Gris moyen
        
        # Configuration du thème
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.setup_ui()
    
    def setup_ui(self):
        # Frame principale
        self.main_frame = ctk.CTkFrame(self, fg_color=self.COLOR_WHITE)
        self.main_frame.pack(fill="both", expand=True)
        
        # Créer la sidebar
        self.create_sidebar()
        
        # Créer la zone de contenu principal
        self.create_main_content()
    
    def create_sidebar(self):
        # Sidebar en bleu nuit
        self.sidebar = ctk.CTkFrame(
            self.main_frame,
            width=200,
            fg_color=self.COLOR_DARK_GRAY,
            corner_radius=0
        )
        self.sidebar.pack(side="left", fill="both", padx=0, pady=0)
        self.sidebar.pack_propagate(False)
        
        # Logo/Titre
        self.logo_frame = ctk.CTkFrame(self.sidebar, fg_color=self.COLOR_DARK_GRAY)
        self.logo_frame.pack(fill="x", pady=30, padx=20)
        
        self.logo_label = ctk.CTkLabel(
            self.logo_frame,
            text="⬇ TubeDL",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=self.COLOR_WHITE
        )
        self.logo_label.pack()
        
        # Menu items
        self.menu_frame = ctk.CTkFrame(self.sidebar, fg_color=self.COLOR_DARK_GRAY)
        self.menu_frame.pack(fill="x", padx=10, pady=20)
        
        menu_items = [
            ("Home", self.home_clicked),
            ("Downloads", self.downloads_clicked),
            ("About", self.about_clicked)
        ]
        
        for text, command in menu_items:
            btn = ctk.CTkButton(
                self.menu_frame,
                text=text,
                font=ctk.CTkFont(size=14),
                fg_color="transparent",
                hover_color="#3d4045",
                text_color=self.COLOR_WHITE,
                anchor="center",
                corner_radius=8,
                command=command,
                height=45
            )
            btn.pack(fill="x", pady=5)
    
    def create_main_content(self):
        # Zone de contenu principal
        self.content_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color=self.COLOR_WHITE,
            corner_radius=0
        )
        self.content_frame.pack(side="left", fill="both", expand=True, padx=30, pady=30)
        
        # Frame pour les onglets
        self.tabs_frame = ctk.CTkFrame(self.content_frame, fg_color=self.COLOR_WHITE)
        self.tabs_frame.pack(fill="x", pady=(0, 20))
        
        # Créer les boutons d'onglets
        self.video_tab = ctk.CTkButton(
            self.tabs_frame,
            text="Video",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.COLOR_DARK_GRAY,
            hover_color=self.COLOR_MEDIUM_GRAY,
            text_color=self.COLOR_WHITE,
            corner_radius=8,
            command=self.video_tab_clicked,
            height=40
        )
        self.video_tab.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.playlist_tab = ctk.CTkButton(
            self.tabs_frame,
            text="Playlist",
            font=ctk.CTkFont(size=14),
            fg_color=self.COLOR_LIGHT_GRAY,
            hover_color="#c1c5cb",
            text_color=self.COLOR_DARK_GRAY,
            corner_radius=8,
            command=self.playlist_tab_clicked,
            height=40
        )
        self.playlist_tab.pack(side="left", fill="x", expand=True, padx=(5, 0))
        
        # Zone de contenu des onglets
        self.tab_content_frame = ctk.CTkFrame(
            self.content_frame,
            fg_color=self.COLOR_LIGHT_GRAY,
            corner_radius=10
        )
        self.tab_content_frame.pack(fill="both", expand=True)
        
        # Contenu de l'onglet Video (par défaut)
        self.create_video_tab_content()
    
    def create_video_tab_content(self):
        # Effacer le contenu existant
        for widget in self.tab_content_frame.winfo_children():
            widget.destroy()
        
        # Frame centrale pour le contenu
        self.center_frame = ctk.CTkFrame(self.tab_content_frame, fg_color=self.COLOR_LIGHT_GRAY)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Label de contenu
        self.content_label = ctk.CTkLabel(
            self.center_frame,
            text="Video Download Content",
            font=ctk.CTkFont(size=16),
            text_color="#6b7280"
        )
        self.content_label.pack(pady=20)
        
        # Zone de saisie URL
        self.url_frame = ctk.CTkFrame(self.center_frame, fg_color=self.COLOR_WHITE)
        self.url_frame.pack(fill="x", padx=40, pady=20)
        
        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            placeholder_text="Collez l'URL YouTube ici...",
            font=ctk.CTkFont(size=14),
            height=45,
            corner_radius=8,
            border_width=2,
            border_color=self.COLOR_LIGHT_GRAY,
            fg_color=self.COLOR_WHITE
        )
        self.url_entry.pack(fill="x", padx=15, pady=15)
        
        # Options de qualité
        self.quality_frame = ctk.CTkFrame(self.center_frame, fg_color=self.COLOR_WHITE)
        self.quality_frame.pack(fill="x", padx=40, pady=20)
        
        self.quality_label = ctk.CTkLabel(
            self.quality_frame,
            text="Qualité vidéo",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.COLOR_DARK_GRAY
        )
        self.quality_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        self.quality_var = ctk.StringVar(value="1080p")
        
        qualities = ["Max", "1080p", "720p", "480p", "240p"]
        qualities_frame = ctk.CTkFrame(self.quality_frame, fg_color=self.COLOR_WHITE)
        qualities_frame.pack(fill="x", padx=15, pady=10)
        
        for quality in qualities:
            radio = ctk.CTkRadioButton(
                qualities_frame,
                text=quality,
                variable=self.quality_var,
                value=quality,
                font=ctk.CTkFont(size=13),
                fg_color=self.COLOR_BLUE
            )
            radio.pack(anchor="w", pady=5, padx=10)
        
        # Bouton télécharger
        self.download_btn = ctk.CTkButton(
            self.center_frame,
            text="⬇ TÉLÉCHARGER",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.COLOR_BLUE,
            hover_color="#0052a3",
            height=50,
            corner_radius=10,
            command=self.download_video
        )
        self.download_btn.pack(fill="x", padx=40, pady=30)
    
    def create_playlist_tab_content(self):
        # Effacer le contenu existant
        for widget in self.tab_content_frame.winfo_children():
            widget.destroy()
        
        # Frame centrale pour le contenu
        self.center_frame = ctk.CTkFrame(self.tab_content_frame, fg_color=self.COLOR_LIGHT_GRAY)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Label de contenu
        self.content_label = ctk.CTkLabel(
            self.center_frame,
            text="Playlist Download Content",
            font=ctk.CTkFont(size=16),
            text_color="#6b7280"
        )
        self.content_label.pack(pady=20)
        
        # Zone de saisie URL
        self.url_frame = ctk.CTkFrame(self.center_frame, fg_color=self.COLOR_WHITE)
        self.url_frame.pack(fill="x", padx=40, pady=20)
        
        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            placeholder_text="Collez l'URL de la playlist...",
            font=ctk.CTkFont(size=14),
            height=45,
            corner_radius=8,
            border_width=2,
            border_color=self.COLOR_LIGHT_GRAY,
            fg_color=self.COLOR_WHITE
        )
        self.url_entry.pack(fill="x", padx=15, pady=15)
        
        # Bouton télécharger
        self.download_btn = ctk.CTkButton(
            self.center_frame,
            text="⬇ TÉLÉCHARGER LA PLAYLIST",
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=self.COLOR_BLUE,
            hover_color="#0052a3",
            height=50,
            corner_radius=10,
            command=self.download_playlist
        )
        self.download_btn.pack(fill="x", padx=40, pady=30)
    
    def video_tab_clicked(self):
        # Mettre à jour l'apparence des onglets
        self.video_tab.configure(
            fg_color=self.COLOR_DARK_GRAY,
            text_color=self.COLOR_WHITE,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.playlist_tab.configure(
            fg_color=self.COLOR_LIGHT_GRAY,
            text_color=self.COLOR_DARK_GRAY,
            font=ctk.CTkFont(size=14)
        )
        
        # Afficher le contenu de l'onglet Video
        self.create_video_tab_content()
    
    def playlist_tab_clicked(self):
        # Mettre à jour l'apparence des onglets
        self.playlist_tab.configure(
            fg_color=self.COLOR_DARK_GRAY,
            text_color=self.COLOR_WHITE,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.video_tab.configure(
            fg_color=self.COLOR_LIGHT_GRAY,
            text_color=self.COLOR_DARK_GRAY,
            font=ctk.CTkFont(size=14)
        )
        
        # Afficher le contenu de l'onglet Playlist
        self.create_playlist_tab_content()
    
    def home_clicked(self):
        print("Navigation vers Home")
    
    def downloads_clicked(self):
        print("Navigation vers Downloads")
    
    def about_clicked(self):
        print("Navigation vers About")
    
    def download_video(self):
        url = self.url_entry.get()
        quality = self.quality_var.get()
        print(f"Téléchargement vidéo: {url} - Qualité: {quality}")
    
    def download_playlist(self):
        url = self.url_entry.get()
        print(f"Téléchargement playlist: {url}")

if __name__ == "__main__":
    app = TubeDLApp()
    app.mainloop()