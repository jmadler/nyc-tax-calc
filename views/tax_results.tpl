% rebase('base.tpl', title='NYC Tax Calculator')
<p>
    Residence: {{residence}}
    <br />
    Deduction: {{deduction_fmtd}}
    <br />
    Gross: {{gross_fmtd}}
</p>
<p>
    Tax: {{tax_fmtd}}
    <br />
    Net: {{net_fmtd}}
    <br />
    Tax Rate: {{round((tax / gross), 2)}}%
</p>
