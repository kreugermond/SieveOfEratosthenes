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
z=len(listt)
print("The prime numbers until",x,"are: ",listt)
print("There are",z,"primes in this list")

y=str(input('Do you want the position of a prime or a prime by its position? \n (Pos/Pri/N) '))
if y=="Pos" or y=="pos" or y=="position":
   p=int(input('which? '));
   print("the",p,"prime is:",listt[p-1])
elif y=="Pri" or y=="pri" or y=="prime":
       p=int(input('which? '));
       index=listt.index
       print(p,"is the",listt.index(p)+1,"prime")
elif y=="N" or y=="no" or y=="No":
   print('okie dokie')
else:
   print('You should answer with yes or no');
