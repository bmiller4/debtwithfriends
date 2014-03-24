from flask import Flask, render_template, request
import utils
import MySQLdb

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homePage():
  
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
  #display debts
  cur.execute('SELECT * FROM user_list')
  rows2 = cur.fetchall()
  cur.execute('SELECT * FROM main_list')
  rows = cur.fetchall()
  
  
  return render_template('index.html', main_list=rows, user_debt=rows2, selectedMenu = 'Home')

@app.route('/addaDebt')
def addDebtIndex():
    return render_template('addaDebt.html', selectedMenu = 'NewDebt')
  
@app.route('/addaDebt2', methods=['POST'])
def newDebtIndex():
    query = "INSERT INTO friend_debt (friend_lastname, debt_amount, description) VALUES ('";
    query += request.form['friend_lastname'] + "', '" + request.form['debt_amount'] + "', '" + request.form['description'] + "')"
    #query2 = "UPDATE main_list SET total_debt = total_debt + " + request.form['debt_amount'] + " WHERE lastname = " + request.form['friend_lastname']
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(query)
    #cur.execute(query2)
    db.commit()
    return render_template('addaDebt2.html', selectedMenu = 'NewDebt')

@app.route('/friendDebt')
def friendDebtIndex():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    query1 = 'SELECT * FROM friend_debt'
    cur.execute(query1)
    rows = cur.fetchall()
    db.commit()
    return render_template('friendDebt.html', selectedMenu = 'FriendsInDebt',friend_debt=rows)
@app.route('/register', methods=['GET', 'POST'])
def register():
	return render_template('register.html', selectedMenu='Register')

@app.route('/register2',methods=['GET','POST'])
def register2():
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  if request.method == 'POST':
		un = MySQLdb.escape_string(request.form['username'])
		pw = MySQLdb.escape_string(request.form['pw'])
	
		query = "INSERT INTO user_list (username, password, 0) VALUES ('%s', '%s')" % (un, pw)
		cur.execute(query)
		db.commit()
		if cur.fetchone():
			return redirect(url_for('mainIndex')) 
  return render_template('register2.html', selectedMenu='Register')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)