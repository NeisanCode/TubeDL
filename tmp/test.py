import customtkinter as ctk
from tkhtmlview import HTMLLabel

ctk.set_appearance_mode("light")

class HTMLApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("HTML Viewer")
        self.geometry("800x600")
        
        # HTML content
        html_content = """
        <html>
            <body style="background-color: #f5f7fa; font-family: Arial;">
                <h1 style="color: #0066cc;">Bienvenue</h1>
                <p>Ceci est du <b>HTML</b> dans CustomTkinter</p>
                <div style="padding: 20px; background: #e8ecf1; border-radius: 10px;">
                    <p>Contenu personnalisé</p>
                </div>
            </body>
        </html>
        """
        
        # HTML Label
        self.html_label = HTMLLabel(self, html=html_content)
        self.html_label.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Important pour le rendu
        self.html_label.fit_height()

if __name__ == "__main__":
    app = HTMLApp()
    app.mainloop()