# def add(*args):

#     num = 0
#     for n in args:
#         num += n
#     return(num)
 
# print(add(2, 4, 6 ,8))
 
def add(*args):
    print(type(args))
 
add(1, 2, 3)


# def calculate(n, **kwargs):

#     print(kwargs)
#     # for key, value in kwargs.items():
#         # print(key)
#         # print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)

# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kw):
#         # Force the user to specify make and model
#         # self.make = kw["make"]
#         # self.model = kw["model"]

#         # Allow the arguments to be optional
#         self.make = kw.get("make")
#         self.model = kw.get("model")
        

# my_car = Car(make="Nissan")

# # Model will be 'none'
# print(my_car.model)