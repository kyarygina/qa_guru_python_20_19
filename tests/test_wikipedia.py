from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_wikipedia_search_appium():

    with step('Ввести текст в поисковую строку'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Проверить результат выдачи поиска'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

def test_wikipedia_search_and_click_tesla():

    with step('Ввести текст в поисковую строку'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Tesla')

    with step('Проверить результат выдачи поиска'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Tesla'))

    with step('Кликнуть на первый результат выдачи поиска'):
        results.first.click()