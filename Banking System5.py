class User:
    def __init__(self, first_name, last_name, gender, street_address, city, email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = balance
        self.account_no = account_no
        userList.append(self)

    def display_info(self):
        print("----------------------------------")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Gender: {self.gender}")
        print(f"Address: {self.street_address}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"CC number: {self.cc_number}")
        print(f"CC type: {self.cc_type}")
        print(f"Balance: {self.balance}")
        print(f"Account number: {self.account_no}")


def print_details():
    for User in userList:
        User.display_info()


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser(text):
    name = input(text).title()
    for User in userList:
        if User.first_name == name:
            User.display_info()
            return User
    print(f"We have no records of {name} in our database")

    
def overdrafts():
    overdraft_users = []
    total_overdraft_amount = 0

    for user in userList:
        if user.balance < 0:
            overdraft_users.append(user)
            total_overdraft_amount += user.balance

    print(f"Overdraft Users:\n"
          f"-----------------")
    for user in overdraft_users:
        print(f"{user.first_name} {user.last_name}")
    print("-----------------")
    print(f"Total Overdraft Users: {len(overdraft_users)}")
    print(f"Total Overdraft Amount: {total_overdraft_amount}")
    
def missingEmails():
    users_without_emails = []

    for user in userList:
        if user.email == "":
            users_without_emails.append(user)

    print(f"Users Without Emails:")
    for user in users_without_emails:
        print(f"{user.first_name} {user.last_name}")
    print("-----------------")
    print(f"Total Users Without Emails: {len(users_without_emails)}")

def bankDetails():
    total_number_users = len(userList)
    total_bank_worth = sum(user.balance for user in userList)

    user_lowest_balance = float('-inf')
    user_highest_balance = float('inf')
    for user in userList:
        if user.balance > user_highest_balance:
            user_highest_balance == user.balance
        if user.balance < user_lowest_balance:
            user_lowest_balance == user.balance
    print(f"Total Number of Users: {total_number_users}")
    print(f"Total Bank Worth: {total_bank_worth}")
    print(user_lowest_balance)
    print(user_highest_balance)




def transfer():
    # TO COMPLETE

    True

userList = []          
generateUsers()
userChoice = ""
print("Welcome")

while userChoice != "Q":
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type 6 to print user list")
    print("Type Q to quit")
    userChoice = input("Enter choice: ")
    print()
    
    if userChoice == "1":
        findUser("Enter the name of the employee you would like to find:")
    elif userChoice == "2":
        overdrafts()
    elif userChoice == "3":
        missingEmails()
    elif userChoice == "4":
        bankDetails()
    elif userChoice == "5":
        transfer()
    elif userChoice == "6":
        print_details()
    print()
