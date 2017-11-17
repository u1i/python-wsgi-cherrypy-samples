from bottle import Bottle, request

app = Bottle()

@app.get('/stuff')
def do_stuff():

    stuff = {'data': '1234'}
   
    return stuff
