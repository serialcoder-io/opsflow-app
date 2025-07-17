import flet as ft
from components.navbutton import nav_button

def sidebar(current_route: str, on_nav) -> ft.Container:
    def section_title(title: str, icon=ft.Icons.CIRCLE):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=ft.Colors.BLUE_200, size=18),
                ft.Text(title, color=ft.Colors.BLUE_200, size=14),
            ]),
            padding=ft.padding.only(top=10, bottom=5)
        )

    def nav(label, route, icon):
        return nav_button(
            label=label,
            route=route,
            icon=icon,
            current_route=current_route,
            on_nav=on_nav  # ✅ on_nav est bien passé ici
        )

    return ft.Container(
        width=200,
        bgcolor=ft.Colors.BLUE_GREY_50,
        content=ft.Column([
            ft.Container(
                content=ft.Text("OpsFlow", size=26, weight="bold", color="white"),
                padding=15,
                bgcolor=ft.Colors.BLUE_900,
                alignment=ft.alignment.center
            ),
            ft.Container(
                content=ft.Column([
                    section_title("Containerization", icon=ft.Icons.TERMINAL),
                    ft.Divider(color="white"),
                    nav("Projects", "/", icon=ft.Icons.FOLDER_OUTLINED),
                    nav("Containers", "/containers", icon=ft.Icons.IMAGE_OUTLINED),
                    nav("Images", "/images", icon=ft.Icons.IMAGE_OUTLINED),
                    nav("Volumes", "/volumes", icon=ft.Icons.STORAGE_OUTLINED),
                    nav("Builds", "/builds", icon=ft.Icons.BUILD_OUTLINED),
                ], horizontal_alignment=ft.CrossAxisAlignment.STRETCH),
                padding=15
            ),
        ])
    )
