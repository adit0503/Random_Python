##
def isSubstring(s1,s2):
    return False if s1.find(s2) == -1 else True

def rotateString(s1,s2):
    l = len(s1)
    if l == len(s2) and l > 0:
        temp = s1+s1
        return isSubstring(temp,s2)
    return False

s1 = 'waterbottle'
s2 = 'erbottlewat'
rotateString(s1,s2)

##
def stringCompresion(s):
    i = 0
    ans = ''
    while(i < len(s)):
        count = 0
        c = s[i]
        while(c == s[i]):
            i += 1
            count += 1
            if i == len(s):
                break
        ans += c
        if count != 1:
            ans += str(count)
    return ans if len(ans) <= len(s) else s

s = 'abbcccdddd'
stringCompresion(s)

##
def oneAway(s1,s2):
    if s1 == s2:
        return True

    if abs(len(s1)-len(s2)) == 1:
        (long,short) = (s1,s2) if len(s1)>len(s2) else (s2,s1)
        short_set = set(s2)
        for s in s2:
            if s not in s1:
                return False
        return True
    elif len(s1) == len(s2):
        count = 0
        for x,y in zip(s1,s2):
            if x != y:
                count += 1
        if count == 1:
            return True
    return False

s1 = 'pale'
s2 = 'pale'
print(oneAway(s1,s2))
