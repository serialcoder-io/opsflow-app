import flet as ft
from components.common.sidebar import sidebar

def containers_view(page: ft.Page):
    return ft.Column([
        ft.Text("Page Containers", size=25),
        # autres controls spécifiques à cette vue...
    ])
