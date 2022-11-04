from flask import Flask, flash
from flask_app.config.mysqlconnection import connectToMySQL

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_boxes = data['num_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (customer_name, cookie_type, num_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_boxes)s)"
        return connectToMySQL('cookies_schema').query_db(query, data)
    
    @classmethod
    def get_all_orders(cls):
        query = "SELECT * FROM orders;"
        return connectToMySQL('cookies_schema').query_db(query)
    
    @classmethod
    def get_one_order(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s;"
        return connectToMySQL('cookies_schema').query_db(query, data)
    
    @classmethod
    def update(cls, data):
        query = """UPDATE orders 
                    SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, num_boxes = %(num_boxes)s 
                    WHERE id = %(id)s;"""
        return connectToMySQL('cookies_schema').query_db(query, data)
    
    @staticmethod
    def validate(data):
        print(data)
        is_valid = True
        if len(data['customer_name']) < 1:
            flash('Please complete the name field')
            is_valid = False
        if len(data['cookie_type']) < 1:
            flash('Please complete the cookie field')
            is_valid = False
        if len(data['num_boxes']) < 1:
            flash('Please order at least one box')
            is_valid = False
        if len(data['num_boxes']) >= 1:
            if int(data['num_boxes']) < 1:
                flash('Please order at least one box')
                is_valid = False
        return is_valid