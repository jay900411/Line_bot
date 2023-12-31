from pymongo import MongoClient
import datetime

stockDB = 'mydb'
dbname = 'howard-good31'

def constructor_stock():
    client = MongoClient('mongodb://jay900411:Qq00451211@ac-jcnyyjh-shard-00-00.zwmifuf.mongodb.net:27017,ac-jcnyyjh-shard-00-01.zwmifuf.mongodb.net:27017,ac-jcnyyjh-shard-00-02.zwmifuf.mongodb.net:27017/?ssl=true&replicaSet=atlas-6vruxq-shard-0&authSource=admin&retryWrites=true&w=majority')
    db = client[stockDB]
    return db

def update_my_stock(user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    collect.update_many({'favorite_stock':stockNumber}, {'$set':{'condition':condition, 'price':target_price}})

def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    db = constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({'favorite_stock': stockNumber})
    if is_exit != None:
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({
            'userID': userID, 
            'favorite_stock': stockNumber, 
            'condition': condition, 
            'price': target_price, 
            'tag': 'stock', 
            'date_info': datetime.datetime.now()
        })
    return f'{stockNumber}已新增至您的股票清單'

########### show出使用者股票條件 ###############
def show_stock_setting(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    dataList = list(collect.find({'userID': userID}))
    if dataList == []: return '您的股票清單為空，請透過指令新增股票至清單中'
    content = '您清單中的選股條件為: \n'
    for i in range(len(dataList)):
        content += f"{dataList[i]['favorite_stock']} {dataList[i]['condition']} {dataList[i]['price']}\n"
    return content


