def  fibonacci(n_term):
    first_n_term = 0
    second_n_term = 1
    count = 0
    fibo=[]
    if n_term <= 0:
       print("Please you should introduce a positive value for the nth term.")

    elif n_term == 1:
       print("The corresponding Fibonacci series for",n_term,"is: ")
       print(first_n_term)

    else:
       print("The corresponding Fibonacci series for",n_term,"is: ")
       while count < n_term:
           nth_term = first_n_term + second_n_term
           first_n_term = second_n_term
           second_n_term = nth_term
           count += 1
           fibo.append(first_n_term)
    return fibo

try:
    n = int(input('Enter a valid integer: '))
    fibonacci = fibonacci(n)
    print('This is the corresponding Fibonacci series for', n, 'is: ', fibonacci)
    sum = 0
    for i in range(len(fibonacci)):
        sum = sum + fibonacci[i]
    print('The sum of the Fibonacci series for the integer you introduced is: ', sum)

except  ValueError:
    print('Sorry you should introduce a valid integer.')