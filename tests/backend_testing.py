import requests
from pypika import Table, Query

import db_connector
from model import users

connector = users.connector


def backend_testings_func(user_id, user_name):
    url = f"http://127.0.0.1:5000/users/{user_id}"
    try:
        post_request = requests.post(
            url,
            json={
                "user_name": user_name.lower()
            }
        )
        if post_request.ok:
            print(post_request.json())
        else:
            post_res_dict = post_request.json()
            print("error: cannot post new request", post_res_dict['reason'],
                  "status code:", post_request.status_code)

    except requests.exceptions.ConnectionError as reqExecConErr:
        print(reqExecConErr, "\n\nDoes rest_app.py is running?")

    get_request = requests.get(url)
    get_response_user_name = get_request.json()['user_name']

    if get_response_user_name == user_name \
            and (get_request.status_code == 200
                 or get_request.status_code == 201):
        print("works like expected", get_response_user_name, "equal to:", user_name,
              "\nstatus code is: ", get_request.status_code)
    else:
        print("Error:", get_response_user_name, "is not equal to:", user_name)

    get_user_from_db = Query.from_(users.users_table).select('*').where(
        users.users_table.user_id == user_id).where(
        users.users_table.user_name == user_name)

    get_user_from_db = get_user_from_db.get_sql(quote_char=None)

    try:

        row_tuple = connector.execute_one(get_user_from_db)

        db_user_id = row_tuple[0]
        db_user_name = row_tuple[1]

        if db_user_name == user_name and db_user_id == user_id:
            print("John is stored in his favor place...\n"
                  "db user_id:", db_user_id, "\ndb_user_name:", db_user_name)

    except UnboundLocalError as Err:
        print("\nJohn is looking for another place.")
        print("Error:", Err)

if __name__ == '__main__':
    backend_testings_func(7, "bob")
