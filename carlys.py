hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Variable to store the length of the lists
len_price = len(prices)
len_hairstyles = len(hairstyles)


# # Task 1 
total_price = 0

# #Task 2 
for total_price in prices:
  print(total_price)

# Task 3 / 4 
average_price = total_price / len_price
print(f"{"Average Haircut Price: "}{average_price:.2f}")

# Task 5

new_prices = [total_price -5 for total_price in prices]
print(new_prices)

# task 7
total_revenue = 0

# Task 8 / 9

for i in range(len_hairstyles):
  total_revenue =  prices[i] + last_week[i]
print("Total Revenue: " + str(total_revenue))

# Task  10 / 11

average_daily_revenue = total_revenue/7
print(average_daily_revenue)

Task # 12 / 13
cuts_under_30 = [new_prices[i] for i in range(len(new_prices) -1) if new_prices[i] < 30] 
print(cuts_under_30)