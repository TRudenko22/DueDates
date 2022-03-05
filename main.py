import yaml
import datetime
from datetime import date


sDate = lambda index: datetime.datetime\
        .strptime(index, '%m/%d/%Y').date()


# Sets todays date.
today = datetime.datetime.today()
today_delta = date(year=today.year, month=today.month, day=today.day)


# Pulls in the YAML file.
with open("assign.yml", "r") as file:
    due_dates = yaml.safe_load(file)


cs_date = due_dates['cSharp']
net_date = due_dates['Net1']
win_date = due_dates['Windows']


# assigns the value from the 'due' key and parses it as a date 
cDue = sDate(cs_date[0]['due'])
nDue = sDate(net_date[0]['due'])
wDue = sDate(win_date[0]['due'])

CS_DueDate = str(cDue - today_delta).split(', ')[0]
NW_DueDate = str(nDue - today_delta).split(', ')[0]
W_DueDate = str(wDue - today_delta).split(', ')[0]

print(f"You have some C# assignments due in {CS_DueDate}\n")

[print('  -  ', x) for x in cs_date[0]['task'].split(' ')]
print('\n')

print(f"You have some Network assignments due in {NW_DueDate}\n")

[print('  -  ', x) for x in net_date[0]['task'].split(' ')]
print('\n')

print(f"You have some Windows assignments due in {W_DueDate }\n")

[print('  -  ', x) for x in win_date[0]['task'].split(' ')]
print('\n')

