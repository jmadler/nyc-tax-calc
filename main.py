#!/usr/bin/env python
from bottle import Bottle, template, request

bottle = Bottle()

def valid_home(value):
    permitted = ['NYS', 'NYC', 'CT', 'NJ']
    if value in permitted:
        return value
    else:
        raise Exception

def valid_int(value):
    if value == int(value) and int(value) >= 0:
        return value
    else:
        raise Exception

@bottle.route('/')
def index():
    return template('tax_form')

@bottle.route('/results')
def tax_calc():
    params = {
        'gross' : valid_int,
        'deduction' : valid_int,
        'residence' : valid_home,
    }
    tax_params = {}
    invalid = []
    for i in params:
        if request.params.get(i):
            try:
                tax_params[i] = params[i](request.params.get(i))
            except Exception:
                pass
        else:
            invalid.append(i)
    if invalid:
        return template('tax_form', invalid=invalid)
    else:
        #results = tax_calc(tax_params)
        return template('tax_results', tax_params)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'
