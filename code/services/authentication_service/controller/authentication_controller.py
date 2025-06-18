from services.authentication_service.repository.authentication_repository import AuthenticationRepository
from services.authentication_service.model.user_model import UserModel


class AuthenticationController:
    def __init__(self):
        self.user_repository = AuthenticationRepository()

    def login(self, email, password):
        user = self.user_repository.find_by_email(email)
        if user and user.check_password(password):
            return user
        return None
    
    def register(self, name, email, password):
        user = UserModel(ID_USER=str(len(self.user_repository._get_users()) + 1), NAME=name, EMAIL=email, PASSWORD=password)
        return self.user_repository.create_user(user)
         
    def get_user_info(self, user_id):
        return self.user_repository.get_user_info(user_id)