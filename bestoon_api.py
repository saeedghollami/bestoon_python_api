

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
    """ Manage expeses """
    def __init__(self, token=''):
        """ 
        Initialize a expense object 

        Parameters:
        -----------
        token: str 
            48 random charcter string, provided after registeration.

        Returns:
        --------
        out: an expense object
            if token was not valid -> 404

        """
        self.token = token
    
    def add(self, **kwargs):
        """
        Add an expense to expenses
        
        Parameters:
        -----------
        amount: int
            the money that user expesed. defualt is 0
        text: str
            discription of the expese. default is empty string
        data: Datetime
            the datetime of the expese, optional, defualt is today datetime
            
        Returns:
        --------
        out: {'status': 'ok'}

        Examples:
        ---------

        >>> expense = Expense(token='5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV')
        >>> r = expense.add(amount=12000, text='some expense')
        >>> r
        {'status': 'ok'}

        """
        kwargs['token'] = self.token  # add token to data
        response = requests.post(Url.SUBMIT_EXPENSE, data=kwargs)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
    
    def stats(self):
        """
        Returns sum of amount and number of amount expense
        
        Parameters:
        -----------
            
        Returns:
        --------
        out: dict
            returns -> {'amount__sum': 123, 'amount__count': 123}

        Examples:
        ---------

        """

        data = {'token': self.token}
        response = requests.post(Url.STATS, data=data)

        if response.status_code == 200:
            return response.json()['expense']
        else:
            return response.status_code
        
    def get_expenses(self, number=10):
        """
        Returns list of latest expenses, if number not provided defualt is 10
        
        Parameters:
        -----------
        number: int
            number of expenses to query them, defualt: 10
            
        Returns:
        --------
        out: list of dict
            if token was not valid -> 404

        Examples:
        ---------

        """
        data = {'token': self.token, 'number': number}
        response = requests.post(Url.GET_EXPENSES, data=data)
        if response.status_code == 200:
            return json.loads(response.json())
        else:
            return response.status_code

    
class Income:
    """ Manage Incomes"""
    def __init__(self, token):
        """ 
        Initialize a income object 

        Parameters:
        -----------
        token: str 
            48 random charcter string, provided after registeration.

        Returns:
        --------
        out: an income object
            if token was not valid -> 404

        Examples:
        ---------
        >>> income = Income(token='5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV')
        """
        self.token = token
        
    def add(self, **kwargs):
        """
        Add an income to incomes
        
        Parameters:
        -----------
        amount: int
            the money that user expesed. defualt is 0
        text: str
            discription of the expese. default is empty string
        data: Datetime
            the datetime of the expese, optional, defualt is today datetime
            
        Returns:
        --------
        out: {'status': 'ok'}

        Examples:
        ---------

        >>> income = Income(token='5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV')
        >>> r = income.add(amount=12000, text='some income')
        >>> r
        {'status': 'ok'}

        """
        kwargs['token'] = self.token  # add token to data
        response = requests.post(Url.SUBMIT_INCOME, data=kwargs)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    
    def stats(self):
        """
        Returns sum of amounts and number of amounts for all incomes
        
        Parameters:
        -----------
            
        Returns:
        --------
        out: dict

        """

        data = {'token': self.token}
        response = requests.post(Url.STATS, data=data)

        if response.status_code == 200:
            return response.json()['income']
        else:
            return response.status_code

    def get_incomes(self, number=10):
        """
        Returns list of latest incomes, if number not provided defualt is 10
        
        Parameters:
        -----------
        number: int
            number of incomes to query them, defualt: 10
            
        Returns:
        --------
        out: list of dict
            if token was not valid -> 404

        Examples:
        ---------

        """
        data = {'token': self.token, 'number': number}
        response = requests.post(Url.GET_INCOMES, data=data)

        if response.status_code == 200:
            return json.loads(response.json())
        else:
            return response.status_code
    
if __name__ == '__main__':
    """ Some Test """
    import doctest
    doctest.testmod()
    