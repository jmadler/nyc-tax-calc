% rebase('base.tpl', title='NYC Tax Calculator')
<h1>2013 NYC Tax Calculator</h1>
<p>Here's a quick and easy way to calculate your net take-home pay and tax rate if you live and/or work in NYC</p>

<form action="/results" method="get">
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
            <input type="text" id="deduction" name="deduction" value="5800" />
        </div>
% if defined('invalid') and 'gross' in invalid:
        <div class="question invalid">
% else:
        <div class="question">
% end
            <label for="gross" class="question">Taxable Income (AGI)</label>
            <input type="text" id="gross" name="gross" />
        </div>
        <input type="submit" class="" />
    </fieldset>
</form>
