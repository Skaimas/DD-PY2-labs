import doctest


class Song:
    def __init__(self, name: str, ganre: str):
        """
        Параметры объекта

        :param name: название
        :param ganre: жанр

        Пример ( Rammstein :) ):
        >>> song = Song("Engel", "Rock")
        """
        if not isinstance(name, str):
            raise TypeError("Данный параметр должен быть типа str")
        if not isinstance(ganre, str):
            raise TypeError("Данный параметр должен быть типа str")

    def Ganre_is_Rock(self) -> bool:
        """
        Функция которая проверят евляется ли жанр песни роком

        :return:Является ли жарн роком

        Примеры:
        >>> song = Song("Engel", "Rock")
        >>> Song.Ganre_is_Rock()
        """

    def Ganre_is_Rep(self) -> bool:
        """
        Функция которая проверят евляется ли жанр песни рэпом

        :return:Является ли жарн рэпом

        Примеры:
        >>> song = Song("Engel", "Rock")
        >>> Song.Ganre_is_Rep()
        """

    def Ganre_is_Jazz(self) -> bool:
        """
        Функция которая проверят евляется ли жанр песни джазом

        :return:Является ли жарн джазом

        Примеры:
        >>> song = Song("Engel", "Jazz")
        >>> Song.Ganre_is_Jazz()
        """


class Fridge:
    def __init__(self, name: str, smart: bool):
        """
        Параметры объекта:

        :param smart: является ли холодильник умным
        :param name: название

        Примеры:
        >>> fridge = Fridge("b-2", False)
        """
        if not isinstance(name, str):
            raise TypeError("Данный параметр должен быть типа str")
        if not isinstance(smart, bool):
            raise TypeError("Данный параметр должен быть типа bool")

    def renaming_fridge(self, new_name: str):
        """
        Изменяет парамерт названия холодильника

        :param new_name: новое название
        :return: возвращает объект с измененым параметром имени

        Примеры:
        >>> fridge = Fridge("b-2", False)
        >>> fridge.renaming_fridge("b-3")
        """
        if not isinstance(new_name, str):
            raise TypeError("Данный параметр должен быть типа str")

    def temperature_setting(self, temp: int, min_temp: int, max_temp: int):
        """
        Установка значения параметра температуры в допустимых приделах
        :param temp: температура которая будет установлена
        :param max_temp: максимальная температура холодильника
        :param min_temp: минимальная температура холодильника
        :return: Возвращает название холодильника и установленную температуру

        Примеры:
        >>> fridge = Fridge("b-2", False)
        >>> fridge.temperature_setting(5, 0, 20)
        """
        if not isinstance(temp, int):
            raise TypeError("Данный параметр должен быть типа int")
        if not isinstance(min_temp, int):
            raise TypeError("Данный параметр должен быть типа int")
        if not isinstance(max_temp, int):
            raise TypeError("Данный параметр должен быть типа int")
        if min_temp < temp:
            raise TypeError("Установленная температура не может быть меньше минимальной")
        if max_temp > temp:
            raise TypeError("Установленная температура не может быть меньше максимальной")

    def smart_or_no(self) -> bool:
        """
        Функция которая проверяет является ли холодильник умным... XD

        :return: проверка наличия ИИ у холодильника

        Примеры:
        >>> fridge = Fridge("b-2", True)
        >>> fridge.smart_or_no()
        """


class Car:
    def __init__(self, brand: str, engine_capacity: float, wheel_size: int):
        """
        Параметры объекта

        :param brand: марка авто
        :param engine_capacity: объем двигателя
        :param wheel_size: размер колес

        Примеры:
        >>> car = Car("toyota mark 2", 2.0, 17)
        """
        if not isinstance(brand, str):
            raise TypeError("Данный параметр должен быть типа str")
        if not isinstance(engine_capacity, (int, float)):
            raise TypeError("Данный параметр должен быть типа int или float")
        if not isinstance(wheel_size, int):
            raise TypeError("Данный параметр должен быть типа int")

    def print_brand(self) -> str:
        """
        Функция выводящая значение параметра name

        :return: вывод значения параметра

        Пример:
        >>> car = Car("toyota mark 2", 2.0, 17)
        >>> car.print_brand()
        """

    def print_engine_capacity(self) -> float:
        """
        Функция выводящая значение параметра name

        :return: вывод значения параметра

        Пример:
        >>> car = Car("toyota mark 2", 2.0, 17)
        >>> car.print_engine_capacity()
        """

    def print_wheel_size(self) -> int:
        """
        Функция выводящая значение параметра name

        :return: вывод значения параметра

        Пример:
        >>> car = Car("toyota mark 2", 2.0, 17)
        >>> car.print_wheel_size()
        """


if __name__ == "__main__":
    doctest.testmod()
