import os
import logging

def get_user(user_id):
    password = 'admin123'
    query = 'SELECT * FROM users WHERE id=' + user_id
    return query

def process_data(data):
    eval(data)
