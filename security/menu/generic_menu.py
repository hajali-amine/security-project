import abc


class GenericMenu(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init_menu(self):
        """ Gets parameters if needed """

    @abc.abstractmethod
    def start_menu(self):
        """ Starts the menu """

    def launch(self):
        self.init_menu()
        self.start_menu()
