import flet as ft
from flet_core.control_event import ControlEvent
import logging

from data import db_dbname, db_host, db_user, db_password
from database import Database
from .pages import Auth, Menu


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.db = Database(
            db_dbname=db_dbname,
            db_host=db_host,
            db_user=db_user,
            db_password=db_password
        )
        self.page.theme_mode = ft.ThemeMode.DARK
        # self.page.window_width = 800
        # self.page.window_height = 500
        self.title = None
        self.auth = None
        self.menu = None
        self.menu_specific_strategy = None

        # Настройка логов
        logging.basicConfig(
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            # filename='info.log',
            filemode='w',
            level=logging.INFO
        )

        logging.debug('Initialized App object')

    def run(self):
        self.title = 'Авторизация'
        self.auth = Auth(self.page, logging.INFO)
        self.menu = Menu(self.page, logging.INFO, self.db)
        self.menu_specific_strategy = self.menu.menu_strategy

        # Связь между страницами
        self.auth.button_submit.on_click = self.button_auth_submit
        self.menu_specific_strategy.button_logout.on_click = self.button_menu_logout

        # self.auth.load_page()
        self.menu.load_page(1)

    def button_auth_submit(self, e: ControlEvent):
        login = self.auth.input_login.value.strip()
        password = self.auth.input_password.value
        user_id = self.db.login_employee(login, password)
        if user_id:
            self.menu.load_page(user_id)
        else:
            self.auth.wrong_password_alert()

    def button_menu_logout(self, e: ControlEvent):
        self.auth.load_page()