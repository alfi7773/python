# class Cat:
#     name = None
#     age = None
#     isHappy = None
    
#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
        
#     def get_data(self):
#         print(self.name, "age: ", self.age, "is happy: ", self.isHappy)
        
    
# cat1 = Cat("Musi", 2, True)
    
# cat1 = Cat()
# cat1.set_data("Musi", 2, True)
# cat1.get_data()

# cat1.name = "Musi"
# cat1.age = 2
# print(f"name: {cat1.name}, age: {cat1.age}")




# class Dog:
#     name = None
#     color = None
    
#     def set_data(self, name, color):
#         self.name = name
#         self.color = color
        
#     def get_data(self):
#         print(self.name, "color: ", self.color)
        
# dog = Dog()

# dog.set_data("Bursik", "balck")
# dog.get_data()


a = int(input("First number: "))
b = int(input("Second number: "))
operator = input("Operator: ")

    
    
if operator == "+" :
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a//b)
else :
    print("Please write correct operator")
    
    
        

    
    
