from datetime import datetime
from simple_salesforce import Salesforce 
sf = Salesforce(username='deepub@gmail.com', password='Salesa@123123', security_token='g81LxOrrTz1vXNlEQnVCoTUPX', sandbox=False)
Lastname='AD Bathini'
Firstname='Bathini'
Accountcreation = sf.Account.create({'Name':Lastname})
