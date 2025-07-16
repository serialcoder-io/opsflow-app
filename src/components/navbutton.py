import flet as ft

def nav_button(
        label: str, 
        route: str,
        current_route: str, 
        on_nav,
        icon=ft.Icons.CIRCLE
    ):
        is_active = current_route == route
        return ft.Container(
            border_radius=6,
            bgcolor=ft.Colors.BLUE_GREY_100 if is_active else ft.Colors.TRANSPARENT,
            border=ft.border.only(
                left=ft.BorderSide(4, ft.Colors.BLUE_400) if is_active else ft.BorderSide(0, ft.Colors.TRANSPARENT)
            ),
            padding=ft.padding.symmetric(vertical=10, horizontal=10),
            on_click=lambda e: on_nav(route),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(icon, size=18),
                    ft.Text(label)
                ]
            ),
            alignment=ft.alignment.center_left
        )