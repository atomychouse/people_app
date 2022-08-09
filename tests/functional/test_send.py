from home import app

"""
Testing cases: 
-1 null value to send e-mail
-2 small list of accounts
"""
def test_null():
    with app.test_client() as test_client:
        body = {'name':None}
        response = test_client.post('/send_email',data=body)
        assert response.status_code == 200

def test_small_list():
    with app.test_client() as test_client:
        body = {'accounts':'cruzarios@gmail.com',
            'accounts':'albertorios.py@gmail.com',}
            
        response = test_client.post('/send_email', json=body)
        assert response.status_code == 200
