from database import db_clean

def get_clean_page(page: int, page_size: int = 10):
    
    if page < 0:
        page = 0
    if page_size <= 0:
        page_size = 10

    offset = page * page_size
    return db_clean.search_clean_paginated(limit=page_size, offset=offset)

def get_clean_total():
    return db_clean.count_clean()

def get_clean():
    return db_clean.search_clean()

def post_clean(date, price, quantity, unitPrice, status, clientID):
    return db_clean.insert_clean(date, price, quantity, unitPrice, status, clientID)

def delete_clean(clean_id):
    return db_clean.remove_clean(clean_id)