# pattern for lower tringular shape
def lower_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()

# Example usage
n = 5
lower_triangle(n)



# pattern for upper tringle shape
def upper_triangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end=" ")
        print()

# Example usage
n = 5
upper_triangle(n)


# pattern for paramid tringular shape
def pyramid_triangle(n):
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))

# Example usage
n = 5
pyramid_triangle(n)

