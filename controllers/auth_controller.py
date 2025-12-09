from database.db_auth import search_user

def login(user, password):
    search = search_user(user)
    if search is None:
        return False   
    db_user, db_password = search
    if password == db_password:
        return True   
    else:
        return False   