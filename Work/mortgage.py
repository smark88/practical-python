# mortgage.py
#
# Exercise 1.7
#principal = 500000.0
#rate = 0.05
#payment = 2684.11

def mortgage(extra_payment, principal, payment, rate):
    total_paid = 0.0
    months = 0.0
    extra_payment_start_month = 61
    extra_payment_end_month = 108
    while principal > 0:
        months = months + 1
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
        
        if months >= extra_payment_start_month and months <= extra_payment_end_month:
            principal = principal * (1+rate/12) - extra_payment
            total_paid = total_paid + extra_payment
        
        if principal < 0:
            total_paid = total_paid + principal
            principal = 0

        print(int(months), total_paid, principal)

    output= f'Total paid: ${total_paid:0.2f} Months: {int(months)}'
    print(output)

if __name__ == '__main__':
    mortgage(1000,500000,2684.11,0.05)