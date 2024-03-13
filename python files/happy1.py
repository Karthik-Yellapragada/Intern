def main():
    n=int(input('enter a number').strip())
    limit=int(input('enter the limit').strip())
    check=0
    while check<limit:
        sum=0
        while n>0:
            digit=n%10
            sum+=(digit*digit)
            n=n//10
        print(sum)
        if(sum==1):
            print(n,'is a Happy number')
            break
        else:
           n=sum
        check+=1
    if check==limit:
        print('You have crossed the limit')


if __name__ == "__main__":
   main()