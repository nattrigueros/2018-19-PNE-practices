
n_term=int(input('Please introduce the nth term you want to find out from the Fibonacci series: '))

first_n_term = 0
second_n_term = 1
count = 0

if n_term <= 0:
   print("Please you should introduce a positive value for the nth term.")

elif n_term == 1:
   print("The corresponding Fibonacci series for",n_term,"is: ")
   print(first_n_term)

else:
   print("The corresponding Fibonacci series for",n_term,"is: ")
   while count < n_term:
       print(first_n_term,end=' , ')
       nth_term = first_n_term + second_n_term
       first_n_term = second_n_term
       second_n_term = nth_term
       count += 1