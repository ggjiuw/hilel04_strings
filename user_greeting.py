from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast

user_nickname = str(pw_input('Enter your nick', required=False)).title().strip()
user_age = str(pw_input('Enter your age', type=NUMBER)).lstrip('0-')
print(f'User: {user_nickname} Age: {user_age}')

admin = 'Ggjiuw'
promouter = 'John'
is_admin = user_nickname == admin
is_promouter = user_nickname == promouter
is_other_user = (user_nickname != admin) and (user_nickname != promouter)
is_authority = is_admin or is_promouter

print(len(admin))

if is_admin:
    put_success(f'Hi, my master') 
    if user_age.isdigit():
        put_success(f'I know, you are {user_age} years old xo-xo')
    else:
        put_warning(f'You have not entered age \U000026D4')
        print('Age error 404')

elif user_nickname == 'Dd':
    put_success(f'Hello, {user_nickname}')
    if user_age.isdigit():
        put_success(f'I know, you are {user_age} years old xo-xo')
    else:
        put_warning(f'You have not entered age \U000026D4')
        print('Age error 404')

elif is_promouter:
    put_markdown('Sold')

else:
    put_warning(f'You have not entered nick \U000026D4')
    print('Name error 404')

toast(f'\U0001F480')



