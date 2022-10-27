from dataclasses import dataclass

from skills import Skill, FuryPunch, HardShot


@dataclass
class UnitClass:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    stamina: float
    armor: float
    skill: Skill


WarriorClass = UnitClass(
    name="Warrior",
    max_health=60,
    max_stamina=30,
    attack=0.8,
    stamina=0.9,
    armor=1.2,
    skill=FuryPunch(),
) # TODO Инициализируем экземпляр класса UnitClass и присваиваем ему необходимые значения аттрибуотов

ThiefClass = UnitClass(
    name="Thief",
    max_health=50,
    max_stamina=25,
    attack=1.5,
    stamina=1.2,
    armor=1.0,
    skill=HardShot(),
) # TODO действуем так же как и с войном

unit_classes = {
    ThiefClass.name: ThiefClass,
    WarriorClass.name: WarriorClass
}