class MenuOption:

    __description: str
    __action: any
    __sub_options: dict

    def __init__(self, description: str, action: any) -> None:
        self.__description = description
        self.__action = action
        self.__sub_options = {}

    def get_description(self) -> str:
        return self.__description

    def execute(self) -> None:
        self.__action()

    def add_sub_option(self, option) -> None:
        index = len(self.__sub_options.keys()) + 1
        self.__sub_options[index] = option

    def get_sub_options(self) -> dict:
        return self.__sub_options