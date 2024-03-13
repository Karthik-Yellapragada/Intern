def main():
    n=int(input('enter a number').strip())
    count=0
    for i in range(2,n//2+1):
        if n%i==0:
            count+=1
            break
    if count != 1:
        print('prime')
    else:
        print('not')
if __name__ == "__main__":
   main()