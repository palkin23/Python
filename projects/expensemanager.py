import json

def load():
    try:
        with open('expenses.txt','r') as file:
            expense=json.load(file)
            return expense
    except FileNotFoundError:
       return []

def save(expenses):
     with open('expenses.txt' ,'w') as file:
         json.dump(expenses,file)

def  view_all_expenses(expenses):
    print("\n")
    print("*" *70)
    for i,expenses in enumerate(expenses,start=1):
        print(f"{i}.,Name:{expenses['name']},Category:{expenses['category']},Amount:{expenses['amount']}")
    print("*" *70)
    print("\n")
    
def addexpense(expenses):
    name=input("Enter expense name: ")
    category=input("Enter expense category: ")
    amount=float(input("Enter expense amount: "))
    expenses.append({'name':name,'category':category,'amount':amount})
    save(expenses)

def updateexpense(expenses):
    view_all_expenses(expenses)
    i = int(input("Enter the index you want to update: "))

    if 1 <= i <= len(expenses):
        name = input("Enter expense name: ")
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))

        expenses[i - 1] = {
            'name': name,
            'category': category,
            'amount': amount
        }

        save(expenses)
        print("Expense updated successfully!")

    else:
        print("Invalid index")

def deleteexpense(expenses):
    view_all_expenses(expenses)
    i = int(input("Enter the index you want to delete: "))

    if 1 <= i <= len(expenses):
        del expenses[i - 1]
        save(expenses)
        print("Expense deleted successfully!")
    else:
        print("Invalid index")

def view_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']

    print("Total spending is:", total)

def main():
    expenses=load()
    while(True):
        print("===== PERSONAL EXPENSE MANAGER =====")
        print("1. View all expenses")
        print("2. Add an expense")
        print("3. Update an expense")
        print("4. Delete an expense")
        print("5. View total spending")
        print("6. Exit")
        choice=input("Enter your choice: ")
        match choice:
            case '1':
                view_all_expenses(expenses)
            case '2':
                addexpense(expenses)
            case'3':
                updateexpense(expenses)
            case '4':
                deleteexpense(expenses)
            case '5':
                view_total(expenses)
            case '6':
                break
            case _:
                print("Invalid Option,Select your option again")
if __name__==("__main__"):
    main()

