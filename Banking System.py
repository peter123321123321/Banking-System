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
        print("----------------------------------")


def print_details():
    for User in userList:
        User.display_info()


def generateUsers():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], float(line[8]), line[9])


def findUser():
    # TO COMPLETE

    True
    
def overdrafts():
    # TO COMPLETE
    
    True
    
def missingEmails():
    # TO COMPLETE

    True

def bankDetails():
    # TO COMPLETE

    True
    
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
        findUser()
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
