# Author: Fahad Ahmad Fayaz
# Internship: Python Developer

# Fibonacci Generator Program
# This program generates the Fibonacci sequence up to n terms

def fibonacci(n):
    # Created an empty list to store the Fibonacci numbers
    sequence = []
    
    # First two Fibonacci numbers
    a, b = 0, 1

    # Loop runs n times to generate n numbers
    for _ in range(n):
        # Add the current value of 'a' to the list
        sequence.append(a)

        # Update values:
        # 'a' becomes the previous 'b'
        # 'b' becomes the sum of previous 'a' and 'b'
        a, b = b, a + b

    # Return the complete Fibonacci sequence
    return sequence


# Ask from the User as Input to enter how many terms they want
terms = int(input("Enter number of terms: "))

if terms <= 0:
        print("Please enter a positive number.")
else:
    # Print the Fibonacci sequence
    print("Fibonacci Series:", fibonacci(terms))

# Calling of the function and storing the result
result = fibonacci(terms)