from flask import Flask, render_template, request
import util
import MySQLdb

app = Flask(__name__)


@app.route('/')
def mainIndex():
    return render_template('index.html', selectedMenu = 'Home')
  
@app.route('/newDebt')
def newDebtIndex():
    return render_template('addADebt.html', selectedMenu = 'NewDebt')

@app.route('/FriendsInDebt')
def friendDebtIndex():
    return render_template('FriendDebt.html', selectedMenu = 'FriendsInDebt')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=3000)