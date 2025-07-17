import flet as ft

def not_found_view(page: ft.Page):
    return ft.Column([
        ft.Text("404 NOT FOUND", size=30, color=ft.Colors.RED),
        ft.ElevatedButton("Go back to projects", on_click=lambda _: page.go("/"))
    ])
