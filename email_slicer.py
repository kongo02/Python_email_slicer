# collect email from user
# split the email using the @, then the first part as the username ,
# the sond part will be the domain
#  split domain using .com

def main():
    print("Welcome to the email slicer")
    print("")

    email_input = input("Enter your email address: ")
    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print(f"Username: {username} ")
    print(f"Domain: {domain} ")
    print(f"Extension: {extension} ")


main()