# Name_Manav_Rupani
# Student_Id_22055532
list_=[]
n=int(input("Enter length of List "))
print("Enter Your numbers ")            
for j in range(n):
    tmp=int(input())
    list_.append(tmp)
output0=[]

print("List of numbers:")
print(list_)
temp2=int(input("Enter value a value for sorting "))
print(f"Numbers greater than {temp2}")
for i in range(len(list_)):
    if list_[i]>temp2:
        output0.append(list_[i])
    else:
        pass
output0.sort()
print(output0)