from moduls.ui.page_objects.sign_in_page import SignInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_username_POM():
    # створення обекту сторінки 
    sign_in_page = SignInPage()

    # відкриваємо сторінку
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # перевіряємоб що назва сторінки такаб яку очікуємо
    assert sign_in_page.check_title ("Sign is to GitHub. GitHub")

    # закриваємо браузер
    sign_in_page.close()
