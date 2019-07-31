import pytest
from fixture.application import Application

"""
These are test for the Customer Portal
"""

# Initializing a pytest fixture
@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_show_passwords(app):
    app.open_home_page()
    app.session.login("vitalytestqa2@gmail.com", "JA_xM2EABVuUVxma")
    app.navigate_to_customer_portal()
    app.switch_show_passwords_toggle()
    app.session.logout()