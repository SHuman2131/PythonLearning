class Livestock:
    name = ''
    weight = 0
    animal_type = ''
    sound = ''

    def __init__(self, name, weight, animal_type, sound):
        self.name = name
        self.weight = weight
        self.animal_type = animal_type
        self.sound = sound

    def feed(self):
        print(f'{self.name} была покормлена')

    def voice(self):
        print(self.name, ' говорит "', self.sound, '"')


class MilkArtiodactyl(Livestock):
    def get_milk(self):
        if not isinstance(self, Livestock):
            return 'Переданное животное не принадлежит классу Livestock'
        print('Вы подоили ', self.name)


class EggBird(Livestock):
    def get_eggs(self):
        if not isinstance(self, Livestock):
            return 'Переданная птица не принадлежит классу Livestock'
        print('Вы собрали яйца у ', self.name)


class Goose(Livestock, EggBird):
    animal_type = 'Гусь'
    sound = 'Га га га'

    def __init__(self, name, weight=3):
        self.name = name
        self.weight = weight


class Cow(Livestock, MilkArtiodactyl):
    animal_type = 'Корова'
    sound = 'Мууууу'

    def __init__(self, name, weight=50):
        self.name = name
        self.weight = weight


class Sheep(Livestock):
    animal_type = 'Овца'
    sound = 'Бееее'

    def __init__(self, name, weight=15):
        self.name = name
        self.weight = weight


class Сhicken(Livestock, EggBird):
    animal_type = 'Курица'
    sound = 'Ко ко ко ко'

    def __init__(self, name, weight=1):
        self.name = name
        self.weight = weight


class Goat(Livestock, MilkArtiodactyl):
    animal_type = 'Коза'
    sound = 'Мееее'

    def __init__(self, name, weight=10):
        self.name = name
        self.weight = weight


class Duck(Livestock, MilkArtiodactyl):
    animal_type = 'Утка'
    sound = 'Кря'

    def __init__(self, name, weight=2):
        self.name = name
        self.weight = weight


