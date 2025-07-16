import flet as ft
from components.navbutton import nav_button

def sidebar(current_route: str, on_nav) -> ft.Container :
    def section_title(title: str, icon=ft.Icons.CIRCLE) -> ft.Container:
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=ft.Colors.BLUE_200, size=18),
                ft.Text(title, color=ft.Colors.BLUE_200, size=14),
            ]),
            padding=ft.padding.only(top=10, bottom=5)
        )

    return ft.Container(
        width=200,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        content=ft.Column([
            ft.Container(
                content=ft.Text("OpsFlow", size=26, weight="bold", color="white"),
                padding=15,
                bgcolor=ft.Colors.BLUE_900,
                alignment=ft.alignment.center,
                border_radius=3
            ),

            ft.Container(
                content=ft.Column(
                    [
                    section_title("Containeriztion", icon=ft.Icons.TERMINAL),
                    ft.Divider(color="white"),
                    nav_button("Projects", "/", current_route, on_nav, icon=ft.Icons.FOLDER_OUTLINED),
                    nav_button("Images", "/images", current_route, on_nav, icon=ft.Icons.IMAGE_OUTLINED),
                    # nav_button("CI/CD", "/cicd", icon=ft.Icons.SYNC),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                ),
                padding=15,
                bgcolor=ft.Colors.BLUE_GREY_50,
                alignment=ft.alignment.center_left,
            ),

        ])
    )