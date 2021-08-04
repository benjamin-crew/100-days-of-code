def prime_number(number):
    prime = True
    for n in range(2, number):
        if number % n == 0:
            prime = False
    
    if prime == True:
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")



number = 10 #int(input("Enter a number: "))
prime_number(number)