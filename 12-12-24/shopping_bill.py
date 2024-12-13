salary = int(input("enter employee salary"))
bill_1 = int(input("shopping bill 1:"))
bill_2 = int(input("shopping bill 2:"))
bill_3 = int(input("shopping bill 3:"))

total = bill_1 + bill_2 + bill_3
print("your total shopping bill is :", total)
sal_left = salary - total
percentage = (total / salary) * 100
print("you spent ", percentage, "% of your salary on shopping ")
