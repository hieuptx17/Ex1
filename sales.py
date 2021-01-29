# s1 = float(input("Input 1st day sale: "))
# s2 = float(input("Input 2nd day sale: "))
# s3 = float(input("Input 3rd day sale: "))
# s4 = float(input("Input 4th day sale: "))
# s5 = float(input("Input 5th day sale: "))
# average = ((s1 + s2 + s3 + s4 + s5) / 5)
# print("The average of product is: ", average)

# total = 0
# for i in range(1, 6):
#     val = float(input("input sale for day %s: " %i))
#     total = total + val
# print("average sale: %.2f" % (total/5))

total = 0
sale = float(input("input sale value: "))
count = 0
while sale >= 0:
    total = total + sale
    count += 1
    sale = float(input("input sale value: "))
if count != 0:
    print("average sale: %.2f" % (total/count))




