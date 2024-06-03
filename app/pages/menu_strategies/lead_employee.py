import flet as ft
from flet_core.control_event import ControlEvent

from . import MenuStrategy


class LeadEmployee(MenuStrategy):

    def load_page(self) -> None:
        self.page.clean()

    def change_menu_section(self, e: ControlEvent) -> None:
        pass


    def build_section_projects(self) -> None:
        pass

    def build_section_create_project(self) -> None:
        pass

    def build_section_print_statement(self) -> None:
        pass

    def build_section_employees(self) -> None:
        pass

    def build_section_add_account(self) -> None:
        pass

    def build_section_settings(self) -> None:
        pass