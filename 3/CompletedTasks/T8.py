email = input("Enter you email,here:")

at_index = email.find("@")
username = email[:at_index]

print(username)