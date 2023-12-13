from flask import Flask, render_template, request, redirect
import pymysql
import json
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'credentials.env')
load_dotenv(dotenv_path)

# Load encryption key from .key file
key_path = os.path.join(os.path.dirname(__file__), 'key.key')
with open(key_path, 'rb') as key_file:
    key = key_file.read()

# Decrypt the encrypted password from .env
encrypted_password = os.getenv("DB_PASSWORD")
cipher_suite = Fernet(key)
db_password = cipher_suite.decrypt(encrypted_password.encode()).decode()
#db_password = db_password_bytes.decode()

# Database connection configuration
db = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=db_password,
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

# صفحه نمایش اطلاعات
@app.route('/')
def index():
    # خواندن اطلاعات از جدول expense
    cursor.execute("SELECT * FROM expense")
    expense_data = cursor.fetchall()

    # خواندن اطلاعات از جدول income
    cursor.execute("SELECT * FROM income")
    income_data = cursor.fetchall()

    # محاسبه مجموع مقادیر iamount و eamount
    total_income = sum(row[2] for row in income_data)
    total_expense = sum(row[2] for row in expense_data)

    # محاسبه سود یا ضرر نهایی
    final_balance = total_income - total_expense

    return render_template('index.html', expense_data=expense_data, income_data=income_data,
                           total_income=total_income, total_expense=total_expense, final_balance=final_balance)

# افزودن ردیف به جدول expense
@app.route('/add_expense', methods=['POST'])
def add_expense():
    eid = request.form['eid']
    ecategory = request.form['ecategory']
    eamount = request.form['eamount']

    cursor.execute("INSERT INTO expense VALUES (%s, %s, %s)", (eid, ecategory, eamount))
    db.commit()

    return redirect('/')

# حذف ردیف از جدول expense
@app.route('/delete_expense/<string:eid>')
def delete_expense(eid):
    cursor.execute("DELETE FROM expense WHERE eid = %s", (eid,))
    db.commit()

    return redirect('/')

# افزودن ردیف به جدول income
@app.route('/add_income', methods=['POST'])
def add_income():
    iid = request.form['iid']
    icategory = request.form['icategory']
    iamount = request.form['iamount']

    cursor.execute("INSERT INTO income VALUES (%s, %s, %s)", (iid, icategory, iamount))
    db.commit()

    return redirect('/')

# حذف ردیف از جدول income
@app.route('/delete_income/<string:iid>')
def delete_income(iid):
    cursor.execute("DELETE FROM income WHERE iid = %s", (iid,))
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
