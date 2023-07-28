
from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast
"""
user_name = pw_input('Enter your name').title()
put_success(user_name)


age = pw_input('Enter your age', type=NUMBER)
put_warning(age)

user_password = pw_input('Enter your password', type=PASSWORD)

date = pw_input('Enter your birthday', type=DATETIME)
put_code(f'Your birthday is {date}\U0001F382')
"""
user_password = pw_input('Enter your password', type=PASSWORD)
put_success(user_password)

popup('popup', 'fffff')
put_markdown('put markdown')