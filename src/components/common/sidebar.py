import flet as ft
from ui import nav_button

def sidebar(current_route: str, on_nav) -> ft.Container:

    def section_title(title: str, icon=ft.Icons.CIRCLE):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=ft.Colors.GREY_600, size=18),
                ft.Text(title, color=ft.Colors.GREY_600, size=14),
            ]),
            padding=ft.padding.only(top=8, bottom=0, left=10, right=10)
        )

    # create a button
    def nav(label, route, icon):
        return nav_button(
            label=label,
            route=route,
            icon=icon,
            current_route=current_route,
            on_nav=on_nav
        )

    return ft.Container(
        width=220,
        expand=True,
        bgcolor=ft.Colors.BLUE_GREY_50,
        border_radius=10,
        content=ft.Column(
            [
                # sidebar header(title)
                ft.Container(
                    content=ft.Text("Opsflow", size=26, weight="bold", color="white"),
                    padding=15,
                    bgcolor=ft.Colors.BLUE_900,
                    alignment=ft.alignment.center,
                    border_radius=6
                ),
                # sidebar content
                ft.Container(
                    content=ft.Column([
                        section_title("Containerization", icon=ft.Icons.TERMINAL),
                        ft.Divider(color=ft.Colors.GREY_300),
                        nav("Projects", "/", icon=ft.Icons.FOLDER_OUTLINED),
                        nav("Containers", "/containers", icon=ft.Icons.IMAGE_OUTLINED),
                        nav("Images", "/images", icon=ft.Icons.IMAGE_OUTLINED),
                        nav("Volumes", "/volumes", icon=ft.Icons.STORAGE_OUTLINED),
                        nav("Builds", "/builds", icon=ft.Icons.BUILD_OUTLINED),
                    ], horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
                    padding=15
                ),
            ],
            spacing=0,
            tight=True,
            expand=True,
        )
    )
