class Book:
    def __init__(self, pages: int, notClearPages: int, color: str):
        self.profit = None
        if not isinstance(pages, int):
            raise TypeError('Number of pages should be int')
        self.pages = pages
        if notClearPages < 0:
            raise ValueError('not Clear pages cant be less then 0')
        self.notClearPages = notClearPages
        if not isinstance(color, str):
            raise TypeError('Color should be str')
        self.color = color

    def torn(self):
        print(' ')
        self.profit = 0


class Car:
    def __init__(self, color: str, doors, carNumber: str):
        self.health = None
        if not isinstance(color, str):
            raise TypeError('Color should be str')
        self.color = color
        if doors <= 0:
            raise TypeError('Car cant be without doors!')
        self.doors = doors
        if not isinstance(carNumber, str):
            raise TypeError('number should be str')
        self.carNumber = carNumber

    def broken(self):
        print(' ')
        self.health = 0


class House:
    def __init__(self, floors: int, entr: int):
        if not isinstance(floors, int):
            raise TypeError('floors should be int')
        if floors <= 0:
            raise ValueError('floors > 0')
        self.height = floors
        if entr <= 0:
            raise ValueError('entr > 0')
        self.entr = entr


if __name__ == "__main__":
    Lada_1 = Car('Синий', 5, 'KZ587234')
    Lada_2 = Car('Красный', 5, 'KZ9834718')
    myBook = Book(100, 90, "GGWP")
    house_1 = House(9, 2)
    house_2 = House(1, 1)
    import doctest

    doctest.testmod()
    pass
