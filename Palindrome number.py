def reverse(num):
    s = []
    num = str(num)
    for x in range(len(num)-1,-1,-1):
        s.append(num[x])
    return int(''.join(s)) 
num = int(input())
reversenum = reverse(num)
if reversenum == num:
    print('true')
else:
    print('false')  



