@app.errorhandler(404)
def not_found(error):
    return {'error': str(error)}, 404

@app.route('/')
def index():
    return '<h3> Hello </h3>'