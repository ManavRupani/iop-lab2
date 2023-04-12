# Name_Manav_Rupani
# Student Id-22055532

a=int(input("Enter number of years : "))
list_=[]
for i in range(1,a+1):
    print(f"For Year {i} : ")
    for j in range(1,13):                                                 
        print(f"Enter the rainfall amount of the month-{j}:",end="")
        input0=int(input())
        list_.append(input0)
    print(f"For 12 Months")
    print(f"Total rainfall {sum(list_)}")
    print(f"Average Monthly rainfall: {sum(list_)/12} inches")
