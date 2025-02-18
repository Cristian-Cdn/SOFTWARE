from car import Car
from account import Account
from uberX import UberX
from user import User

if _name_ == "_main_":
    print("Inicializando la info de los carros")

    print("Car")
    car = Car("AMS256", Account("Andres Herrera", "ASD12365", "tucorreo", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberx = UberX("KLO365", Account("Marco Lois", "SGHJ1236", "tucorreo", "7856"), "Toyota", "Corolla")
    print(vars(uberx))
    print(vars(uberx.driver))

    print("User")
    user = User("Mariana Valle", "SDFG125F", "tucorreo", "7856")
    print(vars(user))