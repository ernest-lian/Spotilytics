from backend.src.user_model.user_dao.user_dao import UserDao


class UserModel:
    @staticmethod
    def create_user(me):
        user_name = me['id']
        name = me['display_name']
        profile = me['images'][0]['url']

        try:
            return {'status_code': 200, 'body': UserDao.create_connection(user_name, name, profile)}
        except Exception as e:
            raise e
