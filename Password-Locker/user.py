class User:
    """
    Class that generates new instances of users
    """

    user_list = []
    def save_user(self):
        '''
        save_user method saves contact objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)   
 

    def __init__(self, first_name, last_name, user_name, password):
        '''
        init__helps us to define our users' properties.
        Args:
            first_name: New contact first name.
            last_name: New contact last name.
            user_name: New user's login username.
            password: New user's login password   
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
    @classmethod
    def find_by_user_name(cls,user_name):   
        '''
        Method that takes in a number and returns a contact that matches that number.
        Args:
        user_name:user_name to search for
        Returns:
        Users of person that matches the user_name.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user
    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        
        Args:
        user_name: User_name to search if it exists 
        Returns:
        Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True

        return False