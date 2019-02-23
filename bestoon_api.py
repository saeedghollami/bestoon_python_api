import requests
import json

class Url:
    BASE_URL = 'http://bestoon.ir'
    SUBMIT_EXPENSE = BASE_URL + '/submit/expense/'
    GET_EXPENSES = BASE_URL + '/q/expenses/'
    SUBMIT_INCOME = BASE_URL + '/submit/income/'
    GET_INCOMES = BASE_URL + '/q/incomes/'
    STATS = BASE_URL + '/q/generalstat/'
    

class Expense:
    def __init__(self, token=''):
        self.token = token
        
    def _check_response(self, response):
        return response.status_code == 200
    
    def add(self, **kwargs):
        kwargs['token'] = self.token  # add token to data
        response = requests.post(Url.SUBMIT_EXPENSE, data=kwargs)
        if self._check_response(response):
            if response.json()['status'] == 'ok':
                return 'Added Successfuly.  :-)'
            else:
                return 'Some Problem had happend :-( ' + str(response.status_code)
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
        if self._check_response(response):
            if response.json()['status'] == 'ok':
                return 'Added Successfuly.  :-)'
            else:
                return 'Some Problem had happend :-( ' + str(response.status_code)
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
    exp = Expense(token='DnjeBhgRBvjDk9YbnDxEwCZvN7GJUUgama3i5nna0VpABQX9')
    inc= Income(token='DnjeBhgRBvjDk9YbnDxEwCZvN7GJUUgama3i5nna0VpABQX9')
    r = exp.get_expenses()
    s = exp.stats()
    x = inc.get_incomes(number=5)
    #print(x)
    #for item in x:
        #print(item['fields']['date'], item['fields']['text'], item['fields']['amount'])
