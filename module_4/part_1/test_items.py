from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

btn_site_lng = {
    'ru': 'Добавить в корзину',
    'en-gb': 'Add to basket',
    'es': 'Añadir al carrito',
    'fr': 'Ajouter au panier'
}

selector_add_btn = '.btn-add-to-basket'


def test_btn_add_to_basket(browser):
    # сохраняем язык сайта, полученный из фикстуры в conftest
    site_language = browser.user_language
    btn_text = btn_site_lng[site_language]

    # Arrange
    browser.get(link)

    # Act
    btn_add = browser.find_element(By.CSS_SELECTOR, selector_add_btn)

    # Assert
    assert btn_text in btn_add.text, 'Button text incorrect'
