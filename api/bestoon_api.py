'''username: tempuser
token: 5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV
password: tempuser
email: tempuser@tempmail.com

BUG: In login part if you send wrong token it will work!
     the wrost part is it return the valid token!
     so if you guess the username and password you can get the token
     which not possiable in most cases.

TODO: Check the kwargs keys to be valid keys.

I think I'm blocked!
'''
'''
token=mg1mQ2cVOgo2Dv2cPCEFDkVzOHRql4htrm3kmYMk4zB1W7wb
username=nobody
email=nobody@nobody.com
password=nobody
'''

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
    def __init__(self):
        pass
        
    def login(self, username, password):
        data = {'username': username, 'password': password}
        response = requests.post(Url.LOGIN, data=data)
        return response.json()
    
    def register(self, **kwargs):
        ''' No api method implemented!
        Users have to register in the offical website.
        '''
        pass
    
    def whoami(self, token):
        ''' pass the token and findout username
            input: token
            output: username
        '''
        data = {'token': token}
        response = requests.post(Url.WHOAMI, data=data)
        return response.json()

    
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
    token='5YrZnB8Z6IwZSTwsv3PwoE2jtP8QSiWONvfso7wvbS9mdNSV'
    acc = Account()
    re = acc.whoami(token)
    print(re)
