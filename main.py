import flet as ft
from app import App


def main(page: ft.Page):
    app = App(page)
    app.run()


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)