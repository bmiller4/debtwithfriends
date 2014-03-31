from flask import Flask, render_template, request, url_for, session, redirect
import utils
import MySQLdb

app = Flask(__name__)

app.secret_key = 'NOPE'
currentUser = ''

@app.route('/', methods = ['GET', 'POST'])
def homePage():
  global currentUser
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  # if user typed in a post ...
  if request.method == 'POST':
		print "HI"
		session['username'] = MySQLdb.escape_string(request.form['username'])
		currentUser = session['username']
		session['pw'] =  MySQLdb.escape_string(request.form['pw'])
		query = "select * from user_list WHERE username = '%s' AND password = '%s'" % (session['username'], session['pw'])
		print query
		cur.execute(query)
		if cur.fetchone():
			cur1 = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
			cur1.execute("select friend_user, friend_totalD from friend_list join user_list join friends ON user_list.id = friends.user_id AND friends.friend_id = friend_list.id WHERE username = '%s'"%(session['username']))
			rows = cur1.fetchall()
			cur2 = db.cursor(cursorclass = MySQLdb.cursors.DictCursor)
			cur2.execute("select username, total_debt from user_list WHERE username = '%s'" % (currentUser))
			rows2 = cur2.fetchall()
			db.commit()
			return render_template('index.html', username = currentUser, friend_list = rows, user_list = rows2)


  return render_template('login.html', username = currentUser)
  #db = utils.db_connect()
  #cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  #display debts
  #cur.execute('SELECT * FROM user_list')
  #rows2 = cur.fetchall()
  #cur.execute('SELECT * FROM main_list')
  #rows = cur.fetchall()
  
  
  #return render_template('index.html', main_list=rows, user_debt=rows2, selectedMenu = 'Home')

@app.route('/addaDebt')
def addDebtIndex():
    return render_template('addaDebt.html', selectedMenu = 'NewDebt')

@app.route('/addFriend', methods = ['POST', 'GET'])
def addFriendIndex(): 
		if currentUser == '':
			return render_template('login.html')
		return render_template('addfriend.html', selectedMenu = 'addFriend')
    

@app.route('/addFriend2', methods = ['POST', 'GET'])
def addFriendIndex2():
		db = utils.db_connect()
		cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
		if request.method == 'POST':
			query = "INSERT INTO friend_list select id, username, total_debt from user_list WHERE username = '%s'" % (request.form['friend_user'])
			print query
			cur.execute(query)
			db.commit()
		return render_template('addfriend2.html', selectedMenu = 'addFriend')		
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
	
		query = "INSERT INTO user_list (username, password, total_debt) VALUES ('%s', '%s', 0)" % (un, pw)
		cur.execute(query)
		db.commit()
		if cur.fetchone():
			return redirect(url_for('mainIndex')) 
  return render_template('register2.html', selectedMenu='Register')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)