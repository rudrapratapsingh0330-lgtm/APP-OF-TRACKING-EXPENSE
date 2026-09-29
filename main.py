expensesLIST=[]
print("Welcome to the Expense Tracker!")

while True:
    print("==Menu==:")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Highest Expense")
    print("5. Delete an Expense")
    print("6. Modify an Expense")
    print("7. Clear all expenses")
    print("8. Average of all expenses")
    print("9. Category wise expenses")
    print("10. Expense Count")
    print("11. Above average expenses")
    print("12. Below average expenses")
    print("13. Set Monthly Budget")
    print("14. check Budget Status")
    print("15. Exit")

    choice = int(input("please Enter your choice (1-15): "))

    if(choice==1): #add expense
        date=input("please enter the date of expense (YYYY-MM-DD): ")
        category=input("please enter the category of expense ( Food, Travel, stationary,etc): ")
        description=input("please give more details about the expense: ")
        amount=float(input("please enter the amount of expense:₹ "))

        expense={
            'date': date,
            'category': category,
            'description': description,
            'amount': amount}
        
        expensesLIST.append(expense)
        print("\nDone , Expense added successfully!")

    elif(choice==2): #view all the expenses
        if(  len(expensesLIST)==0):
            print("No expenses seen.")
        else:
            print("Expenses:")
            count=1
            for every_expense in expensesLIST:
                print(f"{count} - {every_expense["date"]} - {every_expense["category"]} - {every_expense["description"]} - ₹{every_expense["amount"]}")
                count+=1


    elif (choice==3): #view total expenses
        total=0
        for every_expense in expensesLIST:
            total+= every_expense["amount"]

        print(f"Total Expenses: ₹{total}")  

    elif (choice==4): #view the highest expense
        if(len(expensesLIST)==0):
            print("No expenses seen.")
        else:
            highest_expense=max(expensesLIST, key=lambda x: x["amount"])
            print(f"Highest Expense: {highest_expense['date']} - {highest_expense['category']} - {highest_expense['description']} - ₹{highest_expense['amount']}")

    elif (choice==5): #delete an expense
        if(len(expensesLIST)==0):
            print("No expenses to delete.")
        else:
            print("Expenses:")
            count=1
            for every_expense in expensesLIST:
                print(f"{count} - {every_expense['date']} - {every_expense['category']} - {every_expense['description']} - ₹{every_expense['amount']}")
                count+=1

            index=int(input("please enter the number of the expense to delete: ")) - 1
            if 0 <= index < len(expensesLIST):
                deleted_expense=expensesLIST.pop(index)
                print(f"Expense deleted: {deleted_expense['date']} - {deleted_expense['category']} - {deleted_expense['description']} - ₹{deleted_expense['amount']}")
            else:
                print("Invalid expense number.")

    elif (choice==6): #modify an expense
        if(len(expensesLIST)==0):
            print("No expenses to modify.")
        else:
            print("Expenses:")
            count=1
            for every_expense in expensesLIST:
                print(f"{count} - {every_expense['date']} - {every_expense['category']} - {every_expense['description']} - ₹{every_expense['amount']}")
                count+=1

            index=int(input("please enter the number of the expense to modify: ")) - 1
            if 0 <= index < len(expensesLIST):
                expense_to_modify=expensesLIST[index]
                print(f"Modifying Expense: {expense_to_modify['date']} - {expense_to_modify['category']} - {expense_to_modify['description']} - ₹{expense_to_modify['amount']}")
                
                new_date=input("please enter the new date of expense (YYYY-MM-DD) or press Enter to keep it unchanged: ")
                new_category=input("please enter the new category of expense or press Enter to keep it unchanged: ")
                new_description=input("please give more details about the expense or press Enter to keep it unchanged: ")
                new_amount=input("please enter the new amount of expense or press Enter to keep it unchanged:₹ ")

                if new_date:
                    expense_to_modify['date']=new_date
                if new_category:
                    expense_to_modify['category']=new_category
                if new_description:
                    expense_to_modify['description']=new_description
                if new_amount:
                    expense_to_modify['amount']=float(new_amount)

                print("Expense modified successfully!")
            else:
                print("Invalid expense number.")
    
            

    elif (choice==7): #clear all the expenses
        expensesLIST.clear()
        print("All expenses cleared.")

    elif (choice==8): #calculate average
        if len(expensesLIST) == 0:
            print("No expenses to calculate average.")
        else:
            total = sum(expense['amount'] for expense in expensesLIST)
            average = total / len(expensesLIST)
            print(f"Average of all expenses: ₹{average:.2f}")

    elif (choice==9): #category wise expenses
        if len(expensesLIST) == 0:
            print("No expenses to display.")
        else:
            category = input("please enter the category of expenses to display: ")
            category_expenses = [expense for expense in expensesLIST if expense['category'] == category]
            if category_expenses:
                print(f"Expenses for category '{category}':")
                for expense in category_expenses:
                    print(f" - {expense['date']} - {expense['description']} - ₹{expense['amount']}")
            else:
                print(f"No expenses found for category '{category}'.")

    elif (choice==10): #expense count
        print(f"Total number of expenses: {len(expensesLIST)}")

    elif (choice==11): #above average expenses
        if len(expensesLIST) == 0:
            print("No expenses to display.")
        else:
            total = sum(expense['amount'] for expense in expensesLIST)
            average = total / len(expensesLIST)
            above_average = [expense for expense in expensesLIST if expense['amount'] > average]
            if above_average:
                print(f"Expenses above average (₹{average:.2f}):")
                for expense in above_average:
                    print(f" - {expense['date']} - {expense['description']} - ₹{expense['amount']}")
            else:
                print(f"No expenses found above the average.")

    elif (choice==12): #expenses below average
        if len(expensesLIST) == 0:
            print("No expenses to display.")
        else:
            total = sum(expense['amount'] for expense in expensesLIST)
            average = total / len(expensesLIST)
            below_average = [expense for expense in expensesLIST if expense['amount'] < average]
            if below_average:
                print(f"Expenses below average (₹{average:.2f}):")
                for expense in below_average:
                    print(f" - {expense['date']} - {expense['description']} - ₹{expense['amount']}")
            else:
                print(f"No expenses found below the average.")

    elif (choice==13): #set monthly budget
        try:
            amount = float(input("please enter your monthly budget: ₹ "))
            if amount > 0:
                monthly_budget = amount
                print(f"Monthly budget set to ₹{monthly_budget:.2f}")
            else:
                print("Budget must be greater than 0.")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    elif (choice==14): #check budget status
        if 'monthly_budget' in locals():
            total_expenses = sum(expense['amount'] for expense in expensesLIST)
            if total_expenses > monthly_budget:
                print(f"You have exceeded your monthly budget of ₹{monthly_budget:.2f}. Total expenses: ₹{total_expenses:.2f}")
            else:
                print(f"You are within your monthly budget of ₹{monthly_budget:.2f}. Total expenses: ₹{total_expenses:.2f}")
        else:
            print("Monthly budget not set. Please set your monthly budget first.")
                

    elif (choice==15): #exit
        print("Exiting the Expense Tracker , Goodbye!")
        break
            

    else:
        print("INVALID CHOICE. Please try again later.")