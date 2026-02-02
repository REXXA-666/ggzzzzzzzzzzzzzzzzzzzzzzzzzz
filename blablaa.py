n = int(input("Enter number: "))

odd = [i for i in range(1, n) if i % 2 != 0]
even = [i for i in range(1, n) if i % 2 == 0]

print("Odd:", odd)
print("Even:", even)
