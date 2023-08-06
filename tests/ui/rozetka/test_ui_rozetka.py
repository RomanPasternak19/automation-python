from modules.ui.page_objects.rozetka.main_page import MainPage
import pytest

BICYCLE = 'Велосипед'
PHONE = 'Мобільний телефон'


@pytest.mark.rozetka
def test_search_item():
    main_page = MainPage()

    main_page.visit()

    main_page.search_item(BICYCLE)

    assert main_page.check_item_name(BICYCLE)

    main_page.close()


@pytest.mark.rozetka
def test_add_items_to_basket():
    main_page = MainPage()

    main_page.visit()

    main_page.search_item(BICYCLE)

    main_page.add_item_to_basket()
    
    assert main_page.check_product_added_to_cart(1)
    
    main_page.close()


@pytest.mark.rozetka
def test_check_sum_in_basket():
    main_page = MainPage()

    main_page.visit()

    main_page.search_item(BICYCLE)
    main_page.add_item_to_basket()
    
    main_page.search_item(PHONE)
    main_page.add_item_to_basket()
    
    main_page.open_shopping_cart()
    
    assert main_page.check_sum_in_basket()

    main_page.close()

