#завдання 1
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
for i in range(start, end, 1):
    if i%7 != 0:
        continue
    print(i)

# #завдання 2

# start = int(input("Enter first number: "))
# end = int(input("Enter second number: "))
# for i in range(start, end, 1):
#     print(i)
#     while i > 0:
#         i - 1
#     if i%7 != 0:
#         continue
# print(i)
# n = 0;
# while i%5 == 0:
#     n + 1
# print(n)



#завдання 3
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))
for i in range(start, end, 1):
    if i%3 == 0:
        print("Fizz")
    if i%5 == 0:
        print("Buzz")
    if i%15 == 0:
        print("Fizz Buzz")
    if i%15 != 0:
        print(i)