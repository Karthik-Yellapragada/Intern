def main():
   print("Enter two strings : ")
   s1=input().strip().lower()
   s2=input().strip().lower()

   if len(s1)==len(s2):
       if sorted(s1)==sorted(s2):
           print("Anagrams")
       else:
           print("NOT")
   else:
       print("NOT")

if __name__ == "__main__":
   main()



