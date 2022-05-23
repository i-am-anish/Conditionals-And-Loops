## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n = int(input())
sumOfEven = int(0)
sumOfOdd = int(0)
rem = int(0)
while(n>0):
    rem = n%10
    if rem%2==0:
        sumOfEven=sumOfEven+rem
    else:
        sumOfOdd = sumOfOdd+rem
    n = n//10     
print(sumOfEven,sumOfOdd)