print('Sieve of Eratosthenes')
listt = [2]
i=2
n=i

x=int((input('Do you want to know the number until which prime? \n')))
while (len(listt)<x-1):
   n+=1;
   listt.append(n)

def division():
   global i;
   while(i!=listt[-1]):
      for b in listt:
         if b%i == 0 and b != i:
      	    listt.remove(b)		 
      i+=1		 
   
division()
print("The prime numbers until",x,"are: ",listt)  

y=str(input('Do you want a specific prime? \n (Y/N) '))
if y=="Y" or y=="yes" or y=="Yes":
   p=int(input('which? '));
   print(listt[p-1])	 
elif y=="N" or y=="no" or y=="No":
   print('okie dokie')
else:
   print('You should answer with yes or no');
   y
	 