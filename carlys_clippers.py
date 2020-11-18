#specs / variables
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

# no3 avg price
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print('Average Haircut Price: ' + str(average_price))

#no5 lovering prices
new_prices = [price -5 for price in prices]
print(new_prices)

#no7 Revenue
total_revenue = 0

for i in range(len(hairstyles)): 
  total_revenue += prices[i]*last_week[i]

print('Total Revenue: ' + str(total_revenue))

#no10 avg dly rev
average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

#no12 promotion
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30] 

print(list(cuts_under_30))


