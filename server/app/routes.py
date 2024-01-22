from app import app

@app.route('/api/hello')
def hello():
    return {'message': 'Hello from Flask!'}