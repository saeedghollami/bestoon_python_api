

import requests
import json

class Url:
    BASE_URL = 'http://bestoon.ir'
    SUBMIT_EXPENSE = BASE_URL + '/submit/expense/'
    GET_EXPENSES = BASE_URL + '/q/expenses/'
    SUBMIT_INCOME = BASE_URL + '/submit/income/'
    GET_INCOMES = BASE_URL + '/q/incomes/'
    STATS = BASE_URL + '/q/generalstat/'
    LOGIN = BASE_URL + '/accounts/login/'
    REGISTER = BASE_URL + '/accounts/register/'
    WHOAMI = BASE_URL + '/accounts/whoami/'
   
    
class Account:
    """ 
        Manage User Account
        To use Account you have to register from the offical website at
        http://www.bestoon.ir/register
     """
        
    def login(self, username, password):
        """ 
        Login to the account with specifying username and password


        Parameters:
        -----------
        username: str 
            The username which entered at the registeration.
        password: str 
            The password which entered at the registeration.

        
        Returns:
        -------
        out:
            if login was successful -> {'token': 'yourtoken', 'status' = 'ok'}
            if user wasn't exist -> 404
            if password was wrong -> {'status': 'error'}


        Examples:
        ---------
        >>> account = Account()

        >>> response = account.login(username='tempuser', password='temppass')
        >>> response
        {'token': '5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV', 'result': 'ok'}

        >>> wrong_pass_acc = account.login(username='tempuser', password='wrongpass')
        >>> wrong_pass_acc
        'Password is incorrect'

        >>> wrong_user_acc = account.login(username='usernotexist', password='wrongpass')
        >>> wrong_user_acc
        '404 User Not Found'
        """
        data = {'username': username, 'password': password}
        response = requests.post(Url.LOGIN, data=data)
        if  response.status_code == 200 and response.json()['result'] == 'ok':
            return response.json()
        elif  response.status_code == 200 and response.json()['result'] == 'error':
            return 'Password is incorrect'
        elif response.status_code == 404:
            return '404 User Not Found'
        else:
            return response.status_code
        
        return response.status_code  
    

    def whoami(self, token):
        """
            Findout username with specifying token

        Parameters:
        -----------
        token: str 
            The token which recived after registeration.

        Returns:
        --------
        out:
            if token was correct -> {'user': 'yourusername'}
            if token wan't correct -> 404

        Examples:
        ---------
        >>> account = Account()
        
        >>> response = account.whoami(token='5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV')
        >>> response
        {'user': 'tempuser'}

        >>> response = account.whoami(token='this token is not valid')
        >>> response
        '404 Token not Found'

        """
        data = {'token': token}
        response = requests.post(Url.WHOAMI, data=data)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return '404 Token not Found'
        else:
            return response.status_code

    
class Expense:
    def __init__(self, token=''):
        self.token = token
        
    def _check_response(self, response):
        return response.status_code == 200
    
    def add(self, **kwargs):
        kwargs['token'] = self.token  # add token to data
        response = requests.post(Url.SUBMIT_EXPENSE, data=kwargs)
        if self._check_response(response) and response.json()['status'] == 'ok':
                return 'Added Successfuly.  :-)'
        else:
            return 'Connection Failed! '+ str(response.status_code)
            
    
    def edit(self, **kwargs):
        return 'Not Implemented yet!'
    
    def stats(self):
        data = {'token': self.token}
        response = requests.post(Url.STATS, data=data)
        if self._check_response(response):
            content = response.json()['expense']
            return content
        else:
            return 'Connection Failed! '+ str(response.status_code)
        
    def get_expenses(self, number=10):
        data = {'token': self.token, 'number': number}
        response = requests.post(Url.GET_EXPENSES, data=data)
        if self._check_response(response):
            content = json.loads(response.json())
            return content
        else:
            return 'Problem' + str(response.status_code)

    
class Income:
    def __init__(self, token):
        self.token = token
    def _check_response(self, response):
        return response.status_code == 200
        
    def add(self, **kwargs):
        kwargs['token'] = self.token  # add token to data
        response = requests.post(Url.SUBMIT_INCOME, data=kwargs)
        if self._check_response(response) and response.json()['status'] == 'ok':
                return 'Added Successfuly.  :-)'
        else:
            return 'Connection Failed! '+ str(response.status_code)
    
    def edit(self, **kwargs):
        pass
    
    def stats(self, **kwargs):
        data = {'token': self.token}
        response = requests.post(Url.STATS, data=data)
        if self._check_response(response):
            content = response.json()['income']
            return content
        else:
            return 'Connection Failed! '+ str(response.status_code)
    
    def get_incomes(self, number=10):
        data = {'token': self.token, 'number': number}
        response = requests.post(Url.GET_INCOMES, data=data)
        if self._check_response(response):
            content = json.loads(response.json())
            return content
        else:
            return 'Problem' + str(response.status_code)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # account = Account()
    # response = account.whoami(token='this token is not valid')
    # print(response)
