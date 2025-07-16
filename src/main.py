import flet as ft
from components.sidebar import sidebar

def main(page: ft.Page):
    page.title = "OpsFlow"
    current_route = "/"

    content_container = ft.Container(expand=True)
    sidebar_container = ft.Container(width=200)

    def change_route(route):
        nonlocal current_route
        current_route = route
        update_view()

    def update_view():
        # Update le contenu central
        content_container.content = ft.Text(f"You are on {current_route}", size=25)
        # Update la sidebar en lui passant la route actuelle
        sidebar_container.content = sidebar(current_route, change_route)
        page.update()

    # Initial layout (structure fixe)
    page.add(
        ft.Row([
            sidebar_container,
            ft.VerticalDivider(width=1),
            content_container
        ])
    )

    update_view()

ft.app(target=main)