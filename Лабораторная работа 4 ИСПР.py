if __name__ == "__main__":
    class People:
        def __init__(self, age: int, name: str) -> None:
            """
            Создание и подкотовка объекта "Человек"

            :param age: возраст человека
            :param name: имя человека
            """
            self.name = name
            self.age = age

        def say_hello(self) -> str:
            """
            Метод, который будет перезагружаться в дочернем классе.
            (человек здоровается)
            """
            return "Hi"

        def __str__(self) -> str:
            """
            Метод, возвращающий строковое представление человека
            """
            return f"{self.name}, Age: {self.age}"

        def __repr__(self) -> str:
            """
            Метод, возвращающий строковое представление человека
            (Отличие в том, что метод __repr__ более строгий и больше понятен разработчику)
            """
            return f"People(name='{self.name}', age={self.age})"

    class Kid(People):
        def __init__(self, age: int, name: str, gender: str) -> None:
            """
            Создание и подкотовка объекта "Ребенок"
            (Дочерний класс "People")

            :param age: возраст ребенка
            :param name: имя ребенка
            :param gender: пол ребенка
            """
            super().__init__(name, age)
            self._gender = gender  # делаем атрибут защищеным, добавив нижнее подчеркивание вначале атрибута

        def say_hello(self) -> str:
            """
            Перегруженный метод, который вернет приветствие, сказанное ребенком
            """
            return "hello"

        def __str__(self) -> str:
            """
            Добавляем пол ребенка в строковое представление из класса People
            """
            return f"{super().__str__()}, gender: {self._gender}"

        def __repr__(self) -> str:
            """
            по аналогии с str добавляем атрибут gender
            """
            return f"kid(name='{self.name}', age={self.age}, gender='{self._gender}')"

    # Рассмотрим пример работы кода:
    kid =Kid("Женя", 14, "Девочка")

    print(kid)
    print(kid.say_hello())
    # После запуска кода убеждаемся, что он рабочий
    pass
