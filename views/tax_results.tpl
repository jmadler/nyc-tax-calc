% rebase('base.tpl', title='NYC Tax Calculator')
Residence: {{residence}} 
Deduction: {{deduction}}
Gross: {{gross}}
Tax: {{tax}}
Net: {{gross-tax}}
Tax Rate: {{(tax/gross) * 100}}
