from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Laptop(Device):
    def turn_on(self):
        return "Ноутбук: нажата кнопка питания, загрузка ОС..."

    def turn_off(self):
        return "Ноутбук: завершение работы, экран гаснет"

class Smartphone(Device):
    def turn_on(self):
        return "Смартфон: Длинное нажатие кнопки, логотип производителя, загрузка ОС..."

    def turn_off(self):
        return "Смартфон: меню выключения, подтверждение действия, экран гаснет"

laptop = Laptop()
smartphone = Smartphone()
print(f"{laptop.turn_on()} \n{laptop.turn_off()}")
print(f"{smartphone.turn_on()} \n{smartphone.turn_off()}")