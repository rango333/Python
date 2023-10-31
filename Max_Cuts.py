# ## Calculate important metrics that can be used to plan out operation of the business for the rest of the month

# Determine hairstyles and prices for each style
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# Determine number of hairstyle type of last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Determine total price of each style
total_price = 0

for price in prices:
  total_price += price

# Determine and print the average price
average_price = total_price / len(prices)
print(round(average_price, 2))

# Reduce each hairstyle price by $5 and print out the price list
new_prices = [price - 5 for price in prices]
print(new_prices)

#Determine revenue of last week and print
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print(total_revenue)

#Determine average daily revenue of last week and print
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Print out a list for hairstyles under $30 after reducing each style by $5
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)