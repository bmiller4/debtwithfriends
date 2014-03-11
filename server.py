from flask import Flask, render_template, request
import utils
import MySQLdb

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homePage():
  
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
  #display debts
  cur.execute('SELECT * FROM main_list')
  rows = cur.fetchall()
  
  return render_template('index.html', main_list=rows, selectedMenu = 'Home')

@app.route('/addaDebt')
def addDebt():
    #query = "INSERT INTO friend_debt (friend_lastname, debt_amount, description) VALUES ('";
    #query += request.form['friend_lastname'] + "', '" + request.form['debt_amount'] + "', '" + request.form['description'] + "')"
    #query = 'UPDATE main_list SET total_debt = total_debt' + form.request(debt_amount) + 'WHERE lastname = ' + form.request(friend_lastname)
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    #cur.execute(query)
    db.commit()
    return render_template('addaDebt.html', selectedMenu = 'NewDebt')
  
@app.route('/addADebt2')
def newDebtIndex():
    return render_template('addADebt2.html', selectedMenu = 'NewDebt')

@app.route('/friendDebt')
def friendDebtIndex():
    db = utils.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    query = 'SELECT * FROM friend_debt'
    cur.execute(query)
    rows = cur.fetchall()
    db.commit()
    return render_template('friendDebt.html', selectedMenu = 'FriendsInDebt')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)