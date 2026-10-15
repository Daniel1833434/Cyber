import math
from _pyrepl import commands
from os.path import split
from webbrowser import open_new


def passing_students(students):
    lstpassing = []
    for name,grade in students:
        if grade >=60:
            lstpassing.append((name,grade))
    return sorted(lstpassing, key= lambda x: x[1],reverse= True)

def sum_numbers(path):
    sum =0
    try:
        with open(path,"r") as file:
            for line in file:
                line = line.strip()
                try:
                    sum+= int(line)
                except:
                    pass
    except:
        return 0
    return sum

def longest_alternating(text):
    largest_Count = 0
    largest = ''
    current_Count = 0
    current = ''
    wanted = None

    for char in text:
        parity = int(char) % 2

        if parity == wanted:
            current_Count += 1
            current += char
        else:
            current = char
            current_Count = 1

        wanted = 1 - parity

        if current_Count > largest_Count:
            largest_Count = current_Count
            largest = current

    return largest

class PairFinder:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target

    def find_pair(self):
        for i,num in enumerate(self.nums[:-1]):
            for j in range(i+1,len(self.nums)):
                if num+self.nums[j] == self.target:
                    return (i,j)
        return (-1,-1)

def merge_ranges(ranges):
    ranges2= sorted(ranges)
    if not ranges2:
        return []
    newlst = [ranges2[0]]
    for start,end in ranges2[1:]:
        startnew,endnew = newlst[-1]
        if start <= endnew:
            newlst[-1] = (start,endnew)
            if end>endnew:
                newlst[-1] = (startnew, end)
            else:
                newlst[-1] = (startnew, endnew)
        else:
            newlst.append((start,end))
    return newlst

def shortest_section(nums, target):
    shortest_indexes =(-1,-1)
    shortest_count =-1
    for i in range(len(nums)):
        sum=0
        count = 0
        for j in range(i,len(nums)):
            sum+=nums[j]
            count+=1
            if sum >= target and (count<shortest_count or shortest_count==-1):
                shortest_count = count
                shortest_indexes = (i,j)

    return shortest_indexes

class Inventory:
    def __init__(self,items):
        self.items = items.copy()

    def change(self,name, amount):
        newamount = self.items.get(name,0)+amount
        if newamount>=0:
            self.items[name] = newamount
            return True
        else:
            return False

    def available(self,name):
        return self.items.get(name, 0)

def remove_to_increase(nums):
    goodindex = []

    # בדיקה של הרשימה לאחר הסרת כל אינדקס
    for i in range(len(nums)):
        good = True
        lastnum = None

        for j in range(len(nums)):
            if j == i:
                continue

            if lastnum is not None and nums[j] <= lastnum:
                good = False
                break

            lastnum = nums[j]

        if good:
            goodindex.append(i)

    # בדיקה נפרדת של הרשימה המקורית
    isgood = True
    for j in range(1, len(nums)):
        if nums[j] <= nums[j - 1]:
            isgood = False
            break

    if isgood:
        return -2
    elif len(goodindex) == 0:
        return -1
    else:
        return goodindex[0]

def build_route(flights,start):
    used = set()
    route = [start]
    if len(flights) ==0:
        return route

    while len(route) < len(flights)+1:
        found=False
        for i,item in enumerate(flights):
            startt= item[0]
            end = item[1]
            if route[-1] == startt and i not in used:
                route.append(end)
                used.add(i)
                found =True
                break
        if not found:
            return []

    return route

def avg_diff(lst,lst2):
    return sum([x-y for x,y in zip(lst,lst2)])/len(lst)

lst = [1,2,3,4]
#lst = list(map(lambda x:x+2,lst))
lst = [x+2 if x>0 else 0 for x in lst ]

class Robot:
    def __init__(self,name):
        self.name = name
        self.distance =0

    def move(self,steps):
        self.distance +=steps
        return steps

class BatteryRobot(Robot):
    def __init__(self,name,battery):
        super().__init__(name)
        self.battery = battery

    def move(self,steps):
        count =0
        while self.battery>=2 and count<steps:
            self.battery -=2
            self.distance+=1
            count+=1
        return count

class LimitedRobot(Robot):
    def __init__(self,name,limit):
        super().__init__(name)
        self.limit = limit

    def move(self,steps):
        if steps>=self.limit:
            self.distance+=self.limit
            return self.limit
        return super().move(steps)

def execute(robots, commands):
    lst= []
    for i,steps in commands:
        robot= robots[i]
        actual_steps = robot.move(steps)
        lst.append((robot.name,actual_steps,robot.distance))
    return lst

robots = [
    Robot("A"),
    BatteryRobot("B", 5),
    LimitedRobot("C", 3)
]

def merge(lst,lst2):
    return [x+y for x,y in zip(lst,lst2)]
def printlsts(lst,lst2):
    for x,y in zip(lst,lst2):
        print(x,y)

def removenum(lst,num):
    lst = [x for x in lst if x!=num]
    print(lst)

def removedict(dict,lst):
    dict = {x:y for x,y in dict.items() if x not in lst}
    print(dict)

def change(dict,i):
    dict["location"] = dict.pop("city")
    print(dict)

def notempty(lst):
    return [x for x in lst if len(x)>0]

def same(set1,set2):
    return set1.intersection(set2)

def maximusdexamos(lst,k):
    return sorted(lst)[-1 *k]

def rishoni(num):
    for i in range(2,num):
        rishon = True
        for j in range(2,i):
            if i%j ==0:
                rishon = False
                break
        if rishon:
            print(i)


def light(n):
    lst =[]
    for i in range (n):
        lst.append(False)

    for i in range (1,n+1):
        for j in range(1,n+1):
            if j%i==0:
                lst[j-1] = not lst[j-1]

    for i in range(n):
        if lst[i]:
            print(i+1)

def soliders(n):
    remaining =[]
    for num in range(1,n+1):
        remaining.append(num)

    while len(remaining)>1:
        for i in range(len(remaining)-len(remaining)//2):
            remaining.pop((i+1)%(len(remaining)))
    return remaining[0]

def my_int(str):
    num =0
    for char in str:
        num = num*10 +ord(char)-ord('0')
    return num

def football(lst):
    return max(lst,key= lambda x: x["scored"] - x["conceded"])["name"]

def substring_logest(str):
    zogiexpect =None
    biggest=''
    current=''
    count=0
    countbiggest=0
    for char in str:
        num = int(char)
        if zogiexpect == None or zogiexpect == num%2:
            count+=1
            current +=char
            if count>countbiggest:
                biggest=current
                countbiggest = count
        else:
            count=1
            current=char

        zogiexpect = 1 - num % 2
    return biggest

class FindPair:
    def __init__(self,lst,num):
        self.lst = lst
        self.num = num

    def find_loc(self):
        for i in range(len(self.lst)-1):
            for j in range(i+1,len(self.lst)):
                if self.lst[i]+self.lst[j] == self.num:
                    return (i,j)
        return (-1,-1)

class Solution:
    def __init__(self,lst):
        self.lst =lst
    def max_product(self):
        summ=1
        biggestsum =1
        smallestsum =1
        answer = self.lst[0]
        for num in self.lst:
            a= num
            b = num *biggestsum
            c = num *smallestsum
            biggestsum = max(a,b,c)
            smallestsum = min(a,b,c)

            answer = max(answer,biggestsum)

        return answer

def compress(text):
    ret =''
    lastchar =text[0]
    count =1
    for char in text[1:]:
        if lastchar== char:
            count += 1
        else:
            ret += lastchar + str(count)
            lastchar = char
            count =1

    ret+= lastchar + str(count)
    return ret

def balance_index(nums):
    for i in range(len(nums)):
        before =0
        after = 0
        for j,num in enumerate(nums):
            if j>i:
                after+=num
            elif i>j:
                before +=num
        if before == after:
            return i
    return -1

def finish_order(tasks):
    retlst =[]
    while len(tasks)>0:
        tasks[0] = (tasks[0][0],tasks[0][1]-1)
        item = tasks[0]
        if tasks[0][1]<=0:
            retlst.append(tasks[0][0])
            tasks.pop(0)
        else:
            tasks.pop(0)
            tasks.append(item)
    return retlst

def max_circle_sum(nums,k):
    sums=[]
    for i,num in enumerate(nums):
        sum =0
        for j in range(i,i+k):
            sum+= nums[j%len(nums)]
        sums.append(sum)
    return max(sums)

def reduce_numbers(nums):
    while len(nums)>1:
        nums = sorted(nums)
        num1 = nums.pop()
        num2 = nums.pop()
        nums.append(abs(num1 - num2))

    return nums[0]

def min_flips(coins):
    if sum(coins) == 0:
        return 0
    count =0
    for i in range(0,len(coins)-1):
        if coins[i] ==1:
            coins[i] = 0
            coins[i + 1] = 1 - coins[i + 1]
            count += 1
        if sum(coins) == 0:
            return count
    return -1

def find_start(energy,cost):
    stuck=-1
    for i,get in enumerate(energy):
        if get>=cost[i] and i >stuck:
            money = 0
            index=i
            for j in range(i,i+len(energy)):
                realindex = j%len(cost)
                money+= energy[realindex]
                if money<cost[realindex]:
                    index = -1
                    stuck = j
                    break
                else:
                    money-=cost[realindex]
            if index != -1:
               return i
    return -1

def collapse(text):
    exit =True
    newtxt =text
    while exit:
        exit =False
        text = newtxt
        newtxt =''
        lastchar = None
        count=0
        for char in text:
            if char == lastchar or lastchar==None:
                count+=1
            else:
                if count==1:
                    newtxt+=lastchar
                else:
                    exit = True
                count=1
            lastchar = char
        if count < 2:
            newtxt += lastchar
        else:
            exit = True

    return newtxt

def longest_unique(text):
    longest= ''
    longestcount=0
    for i,char in enumerate(text):
        count = 0
        current = []
        for char2 in text[i:]:
            if char2 not in current:
                count+=1
                current.append(char2)
                if count>longestcount:
                    longestcount = count
                    longest = "".join(current)
            else:
                break
    return longest

def can_rearrange(text):
    dict = {}
    count=0
    for char in text:
        dict[char] = dict.get(char,0)+1
    for char2,times in dict.items():
        if times %2==0:
            count+=1
            if count>1:
                return  False
    return True
#דף 80 שאלות
#ex 20
sentence ="the secure shell protocol is used"
abbr = ".".join(x[0].upper() for x in sentence.split() if len(x)>3)

#ex29
response_ms = {"web1": [120, 340, 95], "web2": [80, 610, 150], "db1": [45, 50, 52], "cache": [5, 7, 3]}
stable = {name:round(sum(values)/len(values),1) for name,values in response_ms.items() if sorted(values)[-1] <500}

#ex30
words = ["TCP", "udp", "tcp", "IP", "ip", "Tcp", "dns"]
words = [word.lower() for word in words]
dictt = {word : words.count(word) for word in words if words.count(word)>1}

#ex35
def ex35(dict1, dict2):
    merge = dict1 | dict2
    return {key : max(dict1[key],dict2[key]) if key in dict1 and key in dict2 else value for key,value in merge.items() if (key in dict1 and key in dict2) or value %2 ==0 }

#ex 38
def long_lines_info(path,n):
    summ =0
    longestLength =0
    longest = ''
    with open(path,'r') as file:
        for line in file:
            line = line.strip()
            summ+= 1 if len(line) >n else 0
            if len(line)> longestLength:
                longest = line
                longestLength = len(line)
        return (summ,longest)
#ex 39
def stock_value(path):
    total =0
    largestprice =-1
    largest = ''
    with open(path,'r') as file:
        file.readline()
        for line in file:
            line = line.strip()
            name,qty,price = line.split(',')
            qty = float(qty)
            price = float(price)
            total += qty *price
            if price>largestprice:
                largestprice=price
                largest = name

    return (total,largest)

#ex44
def common_words(t1,t2,n):
    lst1 = {word.lower() for word in t1.split() if len(word)>=n}
    lst2 = {word.lower() for word in t2.split() if len(word) >= n}
    return lst1 & lst2

#ex 45
def only_first_with_digit(t1,t2):
    set1 = {word.lower() for word in t1.split() if any(ch.isdigit() for ch in word)}
    set2 = {word.lower() for word in t2.split() if any(ch.isdigit() for ch in word) }
    return set1 - set2
#ex 48
def chunk_sums(nums,k):
    return [sum(nums[i:i+k]) for i in range(0,len(nums),k)]

#ex 49
def reverse_chunks(s,k):
    return "-".join([s[i:i+k][::-1] for i in range(0,len(s),k)])

#ex50
def single_chars(s):
    return "".join([k for k in s if s.count(k) ==1])

#ex 54
class BankAccount:
    def __init__(self,owner,balance =0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return True
        return False

#ex 55
class Packet:
    def __init__(self,src_ip,dst_ip,payload):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.payload = payload
    def get_size(self):
        return len(self.payload)
    def is_local(self):
        return self.src_ip.startswith("192.168.") and self.dst_ip.startswith("192.168.")

#ex 59
users = ["alice", "bob", "charlie"]
scores = [85, 92, 78]
result = [name for name,value in sorted(zip(users,scores),key= lambda x:x[1],reverse=True)]

#ex 60
words = ["ip", "firewall", "net", "protocol"]
max_item = max([item for item in enumerate(words)],key = lambda x:len(x[1]))

#ex 64
ips = ["192.168.1.50", "10.0.0.1", "192.168.0.100", "172.16.0.5"]
result = [int(ip.split(".")[-1]) for ip in ips if ip.startswith("192.168.")]

#ex 65
text = "we love python code"
result = [word.upper()[::-1] for word in text.split() if len(word) >2]

#ex 68
def filter_errors(path,errors):
    write =[]
    with open(path,'r') as file , open(errors,'w') as output:
        for line in file:
            ip,code = line.split()
            if code == "404" or code == "500" : output.write(ip + "\n")

#ex 69
def copy_without_empty(src_file,dst_file):
    with open(src_file,'r') as file, open(dst_file,'w') as file2:
        for line in file:
            if line.strip() != "" : file2.write(line)
#ex 70
def file_stats(path):
    lines =0
    words = 0
    chars = 0
    with open(path,'r') as file:
        for line in file:
            lines+=1
            words += len(line.split())
            chars += len(line)
    return (lines,words,chars)
#ex 71
def is_happy_number(n):
    hasbeen = set()
    while n != 1 and n not in hasbeen:
        hasbeen.add(n)
        summ=0
        while n>0:
            summ+= (n%10) **2
            n//=10
        n=summ
    return n ==1

#ex72
def max_sub_sum(nums):
    biggest =nums[0]
    for i in range(len(nums)):
        current = 0
        for j in range(i,len(nums)):
            current += nums[j]
            if current>biggest:
                biggest = current
    return biggest

def max_sub_sum_2(nums):
    biggest =nums[0]
    biggest_before = nums[0]
    for num in nums[1:]:
        biggest += num
        biggest_before = max(num,biggest_before,biggest)
        biggest = max(num,biggest)

    return biggest_before

#ex 73
def find_missing_and_duplicate(nums):
    missing =-1
    duplicate =-1
    for i in range(1,len(nums)+1):
        if i not in nums:
            missing = i
        if nums.count(i) >1:
            duplicate = i
    return (duplicate,missing)

#ex 74
def longest_consecutive_ones(binary_str):
    longest =0
    current =0
    for j in range(len(binary_str)):
        if binary_str[j] == '1':
            current += 1
        else:
            current = 0
        if current>longest:
            longest = current
    return longest

#ex 75
def is_valid_parentheses(s):
    new_s= "".join([x for x in s if x in "(){}[]"])
    stack = []
    for i in range(len(new_s)):
        if new_s[i] =="(" or new_s[i] == "{" or new_s[i] =="[":
            stack.append(new_s[i])
        elif len(stack) ==0 or (stack[-1] + new_s[i] != "()" and stack[-1] + new_s[i] != "{}" and stack[-1] + new_s[i] != "[]") :
            return False
        else:
            stack.pop()
    return len(stack) ==0

#ex 76
text = "Hello, World! Python 3.10 #Cyber2026"
text = {x for x in text if not x.isalnum() and not x ==" "}

#ex 78
def unique_intersection(*sets):
    mergeee = set()
    for sett in sets:
        mergeee = mergeee | sett

    ret = set()
    for num in mergeee:
        count =0
        for sett in sets:
            if num in sett:
                count+=1
        if count>=2:
            ret.add(num)

    return ret
#ex 79
def is_pangram(sentence):
    abc = set("abcdefghijklmnopqrstuvwxyz")
    return set(sentence.lower()) >= abc
##################################################
def best_student(path):
    bestname =""
    bestavg=-1
    with open(path,"r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            name,*grades = line.split(',')
            grades = [float(grade) for grade in grades]
            avg = sum(grades) / len(grades)
            if avg>bestavg:
                bestavg = avg
                bestname = name
    return (bestname,round(bestavg,2))

def group_words(words):
    starting = {word[0].lower() for word in words if len(word) >0}
    ret = {char : set(word.lower() for word in words if  len(word) >0 and word[0].lower() == char ) for char in starting}
    return {char: sorted(group) for char,group in ret.items()}

class Product:
    def __init__(self,name,price):
        self.name= name
        self.price = price
    def final_price(self):
        return self.price
    def __str__(self):
        return f"{self.name} : {round(self.final_price(),2)}"

class DiscountProduct(Product):
    def __init__(self,name,price,discount):
        super().__init__(name,price)
        self.discount = discount
    def final_price(self):
        return self.price * ((100-self.discount)/100)

def longest_increasing_run(nums):
    if len(nums) ==0:
        return []
    current =[nums[0]]
    lastnum = nums[0]
    longestlst = [nums[0]]
    for num in nums[1:]:
        if num > lastnum:
            current.append(num)
            if len(current)>len(longestlst):
                longestlst = current
        else:
            current =[num]
        lastnum = num
    return longestlst

def biggest_rezef(nums):
    if len(nums) ==0:
        return -1
    current =nums[0]
    biggest = nums[0]
    for num in nums[1:]:
        current = max(current+num,num)
        biggest = max(current,biggest)
    return biggest
################ chat exam
#1 א
def clean_words(text):
    text = ([word.lower().strip('.,!?') for word in text.split()])
    return [word for word in text if word !=" "]
#1 ב
def common_long_words(t1,t2,n):
    return {word for word in set(clean_words(t1)) & set(clean_words(t2)) if len(word)>=n}
#2 א
grades = {
    "Dana": [80, 100],
    "Ron": [60, 70],
    "Noa": [],
    "Amit": [90, 90]
}
averages = {name:round(sum(lst) / len(lst),1) for name,lst in grades.items() if len(lst)>0}
 # 2 ב
def above_threshold(averages,threshold):
    return sorted({name : avg for name,avg in averages.items() if avg>=threshold})
# 2 ג
def merge_scores(d1,d2):
    return {name:max(d1.get(name,0),d2.get(name,0))for name in d1 | d2}
# 3 א
def total_quantities(path):
    ret = {}
    with open(path,'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                continue
            name,value = line.split(',')
            value = int(value)
            ret[name] = ret.get(name,0) + value
    return ret
# 3 ב
def write_large_orders(src,dst,minimum):
    quant = sorted(total_quantities(src).items())
    with open(dst,'w') as file:
        for name,value in quant:
            if value >= minimum:
                file.write(f"{name},{value}\n")
#4 א
class Storage:
    def __init__(self,capacity):
        self.capacity= capacity
        self.used =0
    def add(self,amount):
        if self.used + amount <=self.capacity:
            self.used += amount
            return True
        return False
    def remaining(self):
        return self.capacity-self.used
class LimitedStorage(Storage):
    def __init__(self,capacity,max_add):
        super().__init__(capacity)
        self.max_add = max_add
    def add(self,amount):
        if amount<=self.max_add:
             return super().add(amount)
        return False
#5 א
def pairs_with_sum(nums,target):
    return {(min(nums[a],b),max(nums[a],b)) for a in range(len(nums)) for b in nums[a+1:] if nums[a]+b == target}
#5 ב
def has_pair(nums,target):
    seen = set()
    ret = False
    for num in nums:
        if target-num in seen:
            return True
        seen.add(num)
    return ret
# 6 א
def longest_alternating_run(nums):
    ret =[]
    current =[]
    wantzogi = None
    for num in nums:
        if wantzogi == None or (num%2 == 0) == wantzogi:
            current.append(num)
            if len(current)> len(ret):
                ret = current
        else:
            current = [num]
        wantzogi = not (num%2==0)
    return ret
# 6 ב
def count_alternating_runs(nums):
    count =0
    wantzogi = None
    for num in nums:
        if wantzogi != None and (num % 2 == 0) != wantzogi:
            count +=1

        wantzogi = not (num % 2 == 0)
    count+=1 if len(nums)>0 else 0
    return count

#################
# אתגר
def min_jumps(nums):
    maxx = 1
    jumps =0
    index =0
    while maxx <len(nums):
        jumps+=1
        for i in range(index,maxx):
            if i+nums[i] >maxx:
                maxx = i+nums[i]
                index =i
    return jumps

def max_product(lst):
    lowest = 1
    biggest = 1
    realbiggest =1
    for num in lst:
        biggest_holder = biggest *num
        lowest_holder = lowest *num
        biggest = max(biggest_holder,lowest_holder,num)
        lowest = min(lowest_holder, biggest_holder, num)
        realbiggest = max(realbiggest,biggest)
    return realbiggest

def follow_chain(links,start):
    link = start
    lst = []
    while link not in lst and link in links:
        lst.append(link)
        link = links[link]
    if link in lst:
        return None
    else:
        lst.append(link)
        return lst

def expand(text):
    digits = [(num, i) for i,num in enumerate(text) if num.isalpha()]
    ret = ""
    for x in range(len(digits)):
        char,i = digits[x]
        times = int(text[i+1:digits[x+1][1] if len(digits)-1 != x else len(text)])
        ret += char *times
    return ret

def merge_ranges(ranges):
    merged = True
    if len(ranges) == 0:
        return ranges
    while merged:
        merged = False
        newlst = ranges.copy()
        for i in range(len(ranges)):
            start,end = ranges[i]
            for j in range(i+1,len(ranges)):
                start2,end2 = ranges[j]
                if end>= start2 and start<= end2:
                    newlst = [ranges[x] for x in range(len(ranges)) if x not in [i,j]]
                    newlst.append((min(start,start2),max(end,end2)))
                    merged =True
                    break
        ranges = newlst.copy()
    return ranges

class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs =[]
    def add_song(self,title,seconds):
        names = [title for title,seconds in self.songs]
        if title not in names:
            self.songs.append((title,seconds))
            return True
        return False
    def total_time(self):
        return sum([seconds for title,seconds in self.songs])
    def long_songs(self,minimum):
        return sorted([name for name,seconds in self.songs if seconds>=minimum])

############################################
# 1
 #9,5,9
 #2
#pypyyyy,1,2,2
#3
#[[1,2,9],[3,4]] , [[1,2,9] [0]]
#שמעתיקים רשימה של רשימות הרשימות הפנימיות הן מפנות לאותו מקום
#4
sentence = "the secure shell protocol is used"
print(".".join(word[0].upper() for word in sentence.split() if len(word) > 3))
#5
#"864", True ,"789", "975"
#6
response_ms = {
    "web1": [120, 340, 95],
    "web2": [80, 610, 150],
    "db1": [45, 50, 52],
    "cache": [5, 7, 3]
}
stable = {server:round(sum(lst) / len(lst),1) for server,lst in response_ms.items() if all(i<=500 for i in lst)}
#7
def merge_max(d1,d2):
    return {key:max(d1.get(key,-float('inf')),d2.get(key,-float('inf'))) for key in d1.keys() | d2.keys() if key in d1.keys &d2.keys() or max(d1.get(key,-float('inf')),d2.get(key,-float('inf'))) %2==0 }
#8
def long_lines_info(path,n):
    longest =''
    count =0
    with open(path,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            if len(line) >n:
                count+=1
            if len(line) > len(longest):
                longest = line
    return (count,longest)
#9
#[1,2,3,4,5] , [3,4]
#[1,2] , [5] , [1,2,5]
#10
def reverse_chunks(s,k):
    return "-".join(s[i:i+k][::-1] for i in range(0,len(s),k))
#11
class BankAccount:
    def __init__(self,owner,balance =0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if self.balance>= amount:
            self.balance -= amount
            return True
        return False
#12
users = ["alice","bob","charlie"]
scores = [85,92,78]
merged = [name for name,grade in sorted(zip(users,scores),key = lambda x:x[1],reverse= True)]
#13
ips = [
    "192.168.1.50",
    "10.0.0.1",
    "192.168.0.100",
    "172.16.0.5"
]
newlst = [int(ip.split('.')[-1]) for ip in ips if ip.startswith("192.168.")]
#14
def filter_errors(src, dst):
    with open(src,'r') as file, open(dst,'w') as file2:
        for line in file:
            line = line.strip()
            ip,code = line.split()
            if code in ('404','500'):
                file2.write(ip +"\n")

#15
def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        if char in ")}]":
            if not stack or stack[-1] +char not in ["()","{}","[]"]:
                return False
            else:
                stack.pop()
    return len(stack) ==0
#16
def unique_intersection(*sets):
    ret = set()
    if len(sets)<2:
        return ret
    for sett in sets:
        ret = ret | sett
    realret = set()
    for num in ret:
        count = 0
        for sett in sets:
            if num in sett:
                count+=1
        if not count<2:
            realret.add(num)
    return realret
######################################################
#8
def kth_largest(lst, k):
    return sorted(lst,reverse= True)[k-1]
#10
n=10
light= [False for x in range(n)]
for i in range(1,n+1):
    for j in range(len(light)):
        if (j+1)%i == 0:
            light[j] = not light[j]
print(list(i+1 for i in range(len(light)) if light[i]))
#ב - כל המספרים שיש להם משהו בריבוע דלוקים
#12
def my_int(text):
    sign =1
    if text.startswith('-'):
        sign = -1
        text = text[1:]
    num =0
    for char in text:
        num = num*10 +ord(char)-ord('0')
    return sign*num
print(my_int("-56"))
#15
class FindNum:
    def __init__(self,lst,num):
        self.lst = lst
        self.num = num
    def find_loc(self):
        for i in range(len(self.lst)):
            for j in range(i+1,len(self.lst)):
                if self.lst[i] + self.lst[j] == self.num:
                    return (i,j)
        return (-1,-1)
#16
class Solution:
    def __init__(self,lst):
        self.lst = lst
    def max_product(self):
        biggest = self.lst[0]
        for i in range(len(self.lst)):
            count =1
            for j in range(i,len(self.lst)):
                count *= self.lst[j]
                biggest = max(biggest,count)
        return biggest

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [x+y for x,y in zip(list1,list2)]

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for num1,num2 in zip(list1,list2[::-1]):
    #print(num1, num2)
    pass

list1 = [5, 20, 15, 20, 25, 50, 20]
list1 = [x for x in list1 if x !=20]

dicat = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys_to_remove = ["name", "salary"]
dicat = {key:value for key,value in dicat.items() if key not in keys_to_remove}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
#print(set1 & set2)
lst = [7,10,4,3,20,15]
#print(sorted(lst)[-3])
n =6  #int(input())
for num in range(2,n):
    rishoni = True
    for num2 in range(2,num//2):
        if num %num2 ==0:
            rishoni=False
            break
    if rishoni:
        #print(num)
        pass

bulbs = [False for i in range(100)]
for i in range(1,101):
    for j in range(100):
        if (j+1)%i == 0:
            bulbs[j] = not bulbs[j]
#print([i+1 for i in range(100) if bulbs[i]==True ])
n = 2
soliders = [i for i in range(1,n+1)]
while len(soliders) >1:
    soliders.append(soliders[0])
    soliders.pop(0)
    soliders.pop(0)
#print(soliders[0])

c =[
    { "name": "Manchester United",
"wins": 30,
"loss": 3,
"draws": 5,
"scored": 88,
"conceded": 20,
},
    {"name": "Arsenal",
"wins": 24,
"loss": 6,
"draws": 8,
"scored": 98,
"conceded": 29,
}]

newdict = sorted({items['name']:items['scored']-items['conceded'] for items in c }.items(),key = lambda x:x[1])[-1][0]

def longest_substring(text):
    wantzogi = None
    count=0
    longest =0
    current = ''
    longesttxt = ''
    for char in text:
        num = int(char)
        if wantzogi == None or (num%2==0) == wantzogi:
            count +=1
            current += char
            if count>longest:
                longest= count
                longesttxt = current
        else:
            count =1
            current = char
            if count > longest:
                longest = count
                longesttxt = current
        wantzogi = not (num %2==0)
    return longesttxt

def max_product(lst):
     biggest =lst[0]
     current = 1
     for i in range(len(lst)):
         for num2 in lst[i:]:
             current *=num2
             if current>biggest:
                biggest = current
     return biggest
Lst = [6, 3, -10, 0, 2]

def first_unique(text):
    for char in text:
        if text.count(char) == 1:
            return char
    return None


response_ms = {"web1": [120, 340, 95], "web2": [80, 610, 150], "db1": [45, 50, 52], "cache": [5, 7, 3]}
stable = {key:round(sum(lst)/len(lst),1) for key,lst in response_ms.items() if all(x<500 for x in lst)}

words = ["TCP", "udp", "tcp", "IP", "ip", "Tcp", "dns"]
words = [word.lower() for word in words]
counts = {word : words.count(word) for word in set(words) if words.count(word)>1}

a = {'x': 1, 'y': 2}
b = {'y': 5, 'z': 3}
c = {'y': 8, 'h': 3}

t1 = "Firewall rules block the Port"
t2 = "the port and the FIREWALL are open"
ret = {word for word in set(t1.lower().split()) & set(t2.lower().split()) if len(word)>=4}

t1 = "Room B12 and lab 7A near gate3"
t2 = "lab 7a is closed"
ret = {word for word in set(t1.lower().split()) - set(t2.lower().split()) if any(x.isdigit() for x in word)}


k=3
lst = [4,1,7,2,9,3,5]
ret = [sum(lst[i:i+k]) for i in range(0,len(lst),k)]

users = ["alice", "bob", "charlie"]
scores = [85, 92, 78]
ret = [x for x,grade in sorted(zip(users,scores),key = lambda x:x[1] ,reverse=True)]

words = ["ip", "firewall", "net", "protocol"]
ret = max([(i,x) for i,x in enumerate(words)],key = lambda x:len(x[1]))

ips = ["192.168.1.50", "10.0.0.1", "192.168.0.100", "172.16.0.5"]
result = [int(x.split('.')[-1]) for x in ips if x.startswith('192.168.')]

text = "we love python code"
result = [word.upper()[::-1] for word in text.split() if len(word)>2]

def filter_errors(path,path2):
    with open(path,"r") as file, open(path2,'w') as file2:
        for line in file:
            if len(line) <0:
                continue
            ip,code = line.split()
            if code in ['404','500']:
                file2.write(ip +'\n')

def copy_without_empty(path,path2):
    with open(path,"r") as file, open(path2,'w') as file2:
        for line in file:
            if line.strip():
                file2.write(line)


def is_happy_number(n):
    seen =set()
    while n!= 1 and n not in seen:
        total = 0
        while n>0:
            total += (n%10) ** 2
            n//=10
        n = total
        seen.add(n)
    return n ==1

def max_sub_sum(nums):
    biggest = nums[0]
    for i in range(len(nums)):
        current  = 0
        for j in range(i,len(nums)):
            current+= nums[j]
            biggest = max(current,biggest)
    return biggest

def find_missing_and_duplicate(nums):
    duplicate = -1
    missing = -1
    for i in range(1,len(nums)+1):
        if nums.count(i) ==0:
            missing = i
        elif nums.count(i) ==2:
            duplicate = i
    return (duplicate,missing)

def longest_consecutive_ones(binary_str):
    longest = 0
    current =0
    for char in binary_str:
        if char == '1':
            current+=1
            longest = max(longest,current)
        else:
            current = 0
    return longest

def is_valid_parentheses(s):
    stackk = []
    for char in s:
        if char in '({[':
            stackk.append(char)
        if char in '}])':
            if stackk[-1] + char in ["()","{}","[]"]:
                stackk.pop()
            else:
                return False
    return len(stackk) ==0

text = "Hello, World! Python 3.10 #Cyber2026"
ret = {x for x in text if all(t>=0 for t in range(0,2))}

s1 = {x for x in range(10) if x % 2 == 0}
s2 = {x for x in range(10) if x % 3 == 0}

pairs = [(1, 2), (2, 1), (3, 0), (0, 3), (1, 2)]
unique_pairs = {tuple(sorted(p)) for p in pairs}

words = ["ip", "firewall", "net", "protocol"]
tup = max(enumerate(words),key = lambda x:len(x[1]))

grades = {
    "Dana": [70, 90, 80],
    "Ron": [55, 60],
    "Noa": [],
    "Amit": [100, 80, 60]
}
result = {name:(round(sum(grades) / len(grades),1),max(grades) ) for name,grades in grades.items() if len(grades) >0 and all(grade>=60 for grade in grades
                                                                                                                             )}
words = ["TCP", "udp", "tcp", "IP", "ip", "Tcp", "dns"]
words = [word.lower() for word in words]
counts = {word:words.count(word) for word in set(words) if words.count(word)>1}

class Packet:
    def __init__(self,src_ip,dst_ip,payload):
        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.payload = payload
    def get_size(self):
        return len(self.payload)
    def is_local(self):
        return all(x.startswith('192.168.') for x in [self.src_ip,self.dst_ip])

def is_pangram(sentence):
    abc = "abcdefghijklmnopqrstuvwxyz"
    return set(sentence.lower()) >= set(abc)

def student_averages(path):
    dicat = {}
    with open(path,'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name,grade = line.split(",")
            grade = int(grade)
            dicat.setdefault(name,[]).append(grade)

    return {name:round(sum(grades)/len(grades),1) for name,grades in dicat.items()}
dicat = student_averages('test.txt')
lst = [name for name,avg in sorted(dicat.items(),key = lambda x:(-x[1],x[0])) if avg>=70]

class Account:
    def __init__(self,owner,balance =0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            return True
        return False

class FeeAccount(Account):
    def __init__(self,owner,balance,fee):
        super().__init__(owner,balance)
        self.fee =fee
    def withdraw(self,amount):
        return super().withdraw(amount+self.fee)

a = FeeAccount("Dana", 100, 5)

def common_chunks(s1,s2,k):
    chunks1 = [s1[i:i+k].lower() for i in range(0,len(s1)-k+1,k)]
    chunks2 = [s2[i:i + k].lower() for i in range(0, len(s2)-k+1, k)]
    return sorted(set(chunks1) & set(chunks2))
print(common_chunks("abc", "xyz", 2))