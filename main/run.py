from bottle import run, route
import bottle.ext.sqlite, sqlite3



db = sqlite3.connect('models/offers.db')
c = db.cursor()
c.execute("SELECT id, department, course_number, price, description, email FROM offers")
data = c.fetchall()
c.close()
    
print(data[0][4])

@route('/')
def show_picnic():
    print("hello")

    db = sqlite3.connect('models/picnic.db')
    c = db.cursor()
    c.execute("SELECT item,quant FROM picnic")
    data = c.fetchall()
    c.close()
    
    output = template("views/make_table", rows=data)


    return output



#run(host='localhost', port=8080)