from backend_testing import backend_testings_func
from frontend_testing import frontend_testings_func


def combined_testing_func(user_id, username):
    backend_testings_func(user_id, username)
    user_name = frontend_testings_func(user_id)
    assert username == user_name


if __name__ == '__main__':
    combined_testing_func(8, 'carl')

