def pct(value):
    return value / 100

def tax_calc(gross, deduction, residence):
    gross = float(gross)
    deduction = float(deduction)

    tax_total = 0

    city_tax_bracket = [
        # http://www.tax.ny.gov/pdf/current_forms/it/nyc_tax_rate_schedule.pdf
        { 'over': 500000, 'base': 18122, 'rate': pct(3.876) },
        { 'over':  50000, 'base':  1706, 'rate': pct(3.648) },
        { 'over':  25000, 'base':   808, 'rate': pct(3.591) },
        { 'over':  12000, 'base':   349, 'rate': pct(3.534) },
        { 'over':      0, 'base':   349, 'rate': pct(3.534) },
    ]

    if residence == 'NYC':
        tax_total += find_tax_liability(city_tax_bracket, gross)
    else:
        # We don't yet support other areas.
        raise Exception

    state_tax_bracket = [
        # http://www.tax.ny.gov/pdf/current_forms/it/nyc_tax_rate_schedule.pdf
        { 'over': 1029250, 'base': 69612, 'rate': pct(8.82) },
        { 'over':  205850, 'base': 13209, 'rate': pct(6.85) },
        { 'over':   77150, 'base':  4651, 'rate': pct(6.65) },
        { 'over':   20550, 'base':  1000, 'rate': pct(5.90) },
        { 'over':   11300, 'base':   468, 'rate': pct(5.25) },
        { 'over':    8200, 'base':   328, 'rate': pct(4.50) },
        { 'over':       0, 'base':     0, 'rate': pct(4.00) },
    ]

    tax_total += find_tax_liability(state_tax_bracket, gross)

    # Federal income tax permits deducting state income tax from 
    federal_agi = gross - tax_total - deduction

    federal_tax_bracket = [
        # where AGI = income - state tax - city tax - standard deduction (5,800) - all other deductions (0)
        # http://www.irs.gov/pub/irs-pdf/i1040.pdf 
        # http://www.irs.gov/publications/p501/index.html
        { 'over': 400000, 'base': 116163.75, 'rate': pct(39.6) },
        { 'over': 398350, 'base': 115586.25, 'rate': pct(35) },
        { 'over': 183250, 'base':  44603.25, 'rate': pct(33) },
        { 'over':  87850, 'base':  17891.25, 'rate': pct(28) },
        { 'over':  36250, 'base':   4991.25, 'rate': pct(25) },
        { 'over':   8925, 'base':    892.50, 'rate': pct(15) },
        { 'over':      0, 'base':         0, 'rate': pct(10) },
    ]

    tax_total += find_tax_liability(federal_tax_bracket, federal_agi)

    # FICA 
    # http://www.irs.gov/taxtopics/tc751.html

    # 1.45% Medicare
    tax_total += (federal_agi * pct(1.45)) 

    # 6.2% SSA (up to the wage base of 113700)
    wage_base = 113700
    if federal_agi >= wage_base:
        tax_total += (wage_base * pct(6.2))
    else:
        tax_total += (federal_agi * pct(6.2))

    return round(tax_total, 2)

def find_tax_liability(bracket, taxable_income):
    # Given a sorted tax bracket, loop through the list and select the first  (and thus highest) liable bracket.
    # The 'bracket' argument is a sorted list of dictionaries representing levels in a tax bracket.
    # Each bracket row has the following keys: 
        # 'over': a maximum applicable income to the preceding bracket
        # 'base': in the bracket is the sum of income liabilities for each preceding bracket.  This is used as an optimization. 
        # 'rate': the tax rate, a decimal multiplier, to which income in this bracket is to be taxed.
    for i in bracket:
        if taxable_income > i['over']:
            return i['base'] + ( i['rate'] * ( taxable_income - i['over'] ) )
