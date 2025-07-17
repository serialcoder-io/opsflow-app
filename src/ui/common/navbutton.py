import flet as ft

def nav_button(label: str, route: str, icon=ft.Icons.CIRCLE, current_route="", on_nav=None):
    is_active = current_route == route
    return ft.Container(
        border_radius=6,
        padding=10,
        bgcolor=ft.Colors.GREY_300 if is_active else ft.Colors.TRANSPARENT,
        border=ft.border.only(
            left=ft.BorderSide(4, ft.Colors.BLUE_900)
        ) if is_active else None,
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
