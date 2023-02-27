import random
import string
from models.contact import Contact


def test_edit_first_contact(app):
    random_string = ''.join(random.choices(string.ascii_letters, k=10))
    app.session.login(username="admin", password="secret")
    app.contact.update_first(Contact(firstname=random_string, middlename=random_string, lastname=random_string,
                                     nickname=random_string, title=random_string, company=random_string,
                                     address=random_string, home=random_string,
                                     mobile=random_string, work=random_string, fax=random_string,
                                     email=random_string, email2=random_string, email3=random_string,
                                     homepage=random_string, bday="21", bmonth="February", byear="1986", aday="21",
                                     amonth="February", ayear="2026", address2=random_string,
                                     phone2=random_string,
                                     notes=random_string))
    app.session.logout()
