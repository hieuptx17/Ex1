# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
s = float(input("Enter 1st number "))
s1 = float(input("Enter 2nd number: "))
s2 = float(input("Enter 3rd number: "))

# if((s>s1)and(s>s2)):
#     print("max value: ",s)
# elif((s1>s)and(s1>s2)):
#     print("max value: ",s1)
# else:
#     print("max value: ",s2)

# if s > s1:
#     maxOfAAndB = s
# else:
#     maxOfAAndB = s1
#
# if maxOfAAndB > s2:
#     print("maximum value", maxOfAAndB)
# else:
#     print("maximum value", s2)

print(max(s,s1,s2))