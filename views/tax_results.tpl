% rebase('base.tpl', title='NYC Tax Calculator')

<%
    deduction_fmtd  = locale.currency( deduction, grouping=True )
    gross_fmtd      = locale.currency( gross, grouping=True )
    tax_fmtd        = locale.currency( tax, grouping=True )
    net_fmtd        = locale.currency( gross - tax, grouping=True )
    tax_rate        = round((tax / gross), 2)
%>
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
    Tax Rate: {{tax_rate}}%
</p>
