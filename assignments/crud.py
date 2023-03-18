from create import create
from assignments.read import read
from assignments.update import update
from assignments.delete import delete


def inquiry():
    selection = input("Welcome to Broadway. Select C/R/U/D/E ")
    selection = selection.lower()

    def continue_or_not(c):
        inquiry() if c else print("Thank You. See you again")
    if selection == 'c':
        cont = create()
        return continue_or_not(cont)
    elif selection == 'r':
        id = input("What is student ID? ")
        cont = read(id)
        return continue_or_not(cont)
    elif selection == 'u':
        id = input("What is student ID? ")
        to_change = input("What do you wish to update? (name, age, department) ")
        changed_info = input(f"Give the new {to_change} ")
        cont = update(id, to_change, changed_info)
        return continue_or_not(cont)
    elif selection == 'd':
        id = input("What is student ID? ")
        cont = delete(id)
        return continue_or_not(cont)
    else:
        print("Thank You. See you again")
        return


if __name__ == "__main__":
    inquiry()










# Read and write in JSON
# Update and Delete
# Password Required Decorator
# Packages in Python
# __name__ == "__main__"
# Virtual Environment
# Jupyter Notebook
# Trello, Slack, Jira
# Palindrome, ascending order, prime
