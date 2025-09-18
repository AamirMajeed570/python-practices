# number = int(input("Enter a Number"))
# print(number)
# for i in range(number):
#     print(f"{number} * {i+1} = {((i+1)*number)}")

# write a program to add two Numbers

num1 = int(input("Enter first Number"))
num2 = int(input("Enter second Number"))

# def add_nums(num1,num2):
#     return num1 + num2;

# res = add_nums(num1,num2)
# print(f"Sum of {num1} and {num2} is {res}")

def average(num1,num2):
    return (num1+num2)/2;
res = average(num1,num2)
print(f"Average of {num1} and {num2} is {res}")

