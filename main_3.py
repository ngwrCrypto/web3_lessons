import random


class Human:
    def __init__(self, name: str, age: int, height : int | float) -> None:
        self.name = name
        self.age = age
        self.height = height

    def show_info(self):
        print(self.name, self.age, self.height)

    @staticmethod
    def when_u_die(year_of_born:int, your_age:int) -> str:
        return f'U will day in {year_of_born + your_age + random.randint(1, 70)} '