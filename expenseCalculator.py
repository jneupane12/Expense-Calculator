expense=-1
total_expense=0
while expense!=0:
    expense=int(input("enter your expense, (press 0 to stop) $"))
    total_expense=total_expense+expense
print(f"Your total expense is $",total_expense)
