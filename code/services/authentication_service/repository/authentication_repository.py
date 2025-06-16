from utils.csv_service import CSVService
from typing import List
from services.authentication_service.model.user_model import UserModel  

class AuthenticationRepository:
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
        return user.ID_USER

    def _get_users(self):
            users = CSVService().read_csv('repositories/users', 'users.csv')
            return [UserModel(**user) for user in users]

    def _write_users(self, users: List[UserModel]):
        CSVService().write_csv('repositories/users', 'users.csv', [user.model_dump() for user in users], header=['ID_USER', 'NAME', 'EMAIL', 'PASSWORD'])