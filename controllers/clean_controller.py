import database.db_clean as db_clean 

def get_cleans():
    cleans = db_clean.search_cleans()
    return cleans

def post_clean(date, price, quantity, unitPrice, status, clientID):
    return db_clean.insert_clean(date, price, quantity, unitPrice, status, clientID)