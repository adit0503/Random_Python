def twoSum(nums,target):
    ans = []
    temp = {}
    l = len(nums)
    for i in range(l):
        temp[nums[i]] = i

    for i in range(l):
        t = target - nums[i]
        if t in temp.keys() and temp[t] != i:
            ans.append(nums[i])
            ans.append(nums[temp[t]])
            return ans
    return ans
##
import sys
sys.maxsize

a = [1,2,3,4]
print(a,*a)
a = [0 for i in range(10)]
a

##
import math
def isPrime(n):
    if n == 1:
        return False

    if n <= 3:
        return True

    if n%2==0 or n%3==0:
        return False

    i = 5
    while(i*i <= n):
        if n%i==0 or n%(i+2)==0:
            return False
        i += 6
    return True
n=184
root = n // 2
ans = []
while
    if n%i==0 and isPrime(i):
        ans.append(i)
print(ans)

##
n = 184
ans = []
while(n != 0):
    if n%2 == 0:
        n = n //2
        ans.append(2)
    if n%3 == 0:
        n = n // 3
        ans.append(3)
##
count = 1
def abc():
    global count #using global
    for i in (1,2,3):
        count += 1
abc()
print(count)

##
a = [[2,3],[1,2]]
tx = a[0].x

##
a = 'abc' "acd" 'yetd' #auto-concatination
a
b = 'abc' + "acd" + 'yetd'
b

##
a= [1,2,3,4,] #remember to add comma after every entry
b = [
        1,
        2,
        3,
        4,
    ]
a
b

##
a = [1,2,3,4,5,5,4,3,2,1,2,3,1,4,5,2,7,9]
b = set(a)
c = set()
for i in a:
    c.add(i)

b
c

##
a = set([1,2,3,4])
b = set([4,5,6,7])
a&b

##
def digits_list(n):
    digits = []
    while(n != 0):
        digits.append(n%10)
        n = n // 10
    return digits

def isHappy(n):
    temp = set()
    while(True):
        digits = digits_list(n)
        digits_sum = 0
        for i in digits:
            digits_sum += i*i
        if digits_sum == 1:
            return True

        if digits_sum  in temp:
            return False
        temp.add(digits_sum)
        n = digits_sum
        print(temp)
    return False
print(isHappy(2))

##
a = 'asdfgasdfg'
b = 'zxcvbzxcvb'
c = zip(a,b)

##
a = 1897
digits_used = [False for i in range(10)]
while(a!=0):
    digit = a%10
    if not digits_used[digit]:
        digits_used[digit] = True
    a = a // 10
ans = []
for i in range(10):
    if digits_used[i] == False:
        ans.append(i)
ans

##
a = [1,2,3,4,1,2,3,5,6,7]
b = [1,2,3,1,2,3,4]
set(a)&set(b)

##
s = 'fjbvourw'
s1 = sorted(s)
s
s1
s[:]
s1[:]
"".join(s1)

##
a = [5,4,3,2,1]
a.sort()
a
b = [5,4,3,2,1]
sorted(b)
b

##
s = 'nitina'
print(s == s[::-1])
temp = s[2:3]
temp
temp.upper()
temp

##
text1 = 'MZJAWXU' #7
text2 = 'XMJYAUZTR'

dp_row = [0 for _ in range(len(text2)+1)]
dp_row
dp = [dp_row for _ in range(len(text1)+1)]
dp

a = [0]*6
a

##
a = 'abc'
b = 'def'
ans = []
for a1 in a:
    for b1 in b:
        ans.append(a1+b1)
ans

##
s = ['a','b','d']
s
a = ''
for i in s:
    a += i
a
a[-1]
b='xywrrmu'
b = b[:-1]
b

##
n = '1234 5678'
n = n.split()
n1 = n[0]
n1

##
arr = [9,9,9]
n = ''
for a in arr:
    n += str(a)
new_n = int(n) + 1
ans = []
for a1 in str(new_n):
    ans.append(a1)
ans

##
a = 1000000007
a

##
arr = [0,1,2,3,4,5]
count = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                for m in range(6):
                    for n in range(6):
                        if i^j^k^l^m^n == 0:
                            count += 1
count
1000000007

##
def perfectSquare(n):
    arr = [i for i in range(50001)]
    res = n ** 0.5
    if res in arr:
        return True
    return False
perfectSquare(9)

arr = []

a=[1,2]
n,m = a
n
m

##
n = 100
num = 0
i = 1
while(num < n):
    for j in range(0, i):
        num = (1 << i) + (1 << j) ##all numbers with 2 bits set
        if (num <= n):
            print(num)
    i += 1

a = 100
b = a << 2
b
b = a << 3
b

##
def lengthC(s):
    i = 0
    while(s[i] == 'C'):
        i += 1
    return i

n = 1
for _ in range(n):
    st = "SSSSEEEECCCCEECCCCCCCCCSSSSEEECCCCSSSSSSSEEESSCCCCCCCSEESSSSCCCCCCSSEEEE"
    maxC = 0
    i = 0
    while(i < len(st)):
        if st[i] == "C":
            l = lengthC(st[i:])
            print(st[i:],l)
            if l > maxC:
                maxC = l
            i += l
        else:
            i += 1
    print(maxC)

##
#0 = left
s = 'abcde'
i = 1
s = s[i:] + s[:i]
s
#1 = right
t = 'abcde'
i = 4
t = t[-i:]+t[:-i]
t

##
s = 'abcd'
set(s)
