import requests
import random

# Sample data (replace with your actual data or variables)
lsd2 = 'sample_lsd'
j2 = 'sample_jazoest'
ccp = 'sample_ccp'
reg_i = 'sample_reg_instance'
reg_id = 'sample_reg_impression_id'
nmf = 'Ashley'
nml = 'Great'
ids = 'oyamatmot0812@gmail.com'
dayy = '08'
monn = '12'
yearr = '2008'
pswrd = 'Grathegreat'

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
url = 'https://www.facebook.com/signup'

# Send POST request
response = requests.post(url, data=data)

# Print response (for debugging purposes)
print(response.status_code)
print(response.text)