import customtkinter as ctk
from tkinterweb import HtmlFrame


# ─────────────────────────────────────────────
#  Contenu HTML de la page About
# ─────────────────────────────────────────────
def build_html(colors: dict) -> str:
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }}

  body {{
    background-color: {colors["bg_primary"]};
    font-family: "Poppins", serif;
    color: {colors["text_primary"]};
    padding: 48px 64px;
  }}

  /* ── Hero ── */
  .hero {{
    text-align: center;
    padding-bottom: 40px;
    border-bottom: 1px solid {colors["border"]};
    margin-bottom: 40px;
  }}

  .app-icon {{
    font-size: 52px;
    margin-bottom: 16px;
  }}

  .app-name {{
    font-size: 36px;
    font-weight: bold;
    color: {colors["text_primary"]};
    letter-spacing: -0.5px;
  }}

  .app-name span {{
    color: {colors["accent_primary"]};
  }}

  .app-version {{
    display: inline-block;
    margin-top: 10px;
    padding: 3px 14px;
    background-color: {colors["bg_card"]};
    border: 1px solid {colors["border"]};
    border-radius: 20px;
    font-size: 12px;
    color: {colors["text_secondary"]};
    font-family: monospace;
  }}

  .app-tagline {{
    margin-top: 14px;
    font-size: 14px;
    color: {colors["text_secondary"]};
    font-style: italic;
  }}

  /* ── Section ── */
  .section {{
    margin-bottom: 36px;
  }}

  .section-title {{
    font-size: 11px;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    color: {colors["text_secondary"]};
    margin-bottom: 16px;
  }}

  /* ── Features ── */
  .features-grid {{
    border: 1px solid {colors["border"]};
    border-radius: 10px;
    overflow: hidden;
    background-color: {colors["bg_secondary"]};
  }}

  .feature-row {{
    padding: 14px 20px;
    border-bottom: 1px solid {colors["border"]};
    font-size: 13px;
    color: {colors["text_primary"]};
  }}

  .feature-row:last-child {{
    border-bottom: none;
  }}

  .feature-icon {{
    margin-right: 10px;
    font-size: 15px;
  }}

  .feature-badge {{
    float: right;
    font-size: 11px;
    font-family: monospace;
    color: {colors["accent_primary"]};
    background-color: #e8f0fc;
    padding: 2px 10px;
    border-radius: 20px;
    font-weight: bold;
  }}

  /* ── Auteur card ── */
  .author-card {{
    background-color: {colors["bg_secondary"]};
    border: 1px solid {colors["border"]};
    border-radius: 10px;
    padding: 22px 24px;
  }}

  .author-avatar {{
    font-size: 32px;
    margin-bottom: 10px;
  }}

  .author-name {{
    font-size: 16px;
    font-weight: bold;
    color: {colors["text_primary"]};
  }}

  .author-role {{
    font-size: 13px;
    color: {colors["text_secondary"]};
    margin-top: 4px;
  }}

  .author-link {{
    display: inline-block;
    margin-top: 12px;
    font-size: 12px;
    color: {colors["accent_primary"]};
    text-decoration: none;
    border-bottom: 1px solid {colors["accent_primary"]};
    padding-bottom: 1px;
  }}

  /* ── Disclaimer ── */
  .disclaimer {{
    background-color: #fff8e1;
    border: 1px solid #f0d080;
    border-radius: 10px;
    padding: 14px 20px;
    font-size: 12px;
    color: #7a6000;
    line-height: 1.6;
  }}

  .disclaimer strong {{
    color: #5a4500;
  }}

  /* ── Footer ── */
  .footer {{
    margin-top: 40px;
    text-align: center;
    font-size: 11px;
    color: {colors["text_secondary"]};
    border-top: 1px solid {colors["border"]};
    padding-top: 20px;
    line-height: 1.8;
  }}

  .footer span {{
    color: #e05555;
  }}
</style>
</head>
<body>

  <!-- Hero -->
  <div class="hero">
    <div class="app-icon">📥</div>
    <div class="app-name">Tube<span>DL</span></div>
    <div class="app-version">v1.0.0</div>
    <div class="app-tagline">Téléchargez librement, regardez sans limites.</div>
  </div>

  <!-- Fonctionnalités -->
  <div class="section">
    <div class="section-title">Ce que TubeDL sait faire</div>
    <div class="features-grid">
      <div class="feature-row">
        <span class="feature-icon">🎬</span>
        Téléchargement de vidéos YouTube
        <span class="feature-badge">jusqu'à 4K</span>
      </div>
      <div class="feature-row">
        <span class="feature-icon">📋</span>
        Téléchargement de playlists complètes
        <span class="feature-badge">batch</span>
      </div>
      <div class="feature-row">
        <span class="feature-icon">⚡</span>
        Téléchargement de Shorts
        <span class="feature-badge">vertical</span>
      </div>
      <div class="feature-row">
        <span class="feature-icon">📐</span>
        Choix de la qualité vidéo
        <span class="feature-badge">144p → 4K</span>
      </div>
    </div>
  </div>

  <!-- Auteur -->
  <div class="section">
    <div class="section-title">Auteur</div>
    <div class="author-card">
      <div class="author-avatar">👤</div>
      <div class="author-name">Neisan</div>
      <div class="author-role">Développeur · AI Engineer</div>
      <a class="author-link" href="https://github.com/neisan">github.com/neisan</a>
    </div>
  </div>

  <!-- Disclaimer -->
  <div class="section">
    <div class="disclaimer">
      <strong>⚠️ Usage personnel uniquement.</strong><br>
      TubeDL est un outil personnel et n'est pas affilié à YouTube ni à Google.
      Veuillez respecter les droits d'auteur et les conditions d'utilisation de YouTube.
    </div>
  </div>

  <!-- Footer -->
  <div class="footer">
    Fait avec <span>♥</span> par Neisan — TubeDL v1.0.0<br>
    Tous droits réservés © 2024
  </div>

</body>
</html>
"""


# ─────────────────────────────────────────────
#  COMPOSANT : AboutPage
# ─────────────────────────────────────────────
class AboutPage(ctk.CTkFrame):
    """
    Page About rendue via tkinterweb.
    S'intègre comme n'importe quel CTkFrame dans ta navigation.
    """

    def __init__(self, parent, colors: dict, **kwargs):
        super().__init__(parent, fg_color=colors["bg_primary"], **kwargs)
        self.colors = colors
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build()

    def _build(self):
        self._html_frame = HtmlFrame(
            self,
            messages_enabled=False,   # désactive les messages de debug
            vertical_scrollbar="auto",
            horizontal_scrollbar=False,
        )
        self._html_frame.grid(row=0, column=0, sticky="nsew")
        self._html_frame.load_html(build_html(self.colors))

