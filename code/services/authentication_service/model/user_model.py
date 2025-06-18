from pydantic import BaseModel


class UserModel(BaseModel):
    ID_USER: str
    NAME: str
    EMAIL: str
    PASSWORD: str

    def check_password(self, password: str) -> bool:
        return self.PASSWORD == password