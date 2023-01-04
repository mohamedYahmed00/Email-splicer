email = input('Please enter the email address:').strip()

username  = email[:email.index("@")] # User name anything before @

domain_name = email[email.index("@") + 1:] # Domain anything after @

format_email = (f"Your username is '{username}' and your domain is '{domain_name}'") # join everything togather

print(format_email)
