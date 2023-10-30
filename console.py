import sys
from os import system
from menu_option import MenuOption

class Console:

    __menu: dict

    def __init__(self) -> None:
        self.__menu = {}

    def add_option(self, option: MenuOption) -> None:
        index = len(self.__menu.keys()) + 1
        self.__menu[index] = option

    def start(self):
        self.run(self.__menu, 'Salir', self.close)

    def clear(self):
        if system('cls') > 0:
            system('clear')

    def close(self):
        sys.exit()

    def execute_option(self, option_number: int):
        option = self.__menu[option_number]
        sub_menu = option.get_sub_options()
        if len(sub_menu.keys()) > 0:
            self.run(sub_menu, 'Regresar', None)
        else:
            option.execute()
            input('\npresione enter para continuar...')

    def run(self, menu: dict, break_lable: str, break_method) -> None:
        last_option_number = len(menu.keys()) + 1
        while True:
            self.clear()
            option = self.get_selected_option(menu, last_option_number, break_lable)
            if option == last_option_number:
                if break_method is None:
                    return
                else:
                    break_method()
            else:
                self.execute_option(option)
    
    def print_menu(self, menu: dict, break_option_number: int, break_lable: str) -> None:
        for key in menu:
            print(str(key) + '. ' + menu[key].get_description())
        print(str(break_option_number) + '. ' + break_lable)

    def get_selected_option(self, menu: dict, break_option_number: int, break_lable: str) -> int:
        well_input = True
        while True:
            if well_input:
                self.print_menu(menu, break_option_number, break_lable)
                option = input('\nDigite su opcion:\n')
            else:
                option = input('\nDigite una opcion valida:\n')

            if option.isdigit() and int(option) > 0 and int(option) <= break_option_number:
                return int(option)
            else:
                well_input = False