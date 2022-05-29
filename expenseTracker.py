from datetime import date
import csv

dt =date.today()
dt= dt.strftime("%d/%m/%Y")

filename="tracker.csv"
exp_list=[]
stopped=False
with open(filename,"a") as f:
    csv_write= csv.writer(f)
    csv_write.writerow(["Date","Expense in $"])
    while not stopped:
        expense=int(input("Enter your expense,(type 0 to stop) "))
        if expense==0:
            stopped= True
        else:

            csv_write.writerow([dt,('$',expense)])
            exp_list.append(expense)

print("\nFile Successfully written to a file")


