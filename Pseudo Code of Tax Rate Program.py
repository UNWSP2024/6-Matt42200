START


DEFINE FUNCTION calculate_taxes(total_sales)
    SET STATE_TAX_RATE = 0.05
    SET COUNTY_TAX_RATE = 0.025
    SET state_tax = total_sales * STATE_TAX_RATE
    SET county_tax = total_sales * COUNTY_TAX_RATE
    SET total_tax = state_tax + county_tax
    RETURN state_tax, county_tax, total_tax
END FUNCTION


DEFINE FUNCTION main()
    DISPLAY "Enter the total sales for the month: "
    INPUT total_sales
    CALL calculate_taxes(total_sales) AND STORE state_tax, county_tax, total_tax


    DISPLAY "Sales Tax Report:"
    DISPLAY "County Sales Tax: $" + FORMAT(county_tax, 2 decimal places)
    DISPLAY "State Sales Tax: $" + FORMAT(state_tax, 2 decimal places)
    DISPLAY "Total Sales Tax: $" + FORMAT(total_tax, 2 decimal places)
END FUNCTION


CALL main()


END