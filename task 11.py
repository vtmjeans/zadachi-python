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
d = Dessert()
d.set_name("Торт")
d.set_calories(150)
print(d.get_name())         
print(d.get_calories())   
print(d.is_healthy())       
print(d.is_delicious())     