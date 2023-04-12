# name_Manav_Rupani
# student_Id_22055532

a_Org=float(input("Enter Number of organism: "))
p_Org=float(input("Average daily percentage increase: "))             
d_Org=int(input("Enter number of day to disaplay in final data: "))
print("Day Approimate\t\t\tPopulation")
print("------------------------------------------")
for i in range(1,d_Org+1):
    print(f"{i}\t\t\t\t{a_Org}")
    a_Org=a_Org+a_Org*(p_Org/100)
