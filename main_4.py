class Weapon:
    def fire(self):
        pass

class Pistol(Weapon):
    def fire(self):
        print("Pistol fires a bullet")

class Bazooka(Weapon):
    def fire(self):
        print("Bazooka fires a rocket")

class Human:
    def shoot(self, weapon):
        weapon.fire()


        