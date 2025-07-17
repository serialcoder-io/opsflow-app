import flet as ft
from components.sidebar import sidebar
from views import projects, images, containers, not_found

def main(page: ft.Page):

    ROUTES = {
        "/": projects.projects_view,
        "/images": images.images_view,
        "/containers": containers.containers_view,
    }

    sidebar_container = ft.Container(
        width=220,
        bgcolor=ft.Colors.BLUE_GREY_50,
    )

    content_container = ft.Container(expand=True)

    def change_route(route):
        page.go(route)

    def route_change(e: ft.RouteChangeEvent):
        route = page.route
        view_fn = ROUTES.get(route, not_found.not_found_view)
        content_container.content = view_fn(page)
        # update the content of the sidebar
        sidebar_container.content = sidebar(route, change_route)
        page.update()

    page.on_route_change = route_change

    page.add(
        ft.Row(
            [sidebar_container, content_container],
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            expand=True,
        )
    )

    page.go(page.route)

ft.app(target=main)
