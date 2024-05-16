import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import logging
from . import CurrentPage


class Projects(CurrentPage):
    def __init__(self, page: ft.Page, logging_level: int):
        super().__init__()
        self.page = page
        logging.getLogger("httpx").setLevel(logging_level)

    def load_page(self):
        self.page.clean()
        self.page.title = 'Проекты'
        self.page.add(
            Row(
                controls=[
                    Column([
                        Text('You are logged in!')
                    ])
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )