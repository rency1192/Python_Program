def pswd(x):
 
   l, u, d, s = 0,0,0,0
  
   if (len(x)>6 and len(x)<12):


       for i in range(len(x)):
           if (x[i].islower()):
               l+=1
           elif (x[i].isupper()):
               u+=1
           elif (x[i].isdigit()):
               d+=1
          
           elif (x[i]=='@' or x[i]=='$' or x[i]=='#' or x[i]=="_"):
               s+=1
          
   if (l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(x)):
       print("password is valid")
   else:
       print("password is not valid, try to enter strong password")




x = str(input("Enter Your Password : "))
pswd(x)
