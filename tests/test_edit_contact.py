import random
import string
from models.contact import Contact


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_edit_first_contact(app):
    app.contact.update_first(Contact(firstname=random_value(), middlename=random_value(), lastname=random_value(),
                                     nickname=random_value(), title=random_value(), company=random_value(),
                                     address=random_value(), home=random_value(),
                                     mobile=random_value(), work=random_value(), fax=random_value(),
                                     email=random_value(), email2=random_value(), email3=random_value(),
                                     homepage=random_value(), bday="21", bmonth="February", byear="1986", aday="21",
                                     amonth="February", ayear="2026", address2=random_value(),
                                     phone2=random_value(),
                                     notes=random_value()))
