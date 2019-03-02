
## Bestoon Project

Bestoon is an open source project which let to manage your inocmes and expenses. It has many clients like command line,
desktop client, Telegram roboat, mobile client and many more. 
for more information check out the [bestoon github page.](https://github.com/jadijadi/bestoon)

## How Bestoon Python API Works
The API interact with the offical website with sending request and getting a json file. 

## How to use it
This API need a token to work with it. To get a token you have to go to [http://bestoon.ir/register](bestoon.ir/register) to create an account, then you get a token.
You can create objects from Income or Expense classes to manage your incomes and expenses. When you create objects form these classes you have to pass the token. here are some examples.

```python
# manage you incomes
income = Income(token='token is 48 random string get it from bestoon.ir/register/')

# add an income
r = income.add(text='from some where', amount=1000)
print(r)  # ---> Added Successfuly.  :-)

# Get information about your incomes (how much money your earned and how many income you added until now)
r = income.stats()
print(r)  # --> {'amount__sum': 1000, 'amount__count': 1}

# Get the info about lates incomes (defualt is 10)
r = income.get_incomes()
print(r)  # --> [{'model': 'web.income', 'pk': 417, 'fields': {'text': 'from some where', 'date': '2019-03-01T12:49:10.650Z', 'amount': 1000, 'user': 839}}]
```
> Note1: Same above methods impelement for Expense class too.
        
> Note2: Currently you cannot register with the api but you can login with your username and password which api return user's token and status:ok. 

> Note3: You can findout your username with passing your token to whoami method in the Account class

