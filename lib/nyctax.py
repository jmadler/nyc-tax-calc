def tax_calc(gross, deduction, residence):
    gross = float(gross)
    deduction = float(deduction)
    if gross < 83600 or gross > 174400:
        raise

    tax_total = 0

    # state 
    # 6.85% of over 40,000
    # plus 1,946
    # for between 40k and 300k
    # http://www.tax.ny.gov/pdf/current_forms/it/it150_201i.pdf

    tax_total += 1946 + (gross * 0.0685)
    
    # city
    # 3.648% of over 50,000
    # plus 1,706
    # for between 50k and 500k
    # http://www.tax.ny.gov/pdf/2010/inc/nyc_tax_rate_150_201.pdf

    tax_total += 1706 + ( (gross - 50000) * 0.03648 )

    # federal
    # 28% of over 83,600
    # plus 17,025
    # for AGI between 83,600 and 174,400
    # where AGI = income - state tax - city tax - standard deduction (5,800) - all other deductions (0)
    # http://www.irs.gov/pub/irs-pdf/i1040.pdf 
    # http://www.irs.gov/publications/p501/index.html
    agi = gross - tax_total - 5800
    tax_total += 17025 + ( (agi - 83600) * 0.28 )

    # FICA 
    # 7.65%
    # http://www.money-zine.com/Financial-Planning/Tax-Shelter/FICA-Tax/
    tax_total += (agi * 0.0765);

    return round(tax_total, 2)
