distance = int(input())
passanger = int(input())
priceofpetrol= 70
mileage = 10
priceofticket = 80
cost = (distance/mileage)*priceofpetrol
income = passanger*priceofticket
if cost<income:
    print("Profit of :", (income-cost))
elif income<cost:
    print("Loss of :", (cost-income))
else:
    print("No profit No loss")