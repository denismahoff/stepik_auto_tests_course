from selene import browser, have, be

browser.config.hold_browser_open = True


# browser.config.browser_name = 'firefox'
# browser.config.timeout = 6.0

def test_guru_login():  # name test case

    browser.open('https://qa.guru/cms/system/login')
    browser.element('.login-form input[name=email]').type('qagurubot@gmail.com')
    browser.element('.login-form input[name=password]').type('qagurupassword').press_enter()
    browser.element('.main-header__login').click()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
