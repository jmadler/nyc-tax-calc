% rebase('base.tpl', title='NYC Tax Calculator')
<h1>Hi there!</h1>
<p>Here's a quick and easy way to calculate your net take-home pay and tax rate if you live and/or work in NYC</p>

<form action="/results" method="get">
    <fieldset>
        <div class="question">
            <label for="live_in" class="question">Residence</label>
            <select id="live_in">
                <option name="NYC">NYC (Year-round)</option>
                <option name="NYS">New York State (other than NYC)</option>
                <option name="NJ">New Jersey</option>
                <option name="CT">Connecticut</option>
            </select>
        </div>
        <div class="question">
            <label for="deduction" class="question">Deduction</label> 
            <input type="text" id="deduction" value="5800" />
        </div>
        <div class="question">
            <label for="gross" class="question">Taxable Income (AGI)</label>
            <input type="text" id="gross" />
        </div>
        <input type="submit" class="" />
    </fieldset>
</form>
