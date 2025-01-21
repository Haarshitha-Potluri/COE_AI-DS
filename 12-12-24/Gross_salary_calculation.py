basic_sal = int(input("enter salary:"))

if basic_sal < 10000:
    HRA = (basic_sal * 67) / 100
    DA = (basic_sal * 73) / 100
elif basic_sal <= 10000:
    HRA = (basic_sal * 69) / 100
    DA = (basic_sal * 76) / 100
elif basic_sal > 20000:
    HRA = (basic_sal * 73) / 100
    DA = (basic_sal * 89) / 100

GS = HRA + DA + basic_sal
print("gross salary is :", GS)
print("HRA:", HRA)
print("DA:", DA)
