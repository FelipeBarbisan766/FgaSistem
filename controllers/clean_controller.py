import database.db_clean as db_clean    

def get_cleans():
    cleans = db_clean.search_cleans()
    return cleans