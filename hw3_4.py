class Chocolate:
    
    brand: str = "Шоколадная фабрика"
    cocoa_percent: list[int] = [30, 50, 70, 80, 90]
    
    def __init__(self, name: str, chocolate_type: str, weight: int, cocoa: int, filling: str) -> None:
        """
        Инициализация шоколадки.
        
        Параметры:
            name: название шоколада
            chocolate_type: тип (молочный, темный, белый)
            weight: вес в граммах
            cocoa: процент какао
            filling: начинка
        """
        
        self.name: str = name
        self.chocolate_type: str = chocolate_type
        self.weight: int = weight
        self.cocoa: int = cocoa
        self.filling: str = filling
    
    def __str__(self) -> str:
        
        return f"{self.name} ({self.weight}г) - {self.filling}"
    
    def eat(self, grams: int) -> None:
        
        if grams > self.weight:
            print(f"Нельзя съесть больше, чем есть( Осталось {self.weight}г")
        else:
            self.weight -= grams
            print(f"Съедено {grams}г. Осталось {self.weight}г")
    
    def add_filling(self, new_filling: str) -> None:
        """Добавить начинку."""
        if self.filling == "нет":
            self.filling = new_filling
            print(f"Добавлена начинка: {new_filling}")
        else:
            print(f"В шоколаде уже есть начинка: {self.filling}")
    
    def check_cocoa(self) -> str:
        """Проверить содержание какао."""
        if self.cocoa >= 70:
            return "Горький шоколад"
        elif self.cocoa >= 50:
            return "Темный шоколад"
        else:
            return "Молочный шоколад"
    
    def get_info(self) -> str:
        """Вернуть всю информацию о шоколаде."""
        return f"""
Название: {self.name}
Тип: {self.chocolate_type}
Вес: {self.weight}г
Какао: {self.cocoa}%
Начинка: {self.filling}
        """

print("Асортимент шоколада")

choco1 = Chocolate("Милка", "молочный", 100, 32, "нет")
choco2 = Chocolate("Бабаевский", "темный", 90, 75, "орехи")
choco3 = Chocolate("Вдохновение", "горький", 80, 85, "клюква")

print(choco1.get_info())
print(choco2.get_info())
print(choco3.get_info())

print("\nДействия с шоколадом")

print(choco1)
choco1.eat(30)
print(f"Тип: {choco1.check_cocoa()}")
choco1.add_filling("орехи")
print()

print(choco2)
choco2.eat(100)
print(f"Тип: {choco2.check_cocoa()}")
choco2.add_filling("карамель")
print()

print(choco3)
choco3.eat(20)
print(f"Тип: {choco3.check_cocoa()}")
print()
