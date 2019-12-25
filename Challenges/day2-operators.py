meal_cost = float(input())
tip_percent = int(input())
tax_percent = int(input())

def percent(x, y):
    return (x*y)/100


def solve(meal_cost, tip_percent, tax_percent):
    total_cost = 0
    new_tip_percent = percent(tip_percent, meal_cost)
    new_tax_percent = percent(tax_percent, meal_cost)
    total_cost = meal_cost + new_tax_percent + new_tip_percent
    print(round(total_cost))

solve(12.00, 20, 8)
