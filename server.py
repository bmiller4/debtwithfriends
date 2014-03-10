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
  
@app.route('/newDebt')
def newDebtIndex():
    return render_template('addADebt.html', selectedMenu = 'NewDebt')

@app.route('/FriendsInDebt')
def friendDebtIndex():
    return render_template('FriendDebt.html', selectedMenu = 'FriendsInDebt')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)