from models import People


def test_new_people():
    """
    Given a people model 
    WHEN new people item  is created
    THEN check all fields are defined correctly
    
    """
    people = People(name='Alberto',last_name='Rios',email_account='test@gmail.com')
    assert people.email_account == "test@gmail.com"
    assert people.name == "Alberto"
    assert people.last_name == "Rios"