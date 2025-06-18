from utils.csv_service import CSVService
from services.authentication_service.model.user_model import UserModel  


class AuthenticationRepository:
    header = ['ID_USER', 'NAME', 'EMAIL', 'PASSWORD']
    
    def find_by_email(self, email):
        users_list = self._get_users()
        return next((user for user in users_list if user.EMAIL == email), None)
    
    def get_user_info(self, id_user: str):
        users_list = self._get_users()
        return next((user for user in users_list if user.ID_USER == id_user), None)

    def create_user(self, user: UserModel):
        users_list = self._get_users()
        users_list.append(user)
        self._write_users(users_list)
        return user

    def _get_users(self):
        rows = CSVService().read_csv('repositories/users', 'users.csv')
        users = [UserModel(**dict(zip(self.header, row))) for row in rows]
        return users

    def _write_users(self, users: list[UserModel]):
        CSVService().write_csv('repositories/users', 'users.csv', [user.model_dump().values() for user in users], header=self.header)