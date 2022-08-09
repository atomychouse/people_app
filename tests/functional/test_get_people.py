from home import app

"""
Testing cases: 
-1 full list
-2 null value in an attribute search
-3 not valid attribute to search

"""



def test_full_list():
    with app.test_client() as test_client:
        response = test_client.get('/people')
        assert response.status_code == 200

def test_null_attr_search():
    body = {'name':None}
    with app.test_client() as test_client:
        response = test_client.get('/people?filter_attr=name&filter_val=')
        assert response.status_code == 200


def test_not_valid_attr():
    body = {
        'filter_attr':'soth_name',
        'filter_val':'Rios'
        }
    with app.test_client() as test_client:
        response = test_client.get('/people?filter_attr=south_name&filter_val=Rios')
        assert response.status_code == 200
