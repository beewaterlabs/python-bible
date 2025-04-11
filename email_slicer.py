# email_slicer.py

# get user email address

email = input("What is your email address?: ").strip()

# slice out user nane

user = email[:email.index("@")]

# slice domain name:
# Start at the character after the @ sign by using the index method:
# email.index("@") + 1
# and slice to the end of the string:

domain = email[email.index("@") + 1:]

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message

print(output)
