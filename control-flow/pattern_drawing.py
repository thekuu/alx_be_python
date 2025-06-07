pattern_size = int(input("Enter the size of the pattern:"))
while  pattern_size >=1:
    for i in range(pattern_size):
        print("*", end="")
    pattern_size -= 1
    print()  # Print a new line after each pattern size