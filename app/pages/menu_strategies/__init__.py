from abc import ABC, abstractmethod
import flet as ft
from flet_core.control_event import ControlEvent
import logging

from database import Database
from app.config import *


class MenuStrategy(ABC):
    def __init__(self, page: ft.Page, logging_level: int, db: Database, user_id: int = 1):
        self.page = page
        self.logging_level = logging_level
        self.db = db
        self.user_id = user_id
        self.current_section_index = 0

        self.permanent_elements = None
        self.content = None
        self.reserved = None
        self.right_side = None
        self.rail = None

        logging.getLogger("httpx").setLevel(self.logging_level)

        self.header_properties = header_properties
        self.textfield_properties = textfield_properties

        # Elements-links to other pages
        self.button_logout = ft.IconButton(
            icon=ft.icons.LOGOUT,
            tooltip='Выйти из аккаунта',
        )

        logging.debug('Initialized MenuStratagy object')

    @abstractmethod
    def load_page(self) -> None:
        pass

    @abstractmethod
    def change_menu_section(self, e: ControlEvent) -> None:
        pass


    @abstractmethod
    def build_section_projects(self) -> None:
        pass

    @abstractmethod
    def build_section_create_project(self) -> None:
        pass

    @abstractmethod
    def build_section_print_statement(self) -> None:
        pass

    @abstractmethod
    def build_section_employees(self) -> None:
        pass

    @abstractmethod
    def build_section_add_account(self) -> None:
        pass

    @abstractmethod
    def build_section_settings(self) -> None:
        pass