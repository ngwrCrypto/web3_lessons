from icecream  import  ic
import random



class Human:
    def __init__(self, name: str, age: int, height : int | float) -> None:
        self.name = name
        self.age = age
        self.height = height

    @staticmethod
    def when_u_die(year_of_born:int, your_age:int) -> str:
        return f'U will day in {year_of_born + your_age + random.randint(1, 70)} '

    def __repr__(self) -> str:
        return f"Human({self.name}, {self.age}, {self.height})"



class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('Initialize {0}'.format(self.name))

        Robot.population += 1


    def __del__(self):
        '''i`m dying'''
        print('{0} is dying'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} is the last one'.format(self.name))
        else:
            print('There are still {0} robots working'.format(Robot.population))


    def sayHi(self):
        print('Hi, my name is {0}'.format(self.name))

    @staticmethod
    def howMany():
        print('We have {0} robots'.format(Robot.population))



droid1 = Robot('R2-D2')
droid1.sayHi()

droid2 = Robot('C-3PO')
droid2.sayHi()

print('robot doing some work')
print('lets destoy them')
# del droid1
# del droid2

# Robot.howMany()
