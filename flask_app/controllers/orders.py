from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import order

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def cookies():
    all_orders = order.Order.get_all_orders()
    return render_template('cookies.html', all_orders=all_orders)

@app.route('/cookies/new')
def new_order():
    return render_template('new_order.html')

@app.route('/cookies/new/create', methods=['POST'])
def create_order():
    data = {
        'customer_name': request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes': request.form['num_boxes']
    }
    is_valid = order.Order.validate(data)
    if is_valid == True:
        order.Order.save(data)
        return redirect('/cookies')
    return redirect('/cookies/new')

@app.route('/cookies/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    one_order = order.Order.get_one_order(data)
    print(one_order)
    return render_template('edit.html', one_order=one_order[0])

@app.route('/log', methods=['POST'])
def update():
    data = {
        'id' : request.form['id'],
        'customer_name' : request.form['customer_name'],
        'cookie_type': request.form['cookie_type'],
        'num_boxes' : request.form['num_boxes']
    }
    is_valid = order.Order.validate(data)
    if is_valid == True:
        order.Order.update(data)
        return redirect('/cookies')
    return redirect('/cookies/edit/' + data['id'])