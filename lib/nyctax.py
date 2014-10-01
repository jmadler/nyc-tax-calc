def tax_calc(gross, deduction, residence):
    gross = float(gross)
    deduction = float(deduction)

    tax_total = 0

    city_tax_bracket = [
        # http://www.tax.ny.gov/pdf/current_forms/it/nyc_tax_rate_schedule.pdf
        { 'over': 500000, 'base': 18122, 'rate': 0.03876 },
        { 'over': 50000, 'base': 1706, 'rate': 0.03648 },
        { 'over': 25000, 'base': 808, 'rate': 0.03591 },
        { 'over': 12000, 'base': 349, 'rate': 0.03534 },
        { 'over': 0, 'base': 349, 'rate': 0.03534 },
    ]

    if residence == 'NYC':
        for i in city_tax_bracket:
            if gross > i['over']:
                tax_total += i['base']
                tax_total += i['rate'] * ( gross - i['over'] )
                break
    else:
        # We don't yet support other areas.
        raise Exception

    state_tax_bracket = [
        # http://www.tax.ny.gov/pdf/current_forms/it/nyc_tax_rate_schedule.pdf
        { 'over': 1029250, 'base': 69612, 'rate': 0.0882 },
        { 'over': 205850, 'base': 13209, 'rate': 0.0685 },
        { 'over': 77150, 'base': 4651, 'rate': 0.0665 },
        { 'over': 20550, 'base': 1000, 'rate': 0.059 },
        { 'over': 11300, 'base': 468, 'rate': 0.0525 },
        { 'over': 8200, 'base': 328, 'rate': 0.045 },
        { 'over': 0, 'base': 0, 'rate': 0.04 },
    ]

    for i in state_tax_bracket:
        if gross > i['over']:
            tax_total += i['base']
            tax_total += i['rate'] * ( gross - i['over'] )
            break

    federal_tax_bracket = [
        # where AGI = income - state tax - city tax - standard deduction (5,800) - all other deductions (0)
        # http://www.irs.gov/pub/irs-pdf/i1040.pdf 
        # http://www.irs.gov/publications/p501/index.html
        { 'over': 400000, 'base': 116163.75, 'rate': 0.396 },
        { 'over': 398350, 'base': 115586.25, 'rate': 0.35 },
        { 'over': 183250, 'base': 44603.25, 'rate': 0.33 },
        { 'over': 87850, 'base': 17891.25, 'rate': 0.28 },
        { 'over': 36250, 'base': 4991.25, 'rate': 0.25 },
        { 'over': 8925, 'base': 892.50, 'rate': 0.15 },
        { 'over': 0, 'base': 0, 'rate': 0.10 },
    ]

    agi = gross - tax_total - deduction

    for i in federal_tax_bracket:
        if agi > i['over']:
            tax_total += i['base']
            tax_total += i['rate'] * ( agi - i['over'] )
            break

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
