% rebase('base.tpl', title='NYC Tax Calculator')
<h1>2013 NYC Tax Calculator</h1>
<p>Here's a quick and easy way to calculate your net take-home pay and tax rate if you live and/or work in NYC.</p>
<p>This is a very simple calculator.  It only handles those filing singly, and doesn't handle any special cases (e.g. EITC).  I can't vouch for its accuracy, either.</p>

<form action="" method="POST">
    <fieldset>
% if defined('invalid') and 'residence' in invalid:
        <div class="question invalid">
% else:
        <div class="question">
% end
            <label for="residence" class="question">Residence</label>
            <select id="residence" name="residence">
                <option name="residence" value="NYC">New York City</option>
            </select>
        </div>
% if defined('invalid') and 'deduction' in invalid:
        <div class="question invalid">
% else:
        <div class="question">
% end
            <label for="deduction" class="question">Deduction</label> 
            <input type="text" id="deduction" name="deduction" value="{{str(int(get('deduction', 5800)))}}" />
        </div>
% if defined('invalid') and 'gross' in invalid:
        <div class="question invalid">
% else:
        <div class="question">
% end
            <label for="gross" class="question">Taxable Income (AGI)</label>
% if defined('deduction'):
            <input type="text" id="gross" name="gross" value="{{str(int(gross))}}" />
% else:
            <input type="text" id="gross" name="gross" />
% end
        </div>
        <input type="submit" class="" />
    </fieldset>
</form>

% if not defined('invalid') and defined('tax_fmtd'):

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
    Tax Rate: {{round( 100 * (tax / gross), 2)}}%
</p>

% end
