import flet as ft
from flet import TextField, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent
import logging
from . import CurrentPage


class Auth(CurrentPage):
    def __init__(self, page: ft.Page, logging_level: int):
        super().__init__()
        self.page = page
        logging.getLogger("httpx").setLevel(logging_level)

        # Page elements
        self.input_login = TextField(label='Логин', text_align=ft.TextAlign.LEFT)
        self.input_password = TextField(label='Логин', text_align=ft.TextAlign.LEFT, password=True)
        self.button_submit = ElevatedButton(text='Войти', disabled=True)

        # Element actions
        self.input_login.on_change = self.validate
        self.input_password.on_change = self.validate
        self.button_submit.on_click = self.submit

    def load_page(self) -> None:
        self.page.clean()
        self.page.title = 'Авторизация'
        self.page.add(
            Row(
                controls=[
                    Column([
                        self.input_login,
                        self.input_password,
                        self.button_submit
                    ])
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    def validate(self, e: ControlEvent) -> None:
        if all([self.input_login.value, self.input_password.value]):
            self.button_submit.disabled = False
        else:
            self.button_submit.disabled = True
        self.page.update()

    def submit(self, e: ControlEvent):
        login = self.input_login.value
        password = self.input_password.value
        self.page.window_destroy()