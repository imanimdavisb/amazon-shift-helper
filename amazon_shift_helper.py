hours = float(input("How many hours did you work this week? "))
pay_rate = float(input("What is your hourly pay rate? "))

if hours > 40:
    overtime_hours = hours - 40
    regular_pay = 40 * pay_rate
    overtime_pay = overtime_hours * pay_rate * 1.5
    total_pay = regular_pay + overtime_pay
else:
    total_pay = hours * pay_rate

print(f"\nEstimated weekly pay before taxes: ${total_pay:.2f}")
