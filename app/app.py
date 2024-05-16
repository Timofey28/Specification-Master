import flet as ft
import logging
from .pages import CurrentPage
from .pages.auth import Auth
from .pages.projects import Projects
from .page_handler import PageHandler


class App:
    def __init__(self, page: ft.Page):
        self.page = page

        # Настройка логов
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            filename='info.log',
            filemode='w',
            level=logging.INFO
        )

        self.auth: CurrentPage = Auth(page, logging.INFO)
        self.projects: CurrentPage = Projects(page, logging.INFO)
        # self.auth: CurrentPage =
        # self.auth: CurrentPage =
        # self.auth: CurrentPage =

        self.page_handler = None

    def run(self):
        self.page_handler = PageHandler(self.auth)
        print('noooooooooooooooooo')
        self.page_handler = PageHandler(self.projects)