from flask import Flask, render_template, request
import utils
import MySQLdb

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def homePage():
  
  db = utils.db_connect()
  cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
  
  #display debts
  cur.execute('select * from main_list')
  rows = cur.fetchall()
  
  return render_template('index.html', main_list=rows, selectedMenu = 'Home')

@app.route('addaDebt')
def addDebt():
    query = 'UPDATE main_list SET total_debt = total_debt' + form.request(debt_amount) + 'WHERE lastname = ' + form.request(friend_lastname)
    db = util.db_connect()
    cur = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    cur.execute(query)
    db.commit()
    return render_template('addaDebt.html', selectedMenu = 'NewDebt')
  
@app.route('/addADebt2')
def newDebtIndex():
    return render_template('addADebt2.html', selectedMenu = 'NewDebt')

@app.route('/FriendDebt2')
def friendDebtIndex():
    return render_template('FriendDebt2.html', selectedMenu = 'FriendsInDebt')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)