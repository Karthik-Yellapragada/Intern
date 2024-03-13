def HappyNumber(n):
    sum=0
    while n>0:
        rem=n%10
        sum+=rem**2
        n=n//10
    return sum
n=int(input('enter a number'))
result=n
while(result!=1 and result !=4):
    result=HappyNumber(result)
if result==1:
    print('happy number')
else:
    print('not a happy number')



