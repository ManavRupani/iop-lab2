# Name_Manav_Rupani
# Student_Id_22055532


list_=[1,2,3,4,5,6,7,8,9,10]
output0=[]
print("List of numbers:")
print(list_)
print("Numbers greater than 5")
for i in range(len(list_)):
    if list_[i]>5:
        output0.append(list_[i])
    else:
        pass
output0.sort()
print(output0)