from selene import browser, have
from allure import title, tag, step, severity, label


@severity('MINOR')
@tag('UI')
@label('p2h.com')
@title('Checking the display of pagination and navigating through it')
def test_displaying_information_with_pagination_on_the_main_page():
    with step('Customize test'):
        browser.config.base_url = 'https://p2h.com'

    with step('Open website page'):
        browser.open('/')

    with step('Checking that the number of pagination points is exactly 12 and that the first one is active'):
        browser.all('#section-pagination li').should(have.size(12))
        browser.element('#section-pagination li:nth-child(1)').should(have.css_class('active'))

    with step('Going to the pagination pages'):

        with step('Going to the second page'):
            browser.element('#section-pagination [data-index="1"]').click()
            browser.element('.image-section-content').should(have.text('We design and develop'))

        with step('Going to the third page'):
            browser.element('#section-pagination [data-index="2"]').click()
            browser.element('#services-block h1').should(have.text('We do'))

        with step('Going to the fourth page'):
            browser.element('#section-pagination [data-index="3"]').click()
            browser.element('.desktop .slide-first span').should(have.text('NUMBER ONE'))

        with step('Going to the fifth page'):
            browser.element('#section-pagination [data-index="4"]').click()

        with step('Going to the sixth page'):
            browser.element('#section-pagination [data-index="5"]').click()

        with step('Going to the seventh page'):
            browser.element('#section-pagination [data-index="6"]').click()

        with step('Going to the eighth page'):
            browser.element('#section-pagination [data-index="7"]').click()

        with step('Going to the ninth page'):
            browser.element('#section-pagination [data-index="8"]').click()

        with step('Going to the tenth page'):
            browser.element('#section-pagination [data-index="9"]').click()

        with step('Going to the eleventh page'):
            browser.element('#section-pagination [data-index="10"]').click()

        with step('Going to the twelfth page'):
            browser.element('#section-pagination [data-index="11"]').click()
            browser.element('.footer-nav .navigation li:nth-child(5)').should(have.text('Careers'))

    browser.quit()