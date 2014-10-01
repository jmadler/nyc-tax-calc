def tax_calc(gross, deduction, residence):
    gross = float(gross)
    deduction = float(deduction)

    tax_total = 0

    if residence == 'NYC':
        # http://www.tax.ny.gov/pdf/current_forms/it/nyc_tax_rate_schedule.pdf
        if gross > 500000:
            tax_total += 18122 + (gross * 0.03876)
        else if gross > 50000:
            tax_total += 1706 + (gross * 0.03648)
        else if gross > 25000:
            tax_total += 808 + (gross * 0.03591)
        else if gross > 12000:
            tax_total += 349 + (gross * 0.03534)
        else:
            tax_total += 0 + (gross * 0.02907)
    else:
        # We don't yet support other areas.
        raise Exception

    # state 
    # http://www.tax.ny.gov/pdf/2013/inc/it201i_2013.pdf
    if gross > 1029250:
        tax_total += 69612 + (gross * 0.0882)
    else if gross > 205850:
        tax_total += 13209 + (gross * 0.0685)
    else if gross > 77150:
        tax_total += 4651 + (gross * 0.0665)
    else if gross > 20550:
        tax_total += 1000 + (gross * 0.0645)
    else if gross > 13350:
        tax_total += 575 + (gross * 0.059)
    else if gross > 11300:
        tax_total += 468 + (gross * 0.0525)
    else if gross > 8200:
        tax_total += 328 + (gross * 0.045)
    else:
        tax_total += 0 + (gross * 0.04)
        
    # federal
    # where AGI = income - state tax - city tax - standard deduction (5,800) - all other deductions (0)
    # http://www.irs.gov/pub/irs-pdf/i1040.pdf 
    # http://www.irs.gov/publications/p501/index.html
    agi = gross - tax_total - deduction
    if agi > 400000:
        tax_total += 116163.75 + (agi * 0.396)
    else if agi > 398350:
        tax_total += 115586.25 + (agi * 0.35)
    else if agi > 183250:
        tax_total += 44603.25 + (agi * 0.33)
    else if agi > 87850:
        tax_total += 17891.25 + (agi * 0.28)
    else if agi > 36250:
        tax_total += 4991.25 + (agi * 0.25)
    else if agi > 8925:
        tax_total += 892.50 + (agi * 0.15)
    else:
        tax_total += 0 + (agi * 0.10)

    # FICA 
    # 6.2% SSA (up to the wage base of 113700)
    # 1.45% Medicare
    # http://www.irs.gov/taxtopics/tc751.html
    tax_total += (agi * 0.0145);
    if agi >= 113700:
        tax_total += (113700 * 0.062)
    else:
        tax_total += (agi * 0.062)

    return round(tax_total, 2)
