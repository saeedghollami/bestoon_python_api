import requests

class Url:
    BASE_URL = 'http://bestoon.ir'
    SUBMIT_EXPENSE = BASE_URL + '/submit/expense'
    SUBMIT_INCOME = BASE_URL + '/submit/income'
    STATS = BASE_URL + '/q/generalstat'
    
    

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
            expenses = response.json()['expense']
            content = f'Total of Expenses: {expenses.get("amount__sum")}\n' \
                      f'Number of Expenses: {expenses.get("amount__count")}'
            return content
        else:
            return 'Connection Failed! '+ str(response.status_code)
    
    
class Income:
    def __init__(self, token):
        self.token = token
        
    def add(self, **kwargs):
        pass
    
    def edit(self, **kwargs):
        pass
    
    def stat(self, **kwargs):
        pass
    
    
if __name__ == '__main__':
    exp = Expense(token='DnjeBhgRBvjDk9YbnDxEwCZvN7GJUUgama3i5nna0VpABQX9')
    r = exp.stats()
    print(r)
