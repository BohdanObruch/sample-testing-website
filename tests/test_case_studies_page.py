from selene import browser, have
from allure import title, tag, step, severity, label


@severity('Medium')
@tag('UI')
@label('p2h.com')
@title('Checking the availability and display of the case studies page on the website ')
def test_displaying_the_case_studies_page():
    with step('Set the size of the browser window'):

        # browser.config.driver_name = 'firefox' # Chrome works by default, but can be customized
        browser.config.base_url = 'https://p2h.com'

        # browser.config.timeout = 2  # Global timeout for the config if necessary
        browser.config.window_width = 1920  # setting the size of the browser window
        browser.config.window_height = 1080

    with step('Open website page'):
        browser.open('/')

    with step('Check the page title'):
        browser.should(have.title_containing('P2H Inc.: Digital Solutions for Public Sector'))

    with step('Accept cookies'):
        browser.element('.cky-notice-group .cky-btn-accept').click()

    with step('Going to burger menu'):
        browser.element('.open-nav').click()

    with step('Open case studies page'):
        browser.element('#menu-main-menu-redesign .menu-item-object-custom').click()

    with step('Check the title and url of the page'):
        browser.should(have.title_containing('P2H Success Stories for Government and Enterprise Solutions'))
        browser.should(have.url_containing("/case-studies"))

    with step('Close browser'):
        browser.quit()
