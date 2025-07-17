import flet as ft
from components.sidebar import sidebar

def images_view(page: ft.Page):
    return ft.Column([
        ft.Text("Page Images", size=25),
        # autres controls spécifiques à cette vue...
    ])

