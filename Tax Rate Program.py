def calculate_taxes(total_sales):
    """Calculates county, state, and total sales tax."""
    STATE_TAX_RATE = 0.05 
    COUNTY_TAX_RATE = 0.025  
    
    state_tax = total_sales * STATE_TAX_RATE
    county_tax = total_sales * COUNTY_TAX_RATE
    total_tax = state_tax + county_tax
    
    return state_tax, county_tax, total_tax


def main():
    total_sales = float(input("Enter the total sales for the month: $"))
    
    state_tax, county_tax, total_tax = calculate_taxes(total_sales)
    
    print(f"\nSales Tax Report:")
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")


if __name__ == "__main__":
    main()