import requests
import random

# Actual sample data (replace with your actual data or variables)
lsd2 = 'ABC123DEF456GHI789JKL'
j2 = '1234567890ABCDEFG'
ccp = 'CCP1234'
reg_i = 'REG_INSTANCE_123456'
reg_id = 'REG_IMPRESSION_ID_123456'
nmf = 'John'
nml = 'Doe'
ids = 'johndoe@hotmail.com'
dayy = '01'  # e.g., '01'
monn = '01'  # e.g., '01'
yearr = '2000'  # e.g., '2000'
pswrd = 'securepassword123'

data = {
    'lsd': lsd2,
    'jazoest': j2,
    'ccp': ccp,
    'reg_instance': reg_i,
    'submission_request': 'true',
    'helper': '',
    'reg_impression_id': reg_id,
    'ns': '0',
    'zero_header_af_client': '',
    'app_id': '',
    'logger_id': '',
    'field_names[]': [
        'firstname',
        'reg_email__',
        'sex',
        'birthday_wrapper',
        'reg_passwd__'
    ],
    'firstname': nmf,
    'lastname': nml,
    'reg_email__': ids,
    'sex': str(random.choice(['1', '2'])),
    'custom_gender': '',
    'did_use_age': 'false',
    'birthday_day': dayy,
    'birthday_month': monn,
    'birthday_year': yearr,
    'age_step_input': '',
    'reg_passwd__': pswrd,
    'submit': 'Sign Up'
}

# URL to which the POST request will be sent (replace with actual URL)
url = 'https://www.example.com/signup'

# Send POST request
response = requests.post(url, data=data)

# Print response (for debugging purposes)
print(response.status_code)
print(response.text)
