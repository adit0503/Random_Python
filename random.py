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
