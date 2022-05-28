expense_list=[]
stopped =False
while not stopped:
    expense=int(input("enter your expense, (press 0 to stop) $"))
    # print(type(expense))
    if expense!=0:
        expense_list.append(expense)
    else:
        stopped=True

print(f"Your expense list is",expense_list)
print(f"Your total expense is",sum(expense_list))
print(f"Max expense is",max(expense_list))
print(f"Min expense is",min(expense_list))
