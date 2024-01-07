import os
os.system("cls")

# or
sun = "down"
if sun == "down":
    print("Good night!")
print("I am here")

# if true, sale tax is add to the total
total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
    print(f"Subtotal:  ${total:.2f}")
    sales_tax = total * sales_tax_rate
    print(f"Sales Tax: ${sales_tax:.2f}")
    total = sales_tax + total
    print(f"Total:     ${total:.2f}")

# adding else to if logic
import datetime as dt 
now = dt.datetime.now()
if now.hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")
print("I hope you are doing well!")

# my example %p pentru PM
now = dt.datetime.now()
current_time = now.strftime("%H:%M: %a %D")
if now.hour < 12:
    print("Good morning, Paris!", current_time)
elif now.hour > 12 and now.hour <19:
    print("Good afternoon, Kimosabe!", current_time)
elif now.hour > 19 and now.hour < 0:
    print("Good evening, Bartolomeo!")
else:
    print("Nu ai interval acoperit - nu indeplineste nicio conditie")
print("Ai aprins toate luminile prin casa! \nMerry Christmas!")

# handling multiple else statements with elif
light_color = "green"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
print("Nu forta galbenu'!")

# or
light_color = "red"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
print("No matter the conditions, this will appear!")

#or
light_color = "yellow"
if light_color == "green":
    print("Go")
elif light_color == "red":
    print("Stop")
else:
    print("Proceed with coution, Robocop!")
