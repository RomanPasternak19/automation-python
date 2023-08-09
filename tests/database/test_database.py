import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_user_insert():
    db = Database()
    db.insert_user(3, 'John', 'MainStreet', 'Anytown', '12345', 'Canada')
    user = db.get_user_address_by_name('John')
    
    assert user[0][0] == 'MainStreet'
    assert user[0][1] == 'Anytown'
    assert user[0][2] == '12345'
    assert user[0][3] == 'Canada'


@pytest.mark.database
def test_place_of_residence_update():
    db = Database()
    db.update_place_of_residence_by_name('John', 'Wall Street', 'New York', '54321', 'USA')
    user = db.get_user_address_by_name('John')

    assert user[0][0] == 'Wall Street'
    assert user[0][1] == 'New York'
    assert user[0][2] == '54321'
    assert user[0][3] == 'USA'


@pytest.mark.database
def test_sorted_database():
    db = Database()
    users = db.sorted_users_by_name()

    assert users[0][1] == 'John'
    assert users[1][1] == 'Sergii'
    assert users[2][1] == 'Stepan'


@pytest.mark.database
def test_number_of_customers():
    db = Database()
    count = db.number_of_customers()

    assert count[0][0] == 3


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'cookies', 'sweet', 30)
    cookies_qnt = db.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'test', 'data', 999)
    db.delete_product_by_id(99)
    qnt  = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Orders", orders)

    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'