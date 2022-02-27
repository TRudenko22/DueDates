import yaml
import datetime
from datetime import date

# Sets todays date.
dt = datetime.datetime
today = datetime.datetime.today()
today_delta = date(year=today.year, month=today.month, day=today.day)

# Pulls in the YAML file.
with open("assign.yml", "r") as file:
    due_dates = yaml.safe_load(file)


cs_date = due_dates['cSharp']
net_date = due_dates['Net1']
win_date = due_dates['Windows']

# assigns the value from the 'due' key and parses it as a date 
cDue = datetime.datetime.strptime(cs_date[0]['due'], '%m/%d/%Y').date()
nDue = datetime.datetime.strptime(net_date[0]['due'], '%m/%d/%Y').date()
wDue = datetime.datetime.strptime(win_date[0]['due'], '%m/%d/%Y').date()

print(f"You have some C# assignments due in {str(cDue - today_delta).split(', ')[0]}\n")
[print('  -  ', x) for x in cs_date[0]['task'].split(' ')]
print('\n')

print(f"You have some Network assignments due in {str(nDue - today_delta).split(', ')[0]}\n")
[print('  -  ', x) for x in net_date[0]['task'].split(' ')]
print('\n')

print(f"You have some Windows assignments due in {str(wDue - today_delta).split(', ')[0]}\n")
[print('  -  ', x) for x in win_date[0]['task'].split(' ')]
print('\n')
#
#cSharp = []
#for item in due_dates["cSharp"]:
#    date = datetime.datetime.strptime(item['due'], '%m/%d/%Y').date()
#    print(f"""
#    Due : {str(date - today_delta).split(', ')[0]}
#    Date : {date.strftime('%m/%d/%Y')}
#    Task : {item['task']}
#          
#    """)
