import random
import string
from random import randrange
from models.contact import Contact


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname=random_value(), middlename=random_value(), lastname=random_value(),
                      nickname=random_value(), title=random_value(), company=random_value(),
                      address=random_value(), home=random_value(),
                      mobile=random_value(), work=random_value(), fax=random_value(),
                      email=random_value(), email2=random_value(), email3=random_value(),
                      homepage=random_value(), bday="21", bmonth="February", byear="1986", aday="21",
                      amonth="February", ayear="2026", address2=random_value(),
                      phone2=random_value(),
                      notes=random_value())
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
