def check_password(password):

   if len(password) < 10 or len(password) > 15:

       return "Good Password: should have more than 10 characters and less than 15 characters"

   elif not any(char.isupper() for char in password):

       return "Better Password: atleast one upper case"

   elif not any(char.islower() for char in password):

       return "Better Password: atleast one lower case"

   elif not any(char.isdigit() for char in password):

       return "Better Password: atleast one digit"

   elif any(char.isspace() for char in password):

       return "Better Password: should contain no space"

   elif not any(char in ['!', '@', '_', '#', '$', '*'] for char in password):

       return "Better Password: should contain special characters"

   elif password.endswith('.') or password.endswith('@'):

       return "Better Password: should not end with . or @"

   else:

       return "Strong Password"





p = input("Enter a password")

print(check_password(p))
