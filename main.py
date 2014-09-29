from bottle import Bottle, template, request

def valid_home(value):
    permitted = ['NYS', 'NYC', 'CT', 'NJ']
    if value in permitted:
        return value
    else:
        raise

def valid_int(value):
    if value == int(val):
        return value
    else:
        raise


bottle = Bottle()

@bottle.route('/')
def index():
    return template('tax_form')

@bottle.route('/results/')
def tax_calc():
    params = {
        'gross' : valid_integer,
        'deduction' : valid_integer,
        'live_in' : valid_home,
    }
    tax_params = {}
    for i in request.params:
        if params[i]:
            try:
                tax_params[i] = params[i](request.params[i])
            except Exception:
                pass
#    results = tax_calc(tax_params)
    return template('tax_results', tax_params)

# Define an handler for 404 errors.
@bottle.error(404)
def error_404(error):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.'

