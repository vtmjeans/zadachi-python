class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_calories(self):
        return self._calories

    def set_calories(self, value):
        self._calories = value

    def is_healthy(self):
        return self._calories is not None and self._calories < 200

    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        super().__init__(name, calories)  
        self._flavor = flavor

    def get_flavor(self):
        return self._flavor

    def set_flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        if self.get_flavor() == "black licorice":
            return False
        return super().is_delicious()
d = Dessert()
print("Тест 1: Dessert без параметров")
print("is_delicious():", d.is_delicious())  

d2 = Dessert("ВКУСНЯШКА", 300)
print("\nТест 2: Десерт с данными")
print("Name:", d2.get_name())              
print("Calories:", d2.get_calories())      
print("is_healthy():", d2.is_healthy())    
print("is_delicious():", d2.is_delicious())


j = JellyBean("Мармелад", 100)
print("\nТест 3: JellyBean без указания вкуса")
print("Name:", j.get_name())              
print("Calories:", j.get_calories())     
print("is_healthy():", j.is_healthy())   
print("is_delicious():", j.is_delicious())

j2 = JellyBean("Желе", 150, "black licorice")
print("\nТест 4: JellyBean со вкусом 'black licorice'")
print("Name:", j2.get_name())              
print("Flavor:", j2.get_flavor())          
print("is_delicious():", j2.is_delicious())  

