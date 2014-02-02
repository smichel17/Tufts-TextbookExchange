from bottle import run, route, static_file
import bottle.ext.sqlite, sqlite3



db = sqlite3.connect('models/offers.db')
c = db.cursor()
c.execute("SELECT id, department, course_number, price, description, email FROM offers")
data = c.fetchall()
c.close()
    
@route('/')
def show_index():
    return static_file('index.html', root="/views")



run(host='localhost', port=8080)