n=input("Enter the word that you want to be Abbreviated")
l=len(n)
first_char=n[0]
last_char=n[l-1]
middle=l-2
if(l<10):
    print("Too Short")
   
elif(l>100):
    print("Too long")

else:
    print(first_char,middle,last_char,sep='')



