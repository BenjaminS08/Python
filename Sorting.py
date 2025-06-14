#Gaining five different Name inputs
name1 = (input(f"Input a name?"))
name2 = (input(f"Input a name?"))
name3 = (input(f"Input a name?"))
name4 = (input(f"Input a name?"))
name5 = (input(f"Input a name?"))
#Creating List of Names
name_list = [name1, name2, name3, name4, name5]
name_list = [name.lower() for name in name_list]
swapped = True
while swapped:
    swapped = False
    for i in range(len(name_list) - 1):
        if name_list[i] > name_list[i + 1]:
            name_list[i], name_list[i + 1] = name_list[i + 1], name_list[i]
            swapped = True 
print(f"Names in order",name_list)
name_list.reverse()
print(f"Names in reverse order", name_list)