import time
import re


def test_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    initial_account = browser.find_element_by_css_selector('#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs').text
    initial_account = float(re.findall(r'\d+,\d+', initial_account)[0].replace(',', '.'))
    print(initial_account)

    browser.find_element_by_class_name("btn-add-to-basket").click()
    time.sleep(1)

    result = browser.find_element_by_xpath('//*[@id="messages"]/div[1]/div/strong').text
    assert 'Coders at Work' in result

    final_account = browser.find_element_by_css_selector(
        '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs').text
    final_account = float(re.findall(r'\d+,\d+', final_account)[0].replace(',', '.'))

    assert final_account == initial_account + 19.99