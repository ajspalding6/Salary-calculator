def fed_tax(desired_yearly_income):
    ranges = [
        (0, 11000, 0.1),
        (11001, 44725, 0.12),
        (44726, 95375, 0.22),
        (95376, 181375, 0.24),
        (181376, 231250, 0.32),
        (231251, 578125, 0.35),
    ]
    for start, end, rate in ranges:
        if start <= desired_yearly_income <= end:
            print(rate)
            return rate
    print(0.37)
    return 0.37  # Default rate if the income is not in any of the specified ranges

def state_tax(desired_yearly_income):
    ranges = [
        (0, 3000, 0.02),
        (3001, 5000, 0.03),
        (5001, 17000, 0.05),
    ]

    for start, end, rate in ranges:
        if start <= desired_yearly_income <= end:
            print(rate)
            return rate
    print(0.0575)
    return 0.0575  # Default rate if the income is not in any of the specified state tax ranges

def calculate_hourly_rate(desired_monthly_income, hours_per_week, weeks_per_month):
    yearly_income = int(desired_monthly_income * 12)
    fed_tax_rate = fed_tax(yearly_income)
    state_tax_rate = state_tax(yearly_income)
    monthly_income_after_tax = desired_monthly_income * (1 + (fed_tax_rate + state_tax_rate))
    hourly_rate = monthly_income_after_tax / (hours_per_week * weeks_per_month)
    return hourly_rate

def calculate_yearly_salary(desired_monthly_income):
    yearly_income = desired_monthly_income * 12
    fed_tax_rate = fed_tax(yearly_income)
    state_tax_rate = state_tax(yearly_income)
    monthly_income_after_tax = yearly_income * (1 + (fed_tax_rate + state_tax_rate))
    return monthly_income_after_tax

# Get user inputs
desired_monthly_income = float(input("Enter your desired monthly income after taxes: $"))
employment_type = input("Are you working hourly or salary? (Type 'hourly' or 'salary'): ").lower()

# Check employment type
if employment_type == 'hourly':
    hours_per_week = float(input("How many hours a week do you want to work?: "))
    weeks_per_month = 4  # Assuming an average of 4 weeks in a month
    hourly_rate = calculate_hourly_rate(desired_monthly_income, hours_per_week, weeks_per_month)
    print(f"To achieve a monthly income of ${desired_monthly_income:.2f} after taxes working {hours_per_week} hours a week, you need to make ${hourly_rate:.2f} per hour.")
    
elif employment_type == 'salary':
    yearly_salary = calculate_yearly_salary(desired_monthly_income)
    print(f"To achieve a monthly income of ${desired_monthly_income:,.2f} after taxes on a salary, you need a yearly salary of ${yearly_salary:,.2f}.")
    
else:
    print("Invalid employment type. Please enter 'hourly' or 'salary'.")
