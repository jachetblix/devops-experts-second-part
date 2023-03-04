from flask import jsonify, request
from pypika import Query, Table, Field
from db_connector import DBConnector
from datetime import datetime
import time
from config import config



users_table = Table('users')
is_connected = False
while not is_connected:
    try:
        connector = DBConnector(
            host=config.get('MYSQL_HOST'),
            user=config.get('MYSQL_USER'),
            password=config.get('MYSQL_PASSWORD'),
            database=config.get('MYSQL_DATABASE')
        )
        is_connected = True
        print('connected')
    except Exception as e :
        print(e)
        time.sleep(1)
        print('not connected')


def get_user(user_id):
    query = Query.from_(users_table).select(users_table.user_name).where(users_table.user_id == int(user_id))
    return connector.execute_one(query.get_sql(quote_char=None))


def create_user(user_id, user_name):
    query = Query.into(users_table).columns(users_table.user_id, users_table.user_name, users_table.creation_date) \
        .insert(user_id, user_name, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return connector.execute_one(query.get_sql(quote_char=None))


def update_user(user_id, user_name):
    query = Query.update(users_table).set(users_table.user_name, user_name).where(users_table.user_id == int(user_id))
    return connector.execute_one(query.get_sql(quote_char=None))


def delete_user(user_id):
    query = Query.from_(users_table).where(users_table.user_id == int(user_id)).delete()
    return connector.execute_one(query.get_sql(quote_char=None))
