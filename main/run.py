from bottle import run, route, static_file, request, error, get, post, redirect, template
import bottle.ext.sqlite, sqlite3, sendgrid


# SendGrid Login credentials
global username 
global password 
username = 'arloclarke'
password = "Monkey"

sg = sendgrid.SendGridClient(username, password)

offersdb = sqlite3.connect('models/offers.db')
bidsdb = sqlite3.connect('models/bids.db')

user_id=0
user_num=0
user_dep=''

@route('/')
def show_index():
    return static_file('index.html', root="views/")


@get('/sell')
def show_sell():
    return static_file('sell.html', root="views/")


@post('/sell')    
def get_sell():

    department=request.forms.get('department')
    price=request.forms.get('price')
    email=request.forms.get('email')
    description=request.forms.get('description')
    course_number=request.forms.get('course_number')

    c = offersdb.cursor()
    c.execute("INSERT INTO offers (department,course_number, price, description, email) VALUES ('"+department+"', '"+course_number+"', '"+price+"', '"+description+"', '"+str(email)+"')")
    c.close()
    redirect("/")

@get('/buy')
def show_buy():
    return static_file('buy.html', root="views/")

@post('/buy')
def get_buy():
    global user_dep
    global user_num
    user_num=request.forms.get('course_number')
    user_dep=request.forms.get('department')
    redirect('/results')

    # course_number=request.forms.get('course_number')
    # department=request.forms.get('department')
    # email=request.forms.get('email')

    # c = bidsdb.cursor()
    # c.execute("SELECT id, department, course_number, email FROM bids")
    # data = c.fetchall()
    # data[0]=department
    # data[1]=course_number
    # data[2]=email
    # c.close()



@get('/results')    
def show_results():
    global user_dep
    global user_num
    c = offersdb.cursor()

    c.execute("SELECT id, department, course_number, price, description FROM offers WHERE department LIKE \'%"+user_dep+"%\' AND course_number LIKE \'%"+user_num+"%\' ORDER BY price DESC")
    data=c.fetchall()
    c.close()
    output = template('views/results', rows=data)
    return output

@post('/results')
def get_results():
    global user_id
    user_id=request.forms.get('button') 
    redirect('/confirm')

@get('/confirm')
def show_confirm():
    return static_file('confirm.html', root='views/')

@post('/confirm')
def get_confirm():
    global user_id
    global fromEmail
    global username
    global password
    global msg
    email=request.forms.get('email') 
 
    c = offersdb.cursor()
    c.execute("SELECT department, course_number, price, description, email FROM offers WHERE id = "+user_id)
    data=c.fetchone()
    c.close()

    message = sendgrid.Mail()
    message.add_to(data[4])
    message.set_subject("Buyer for " + data[0] +" "+ str(data[1]) +" Textbook")
    message.set_text("Your textbook has been reserved on TuftsTextEx.\nPlease contact "+email+ " to set up a meeting place.\n"+str(data[0])+" "+str(data[1])+" textbook priced at "+str(data[2])+" dollars.")
    message.set_from(email)
    sg.send(message)


    c = offersdb.cursor()
    c.execute("DELETE FROM offers WHERE id = "+user_id)
    c.close()
    redirect("/")

@route('/styles/<filename>')    
def show_sell_css(filename):
    return static_file(filename,root="views/styles/")
@route('/images/<filename>')    
def show_sell_css(filename):
    return static_file(filename,root="views/images/")
@route('/scripts/<filename>')    
def show_sell_css(filename):
    return static_file(filename,root="views/scripts/")


run(host='localhost', port=8080)

