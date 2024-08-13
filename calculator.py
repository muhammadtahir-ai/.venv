import streamlit as st

# Title
st.title("Pakistan Income Tax Calculator (2024-2025)")

# Add a sidebar for salary calculation
st.sidebar.header("Calculate Your Annual Salary")

# Option to calculate annual salary
calculate_salary = st.sidebar.checkbox("Do you want to calculate your annual salary?")

if calculate_salary:
    # Input fields for salary components
    monthly_salary = st.sidebar.number_input("Enter your monthly salary (PKR):", min_value=0.0, step=1000.0, format="%.2f")
    bonuses = st.sidebar.number_input("Enter your annual bonuses (PKR):", min_value=0.0, step=1000.0, format="%.2f")
    other_income = st.sidebar.number_input("Enter any other annual income (PKR):", min_value=0.0, step=1000.0, format="%.2f")
    
    # Calculate annual salary
    annual_income = (monthly_salary * 12) + bonuses + other_income
    st.sidebar.write(f"Your calculated annual salary is: PKR {annual_income:,.2f}")
else:
    # Direct input for annual income
    annual_income = st.number_input("Enter your annual taxable income (PKR):", min_value=0.0, step=1000.0, format="%.2f")

# Tax slabs for the year 2024-2025
def calculate_income_tax(income):
    tax = 0.0
    
    if income <= 600000:
        tax = 0
    elif income <= 1200000:
        tax = 0.05 * (income - 600000)
    elif income <= 2400000:
        tax = 30000 + 0.10 * (income - 1200000)
    elif income <= 3600000:
        tax = 150000 + 0.15 * (income - 2400000)
    elif income <= 4800000:
        tax = 330000 + 0.20 * (income - 3600000)
    elif income <= 6000000:
        tax = 570000 + 0.25 * (income - 4800000)
    elif income <= 30000000:
        tax = 870000 + 0.30 * (income - 6000000)
    else:
        tax = 8010000 + 0.35 * (income - 30000000)
    
    return tax

# Calculate tax
if annual_income > 0:
    tax_payable = calculate_income_tax(annual_income)
    st.write(f"Your calculated income tax for the year 2024-2025 is: PKR {tax_payable:,.2f}")
else:
    st.write("Please enter a valid income to calculate tax.")

# Display the tax slabs for reference
st.subheader("Income Tax Slabs (2024-2025)")
st.write("""
- Income up to PKR 600,000: 0%
- Income from PKR 600,001 to PKR 1,200,000: 5%
- Income from PKR 1,200,001 to PKR 2,400,000: PKR 30,000 + 10% of the amount exceeding PKR 1,200,000
- Income from PKR 2,400,001 to PKR 3,600,000: PKR 150,000 + 15% of the amount exceeding PKR 2,400,000
- Income from PKR 3,600,001 to PKR 4,800,000: PKR 330,000 + 20% of the amount exceeding PKR 3,600,000
- Income from PKR 4,800,001 to PKR 6,000,000: PKR 570,000 + 25% of the amount exceeding PKR 4,800,000
- Income from PKR 6,000,001 to PKR 30,000,000: PKR 870,000 + 30% of the amount exceeding PKR 6,000,000
- Income above PKR 30,000,000: PKR 8,010,000 + 35% of the amount exceeding PKR 30,000,000
""")
