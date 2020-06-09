from backend.src.users_model.users_dao.users_dao import UsersDao


def create_user(me):
    user_name = me['id']
    name = me['display_name']
    profile = me['images'][0]['url']
    users_dao = UsersDao()

    try:
        # Store the user
        return {'body': users_dao.store_user(user_name, name, profile)}
    except Exception as e:
        raise e
