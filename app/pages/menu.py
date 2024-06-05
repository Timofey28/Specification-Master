import flet as ft
import logging

from database import Database
from .menu_strategies.chief_engineer import ChiefEngineer
from .menu_strategies.lead_employee import LeadEmployee


class Menu:
    def __init__(self, page: ft.Page, logging_level: int, db: Database):
        self.page = page
        self.logging_level = logging_level
        self.db = db
        self.user_id = None

        logging.getLogger("httpx").setLevel(logging_level)

        # Инициализируем произвольную стратегию исключительно для того, чтобы можно было инициализировать переменную
        # button_logout в абстрактном классе и, обратившись к ней из App, присвоить полю on_click функцию действия из
        # App. Чтобы потом при смене стратегий меню перед новой инициализацией запоминать ссылку на on_click-действие
        # из верхнего уровня App и присваивать ее новому объекту, потому что отсюда обратиться к этой функции невозможно )))
        self.menu_strategy = ChiefEngineer(self.page, self.logging_level, self.db)

    def load_page(self, user_id: int):
        self.user_id = user_id
        self.page.title = 'Главная'

        # Save links to actions
        action_when_logout = self.menu_strategy.button_logout.on_click

        if user_id == 1:
            self.menu_strategy = ChiefEngineer(self.page, self.logging_level, self.db)
        else:
            self.menu_strategy = LeadEmployee(self.page, self.logging_level, self.db, user_id)

        # Assign them back to a new object
        self.menu_strategy.button_logout.on_click = action_when_logout

        self.menu_strategy.load_page()