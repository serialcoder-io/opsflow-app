import flet as ft
from components.sidebar import sidebar
from views import projects, images, containers, not_found

def main(page: ft.Page):
    ROUTES = {
        "/": projects.projects_view,
        "/images": images.images_view,
        "/containers": containers.containers_view,
    }

    # Sidebar once, container fixe
    sidebar_container = ft.Container(width=220, expand=False)
    content_container = ft.Container(expand=True)

    def change_route(route):
        page.go(route)

    def route_change(e: ft.RouteChangeEvent):
        route = page.route
        view_fn = ROUTES.get(route, not_found.not_found_view)
        content_container.content = view_fn(page)
        sidebar_container.content = sidebar(route, change_route) 
        page.update()

    # Add global layout: sidebar + content_container
    page.add(
        ft.Row([
            sidebar_container,
            content_container,
        ])
    )

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
