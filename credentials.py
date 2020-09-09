import random
import string
from user import User


class Credentials:
    '''
    Class that generates new instances of the credentials.
    '''
    credential_list = []
    def save_credential(self):
        '''
        save_user method saves contact objects into credential_list
        '''
        Credentials.credential_list.append(self)

    
    def generate_password(stringlength=10):
        '''
        method that generates a random password
        '''
        letters = string.ascii_letters + string.digits
        gen_pass = ''.join(random.choice(letters) for i in range (stringlength))
        return gen_pass    

    def delete_credentials(self):
        '''
        delete_user method deletes a saved user from the credential_list
        '''
        Credentials.credential_list.remove(self)    

    def __init__(self, user_name, password):
      

        self.user_name = user_name
        self.password = password
    @classmethod
    def find_by_user_name(cls,user_name):   
       
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return credential
    @classmethod
    def credential_exist(cls,user_name):
    
        for credential in cls.credential_list:
            if credential.user_name == user_name:
                return True

        return False