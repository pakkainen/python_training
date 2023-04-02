import pytest
import random
import string
from models.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '!"#＄%&()*+,-./:;=>?@[]^_`{|}~' + " " * 10
    # исключается при сохранении пробел ' ' в конце строки, '\\' из строки и все символы после <,
    # одинарная ковычка вызывает ошибку БД
    # повторяющиеся пробелы не отображаются в списке
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="")] + [
            Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                    title=random_string("title", 20), company=random_string("company", 20),
                    address=random_string("address", 20), home=random_string("home", 20),
                    mobile=random_string("mobile", 20), work=random_string("work", 20), fax=random_string("fax", 20),
                    email=random_string("email", 20), email2=random_string("email2", 20),
                    email3=random_string("email3", 20), homepage=random_string("homepage", 20),
                    bday="21", bmonth="February", byear="1986", aday="21", amonth="February", ayear="2026",
                    address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                    notes=random_string("notes", 20))
            for i in range(10)
            ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
