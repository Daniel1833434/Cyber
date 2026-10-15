# [2,4,6] מפני שלא עשו קופי אז שינוי בa משנה את Nums
#[9,4] כי כן עשו קופי
#15
#10
# 2.
def combine(a,b):
    return [x+y for x,y in zip(a,b) if x>0 and y>0]
#3.
def exactly_two(a,b,c):
    dict = {}
    ret = set()
    lst = [a,b,c]
    for team in lst:
        for name in team:
            dict[name] = dict.get(name,0)+1

    for name, times in dict.items():
        if times ==2:
            ret.add(name)
    return  ret

#4.
def group_students(students):
    dict = {}
    for name, clss in students.items():
        if clss not in dict:
            dict[clss] = []
        dict[clss].append(name)
    for lst in dict.values():
        lst.sort()
    return dict
#5.
def rank_products(products):
    lst=[]
    return sorted(products,key= lambda x:(-x[2],x[1],x[0]))
#6
def remove_for_palindrome(text):
    if text == text[::-1]:
        return -2
    for i in range(len(text)):
        currenttext= text[:i] + text[i+1:]
        if currenttext == currenttext[::-1]:
            return i
    return -1
#7
def calculate(*nums, **options):
    return sum(nums)*options.get("factor",1) + options.get("bonus",0)
#8
def load_grades(filename):
    dict ={}
    try:
        with open(filename,'r') as file:
            for line in file:
                try:
                    name,grade = line.split(',')
                    name = name.strip()
                    grade = grade.strip()
                    grade = int(grade)
                except:
                    continue

                if not(grade>=0 and grade<=100) or name == "":
                    continue
                dict[name] = grade
    except:
        pass
    return dict
#9

#10
def stone_piles(a, b):
    steps =0
    while a !=b:
        if a>b:
            a-=b
        else:
            b-=a
        steps+=1
    return a,steps
#התהליך חייב להתקיים כי בגלל שאתה כל פעם מוריד מספר אחד מהאחר זה ההפך מכפל לדוגמה 9 -3 -3-3 זה כמו 9 כפול שלוש ואם ממשיכים להוריד תמיד נגיע למספרים שווים
#אם המספר גדול מתחלקים באותו מספר ללא שארית אז יצא המספר ההוא ואם לא אז יצא 1

#11
class TravelCard:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def load(self,amount):
        self.balance+=amount
    def pay(self,fare):
        if self.balance>=fare:
            self.balance-=fare
            return  True
        return False

class DiscountCard(TravelCard):
    def __init__(self,owner,balance,discount):
        super().__init__(owner,balance)
        self.discount =discount
    def pay(self,fare):
        return super().pay(fare*(1-self.discount/100))
def charge_all(cards, fare):
    ret =[]
    for card in cards:
        result = card.pay(fare)
        if result:
            ret.append(card.owner)
    return ret

def next_number(n):
    sum =0
    while n>0:
        sum+= pow(n%10,2)
        n//=10
    return sum
def reaches_one(n):
    x=n
    nums =set()
    while x!= 1 and x not in nums:
        nums.add(x)
        x=next_number(x)
    if x==1:
        return True
    else:
        return False

def number_chain(n):
    lst=[]
    x = n
    nums = set()
    while x != 1 and x not in nums:
        lst.append(x)
        nums.add(x)
        x = next_number(x)
    lst.append(x)

    return lst
#כי כבר ניסינו להתחיל ממנו וחזרנו אליו אז כל פעם שנמשיך נחזור אליו שוב