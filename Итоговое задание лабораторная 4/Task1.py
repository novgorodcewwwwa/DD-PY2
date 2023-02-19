class Cartoon:
    def __init__(self, name: str, dur: int):
        """
        Создание объекта класса мультфильм
        :param name: название мультфильма
        :param dur: продолжительность мультфильма (в минутах)
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)  #Инициализация объекта класса
        """
        self.name = name  # Название мультфильма можно менять, как и его тип (не рекомендуется)
        self.duration = dur
        self._comm = None  # Комментарий к мультфильму, по умолчанию отсутствует, для добавления применить метод add_comm
        self._accordance = None  # Параметр соответствия мультфильма теме, по умолчанию отсутствует, добавляется методом


    def add_comm(self, message: str):
        """
        Метод, позволяющий оставить комментарий к мультфильму
        :param message:
        :return:
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)  #Инициализация объекта класса
        >>> test_cartoon.add_comm("Добрый и поучительный мультик, смотрим всей семьей не в первый раз")
        """
        self._comm = message

    def write_com(self):
        """
        Метод, позволяющий вернуть ранее оставленный комментарий к мультфильму
        :return: возвращает комментарий
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)  #Инициализация объекта класса
        >>> test_cartoon.add_comm("Добрый и поучительный мультик, смотрим всей семьей не в первый раз")
        >>> test_cartoon.write_com()
        'Добрый и поучительный мультик, смотрим всей семьей не в первый раз'
        """
        return self._comm

    def add_accordance(self, rating: float):
        """
        Метод, позволяющий добавить степень соответствия мультфильма теме
        :param rating: степень соответствия мультфильма теме (от 0 до 10)
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)
        >>> test_cartoon.add_accordance(8.9)
        """

        if isinstance(rating, float):
            if 10. >= rating >= 0.:
                self._accordance = rating
            else:
                raise ValueError("accordance must be from 0 to 10")
        else:
            raise TypeError("accordance must be float")

    def check_accordance(self):
        """
        Метод, печатающий степень соответствия мульфильма теме. Предварительно необходимо добавить её к экземпляру класса
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)
        >>> test_cartoon.add_accordance(8.9)
        >>> test_cartoon.check_accordance()
        Соответствие мультфильма теме: 8.9
        """
        print(f'Соответствие мультфильма теме: {self._accordance}')


    @property
    def duration(self):
        """
        Геттер для атрибута (длительности) мультфильма
        :param self:
        :return:
        """
        return self._duration

    @duration.setter  # Длительность мультфильма должна быть положительным целым числом, поэтому создан атрибут
    def duration(self, dur: int):
        """
        Cеттер для атрибута (длительности) фильма
        :param self:
        :param dur: длительность мультфильма
        :return:
        """
        if isinstance(dur, int):
            if dur > 0:
                self._duration = dur
            else:
                raise ValueError(f'duration of cartoon must be greater than zero, while incoming {dur}')
        else:
            raise ValueError(f'cartoon duration must be int, while incoming is {type(dur)}')

    def __str__(self):
        """
        Магический метод __str__
        :return: Возвращает название и длительность мультфильма
        Примеры:
        >>> test_cartoon = Cartoon ("Frozen", 102)
        >>> print(test_cartoon)
        Мультфильм "Frozen", длительность 102
        """
        return f'Мультфильм "{self.name}", длительность {self.duration}'

    def __repr__(self):
        """
        Магический метод, выдающий строку, необходимую для инициализации фильма
        :return:
        Примеры:
        >>> test_cartoon = Cartoon("Frozen", 102)
        >>> repr(test_cartoon)
        "Cartoon(name='Frozen', dur=102)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration})"


class Anime(Cartoon):
    def __init__(self, name: str, dur: int, year: int):
        """
        Создание объекта класса мультфильм жанра аниме
        :param name: название мультфильма
        :param dur:  длительность мультфильма
        :param year: год, когда создан мультфильм
        Примеры:
        >>> test_cartoon = Anime ("Bubble", 126, 2022) # инициализация объекта класса
        """
        super().__init__(name, dur)  # имя и длительность наследуются
        self.year = year
        self._comm = None
        self._accordance = None


    def __str__(self):  # Перегрузка необходима в связи с добавлением "жанра аниме" и параметра (год)
        """
        Магический метод __str__
        :return: Возвращает название и длительность мультфильма
        Примеры:
        >>> test_cartoon = Anime ("Bubble", 126, 2022)
        >>> print(test_cartoon)
        Мультильм жанра аниме "Bubble" , длительность 126, 2022 год
        """
        return f'Мультфильм жанра аниме "{self.name}", длительность {self.duration}, {self.year} год'

    def __repr__(self):  # Перегрузка необходима ради введения в метод нового параметра (год)
        """
        Магический метод, выдающий строку, необходимую для инициализации мультфильма жанра аниме
        :return:
        Примеры:
        >>> test_cartoon = Anime ("Bubble", 126, 2022)
        >>> print(repr(test_cartoon))
        Anime(name='Bubble', dur=126, year=2022)
        """
        return f"{self.__class__.__name__}(name={self.name!r}, dur={self.duration}, year={self.year})"

    def check_accordance(self):  # методу необходима перегрузка, чтобы показывать степень соответствия жанру
        """
        Метод, печатающий степень соответствия мультфильма жанру аниме, ранее добавленную
        методом add_accordance
        Примеры:
        >>> test_cartoon = Anime ("Bubble", 126, 2022)
        >>> test_cartoon.add_accordance(9.5)
        >>> test_cartoon.check_accordance()
        Степень соответствия мультфильма жанру аниме:9.5
        """
        print(f'Степень соответствия мультфильма жанру аниме:{self._accordance}')



if __name__ == "__main__":
    # Write your solution here
    """
    Унаследованы методы add_accordance, add_comm и write_comm. Метод check_accordance перегружен
    """
    pass

















