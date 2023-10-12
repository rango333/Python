# ## Create system for furniture store "Neat Suites on Fleet Street" to help speed up the process of creating receipts for customers

# # Add in the catalog
lovely_loveseat_description = """lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00
stylish_settee_description = """Stylish Settee. Faux leather on birch. 29.50 inches high x  54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price = 180.50
luxurious_lamp_description = """Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price = 52.15
# calculate 8.8% sales tax
sales_tax = .088

# # Process the total price and item list of the first customer
customer_one_total = 0
customer_one_itemization = ""
# Customer decides to purchase the Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
# Customer decides to purchase the luxurious lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += "\n&\n" + luxurious_lamp_description
# calculate total with sales tax
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
format_customer_one_total = "{:.2f}".format(customer_one_total)

print("Customer One Items:\n" + customer_one_itemization + "\n")
print("Customer One Total:\n" + str(format_customer_one_total))
