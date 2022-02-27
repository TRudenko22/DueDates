import yaml
import datetime
from datetime import date

today = datetime.datetime.today()
today_delta = date(year=today.year, month=today.month, day=today.day)

with open("assign.yml", "r") as file:
    due_dates = yaml.safe_load(file)


cs_date = due_dates['cSharp']

#cSharp = []
#for item in due_dates["cSharp"]:
#    date = datetime.datetime.strptime(item['due'], '%m/%d/%Y').date()
#    print(f"""
#    Due : {str(date - today_delta).split(', ')[0]}
#    Date : {date.strftime('%m/%d/%Y')}
#    Task : {item['task']}
#          
#    """)
