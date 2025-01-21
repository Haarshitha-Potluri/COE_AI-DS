def calculate_total(cart):

   total = 0

   total1 = 0

   for i in cart.values():

       if i >= 25000:

           total += i



       if i > 20000 and i < 50000:

           total *= 0.90



       elif i > 50000:

           total *= 0.85



   return total





cart = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 35000, 'Keyboard': 1500, 'Monitor': 8000, 'USB': 1000}

print(f"Total price : {calculate_total(cart)}")

