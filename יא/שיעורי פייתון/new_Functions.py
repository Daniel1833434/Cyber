# list =['nig']
# list2 =['ga']
# list3 =[]
# for i,j in zip(list, list2):
#     list3.append(i+j)
# print(list3)

# list1 = ['nig', 'ga']
# def printPlace(list1):
#     for i, j in enumerate(list1):
#         print(i, j)
# printPlace(list1)

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total
# print(add(1, 2, 3, 4, 5))

# def print_values(**kwargs):
#     print(kwargs)
# print(print_values(a=1, b=2, c=3, d=4, e=5))
# x = lambda a,b :a+b
# print(x(5,6))
# numbers = [1, 2, 3, 4, 5]
# dict = {'key': 'value', 'key2': 'value2'}
# def double(x):
#     return x * 2
# numbers = list(map(lambda x: x * 2, dict.values()))
# numbers2 = list(map(double, numbers))
# print(numbers2)

# lst = [1, 2, 3, 4, 5]
# newlst = [x+2 for x in lst if x>2]
# print(newlst)

# lst2 = [1, 2, 3, 4, 5]
# func = lambda a,lst2: [x for x in lst2 if x!=a]
# print(func(3, lst2))

# a=10
# b=20
# x=a if b==20 else b
# print(x)

# l1=[9, 2, 3,4,5]
# l2=[6, 7, 8,9,10]
# l3=[max(i[0],i[1]) for i in zip(l1,l2)]
# print(l3)

# print(sum([i**2 for i in range(5)]))

# x= (i**2 for i in range(5)) // גנרטור זה פחות מקום
# print(list(x))

# def my_gen():
#     for i in range(5):
#         yield i**2

# for nig in my_gen():   
#     print(nig)

# f = open('text.txt', 'rt')
# for line in f:
#     print(line.strip())
# f.close()

# with open('text.txt', 'rt') as file:#זה יותר טוב כי זה סוגר את הקובץ לבד
#     for line in file:
#         print(line.strip())

class Nigga:
    def __init__(self,name):
        self.name = name
        self.color = 'black'

    def print_info(self):
        print(f"Name: {self.name}, Color: {self.color}")

class IsraliNigga(Nigga):
    def __init__(self, name):
        super().__init__(name)
        self.color = 'brown'

nig2 = IsraliNigga("david")
nig2.print_info()

nig1 = Nigga("abram")
nig1.print_info()
