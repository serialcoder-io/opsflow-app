import flet as ft
from components.sidebar import sidebar

def projects_view(page: ft.Page):
    return ft.Column([
        ft.Text("Page Projets", size=25),
        # autres controls spécifiques à cette vue...
    ])
