#Write Your Code Here
def reverse(n):
    
    s=[]
    n=str(n)
    for x in range(len(n)-1,-1,-1):
        s.append(n[x])
    return int(''.join(s))

n = int(input())
result= reverse(n)
print(result)