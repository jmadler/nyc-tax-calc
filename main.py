#!/usr/bin/env python
from bottle import Bottle, template, request
from nyctax import tax_calc

bottle = Bottle()

def valid_home(value):
    permitted = ['NYC']
    if value in permitted:
        return value
    else:
        raise Exception

def valid_int(value):
    if value.isdigit and int(value) >= 0:
        return float(value)
    else:
        raise Exception

@bottle.route('/', method='GET')
def index():
    return template('tax_form')

@bottle.route('/', method='POST')
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
                # Validate the incoming parameters.
                tax_results[i] = params[i](request.params.get(i))
            except Exception:
                invalid.append(i)
        else:
            invalid.append(i)
    if not invalid and tax_results['deduction'] > tax_results['gross']:
        invalid.append('deduction', 'gross')
    if invalid:
        return template('tax_form', invalid=invalid)
    else:
        try: 
            tax_results['tax'] = tax_calc(**tax_results)
        except Exception:
            raise
        tax_results['net'] = tax_results['gross'] - tax_results['tax'];
        for i in 'deduction', 'gross', 'tax', 'net':
            tax_results[i + '_fmtd'] = '$' + '%.2f' % tax_results[i]
        return template('tax_form', **tax_results)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
