proj=int(input("enter your project score:"))
internal=int(input("enter your internal score:"))
external=int(input("enter your external score:"))
total=0
if(proj>50 and internal>50 and external>50):
    total=((proj*70)/100) +((internal*10)/100)+((external*20)/100)
    print("Total score is :",total)
else:
    if(proj<=50):
        print("failed in project,score is:",proj)
    if (internal <= 50):
            print("failed in internal,score is:", internal)
    if (external<= 50):
                print("failed in external,score is:", external)

if(total>90):
    print("A grade")
elif(total>80):
    print("B grade")
elif(total>50):
    print("c grade")