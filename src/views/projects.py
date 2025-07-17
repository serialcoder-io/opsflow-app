import flet as ft

def projects_view(page: ft.Page):
    def dropdown_changed(e):
        e.control.color = e.control.value
        page.update()
    
    project_path_text = ft.TextField(
        adaptive=True,
        label="/project/path",
        label_style=ft.TextStyle(color=ft.Colors.GREY_600),
        width=500
    )

    def on_file_picker_result(e: ft.FilePickerResultEvent):
        if e.path:
            print("Chemin sélectionné :", e.path)
            project_path_text.value = e.path
            page.update()
    
    file_picker = ft.FilePicker(on_result=on_file_picker_result)
    page.overlay.append(file_picker)


    return ft.ResponsiveRow(
        [
            ft.Column(
                col={"md": 6},
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.GREY_200,
                        border_radius=6,
                        padding=0,
                        expand=True,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                # header
                                ft.Container(
                                    content=ft.Text("New Project", size=22, weight="medium", color=ft.Colors.GREY_900),
                                    padding=15,
                                    alignment=ft.alignment.center,
                                ),

                                # body
                                ft.Container(
                                    padding=ft.padding.symmetric(horizontal=30, vertical=15),
                                    alignment=ft.alignment.center,
                                    expand=True,
                                    content=ft.Column([
                                        ft.Text("Project path (root folder)", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                                        project_path_text,
                                        ft.ElevatedButton(
                                            text="Browse",
                                            icon=ft.Icons.FOLDER_OPEN,
                                            on_click=lambda e: file_picker.get_directory_path(dialog_title="Select Project Directory")
                                        ),
                                        ft.Container(
                                            expand=True,
                                            content=ft.Column([
                                                ft.ResponsiveRow(
                                                    [
                                                        ft.Column(
                                                            col={"sm": 6},
                                                            expand=True,
                                                            controls=[
                                                                ft.Text("language", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                                                                ft.Dropdown(
                                                                    editable=True,
                                                                    expand=True,
                                                                    options=[
                                                                        ft.dropdown.Option("python"),
                                                                        ft.dropdown.Option("node.js")
                                                                    ],
                                                                    on_change=dropdown_changed,
                                                                )
                                                            ]
                                                        ),
                                                        ft.Column(
                                                            col={"sm": 6},
                                                            expand=True,
                                                            controls=[
                                                                ft.Text("language", theme_style=ft.TextThemeStyle.BODY_MEDIUM),
                                                                ft.Dropdown(
                                                                    editable=True,
                                                                    expand=True,
                                                                    options=[
                                                                        ft.dropdown.Option("Django"),
                                                                        ft.dropdown.Option("FastApi")
                                                                    ],
                                                                    on_change=dropdown_changed,
                                                                )
                                                            ]
                                                        )
                                                    ]
                                                )
                                            ])
                                        )
                                    ])
                                ),
                            ]
                        )
                    )
                ],
            ),
            ft.Column(
                col={"md": 6},
                expand=True,
                controls=[
                    ft.Container(
                        bgcolor=ft.Colors.GREY_200,
                        border_radius=6,
                        padding=0,
                        content=ft.Column(
                            spacing=0,
                            controls=[
                                ft.Container(
                                    content=ft.Text("Preview", size=22, weight="medium", color=ft.Colors.GREY_900),
                                    padding=15,
                                    alignment=ft.alignment.center,
                                ),
                                ft.Container(
                                    padding=15,
                                    alignment=ft.alignment.center,
                                    content=ft.Text("Preview content")  # exemple
                                ),
                            ]
                        )
                    )
                ],
            ),
        ],
        expand=True,
    )
