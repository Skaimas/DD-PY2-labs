class Dog:
    def __init__(self, age: int, weight: float):
        """
        Параметры объекта базового класса собака

        :param age: возраст в обычных годах собаки
        :param weight: вес собаки

        Примеры:
        >>> Dog("Белый", 6, 46.7)
        """
        if not isinstance(age, int):
            raise TypeError("Аргумент age должен иметь тип int")
        if not isinstance(weight, float):
            raise TypeError("Аргумент weight должен иметь тип float")

        self.age = age
        self.weight = weight

    def __str__(self):
        """
        :return: Возвращает строку параметров объекта класса

        Примеры:
        >>> print(Dog(6, 46.7))
        """
        return f"Возраст собаки: {self.age!r}, Вес собаки: {self.weight!r}"

    def __repr__(self):
        """
        :return: Возвращает строку аргументов объекта класса и их значений

        Примеры:
        >>> print(repr(Dog(6, 46.7)))
        """
        return f"{self.__class__.__name__}(age = {self.age!r}, weight = {self.weight!r})"

    def Dog_Years(self) -> str:
        """
        Считает возраст собаки в собачьих годах

        :return: Возвращает строку с возрастом собаки в собачиьх годах

        Примеры:
        >>> print(Dog(4, 23.6).Dog_Years())
        """
        s = 0
        dy = 0
        for i in range(self.age):
            if i == 0:
                s = 15
            elif i == 1:
                s = 9
            elif i >= 2:
                s = 5
            dy += s
        return f"Возраст собаки в собачьих годах: {dy}"

    def AVG_weight(self) -> str:
        """
        В расчет берутся средние собаки

        :return: Вернет строку состояния собаки взависимости от веса собаки

        Примеры:
        >>> print(Dog(5, 26.2).AVG_weight())
        """


class Pedigree_Dog(Dog):
    def __init__(self, age, weight, breed: str):
        """
        Параметры объекта дочернего класса пародистая собака

        :param age: возраст в обычных годах собаки
        :param weight: вес собаки
        :param breed: парода собаки (причина инкапсуляции: невозможно изменить пароду собаки как
                                                                                            и национальность человека)

        Примеры:
        >>> Pedigree_Dog(5, 10.42, "Шпиц")
        """
        super().__init__(age, weight)
        if not isinstance(breed, str):
            raise TypeError("Аргумент breed должен иметь тип str")

        self.age = age
        self.weight = weight
        self._breed = breed

    @property
    def breed(self):
        return self._breed

    def __str__(self):
        """
        :return: Возвращает строку параметров объекта класса

        Примеры:
        >>> print(Pedigree_Dog(6, 46.7, "Немецкая овчарка"))
        """
        return f"Возраст собаки: {self.age!r}, Вес собаки: {self.weight!r}, Парода собаки: {self._breed}"

    def __repr__(self):
        """
        :return: Возвращает строку аргументов объекта класса и их значений

        Примеры:
        >>> print(repr(Pedigree_Dog(6, 46.7, "Немецкая овчарка")))
        """
        return f"{self.__class__.__name__}(age = {self.age!r}, weight = {self.weight!r}, breed = {self._breed!r})"

    def AVG_weight(self) -> str:
        """
        В данном случае требуется перегрузка метода, потому что средний вес пародистых собак различается

        :return: Вернет строку состояния собаки взависимости от веса собаки

        Примеры:
        >>> print(Pedigree_Dog(7, 72, "Английский мастиф"))
        """
