class Animal:
    def __init__(self, name, age, color, weight):
        self.name = name
        self.age = age
        self.color = color
        self.weight = weight
    def print_info(self):
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")
        print(f"Màu lông: {self.color}")
        print(f"Trọng lượng: {self.weight} kg")
class Bird(Animal):
    def __init__(self, name, age, color, weight, wingspan):
        super().__init__(name, age, color, weight)
        self.wingspan = wingspan
        self.is_flying = False