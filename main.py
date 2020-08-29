
prime = True
prime_number = 0
prime_number_str = ''

while True:
  prime_number_str = input("enter a number: ")
  
  if prime_number_str.isdecimal():
    prime_number = int(prime_number_str)
    print(prime_number_str)
    break
  else:
    print("you entered a incorrect number please try again")
 



for i in range(2, prime_number):
  prime_number%i
  print(prime_number%i)

  if prime_number%i == 0:
    prime = False
    break
    
    

if prime == True:
  print("yes it is a prime number")
else:
  print("no it is not a prime number")
  
  
  

