#!/usr/bin/env python
from bottle import Bottle, template, request
from nyctax import tax_calc

bottle = Bottle()

def valid_home(value):
    permitted = ['NYS', 'NYC', 'CT', 'NJ']
    if value in permitted:
        return value
    else:
        raise Exception

def valid_int(value):
    if value.isdigit and int(value) >= 0:
        return float(value)
    else:
        raise Exception

@bottle.route('/')
def index():
    return template('tax_form')

@bottle.route('/results')
def tax_results():
    params = {
        'gross' : valid_int,
        'deduction' : valid_int,
        'residence' : valid_home,
    }
    invalid = []
    tax_results = {}
    for i in params:
        if request.params.get(i):
            try:
                tax_results[i] = params[i](request.params.get(i))
            except Exception:
                invalid.append(i)
        else:
            invalid.append(i)
    if invalid:
        return template('tax_form', invalid=invalid)
    else:
        try: 
            tax_results['tax'] = tax_calc(**tax_results)
        except Exception:
            raise
        return template('tax_results', **tax_results)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'

