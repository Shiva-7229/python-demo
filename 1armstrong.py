"""number = 10
number1 = 500
for i in range(number, number1):
    num = len(str(i))
    sum = 0
    temp = i
    while temp>0:
        digit = int(temp% 10)
        sum += pow(digit, num)
        temp = temp/10
    if i == sum:
        print(sum)"""
    
"""def armstrong(a,b):
    for i in range(a, b+1):
        n = len(str(i))
        sum = 0
        temp = i
        while temp >0:
            digit = temp%10
            sum += pow(digit, n)
            temp = temp/10
    
i = armstrong(1,500)
if sum == i:
    print(sum)"""

"""n = 3716
sum = 0
a = len(str(n))
temp = n
while temp>0:
    digit = temp %10
    sum += pow(digit, a)
    temp = temp//10
if sum == n:
    print("armstrong")
else: 
    print("not armstrong")"""