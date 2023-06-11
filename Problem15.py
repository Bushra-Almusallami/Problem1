def discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    return discounted_price

#Enter the price and discounted_price
discounted_price = int(discount(1100,50))

#print the price after the discount
print("The price after the discount is", discounted_price)
