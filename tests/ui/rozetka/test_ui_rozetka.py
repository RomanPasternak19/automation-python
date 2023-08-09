from modules.ui.page_objects.rozetka.main_page import MainPage
import pytest

BICYCLE = "Велосипед"
PHONE = "Мобільний телефон"
CATEGORYNAME = "Ноутбуки та комп’ютери"
CATEGORYHEADERTEXT = "Комп'ютери та ноутбуки"


@pytest.mark.rozetka
def test_search_item():
    main_page = MainPage()

    main_page.visit()
    main_page.search_item(BICYCLE)

    assert main_page.check_item_name(BICYCLE)


@pytest.mark.rozetka
def test_add_item_to_basket():
    main_page = MainPage()

    main_page.visit()
    main_page.search_item(BICYCLE)
    main_page.add_item_to_basket()
    
    assert main_page.check_product_added_to_cart(1)


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


@pytest.mark.rozetka
def test_check_display_categories():
    main_page = MainPage()

    main_page.visit()
    main_page.open_catalogue_menu()
    main_page.select_category_by_name(CATEGORYNAME)
    
    assert main_page.check_category_heading(CATEGORYHEADERTEXT)