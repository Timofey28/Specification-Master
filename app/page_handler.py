from .pages import CurrentPage


class PageHandler:
    def __init__(self, current_page: CurrentPage):
        self.current_page = current_page
        self.__load_page()

    def go_to(self, new_page: CurrentPage):
        if type(self.current_page) != type(new_page):
            self.current_page = new_page
            self.__load_page()

    def __load_page(self):
        self.current_page.load_page()