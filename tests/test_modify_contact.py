import random
import string
from random import randrange
from models.contact import Contact


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                      nickname="russian_ivan", title="Temp_title", company="Temp_company",
                      address="Temp_company_address", home="+79987654321",
                      mobile="+79087654321", work="+79987654321", fax="89098765432",
                      email="ivanii@temp.com", email2="ivanii@temp.ru", email3="ivanii@temp.su",
                      homepage="ivan.temp.ru", bday="21", bmonth="February", byear="1986", aday="21",
                      amonth="February", ayear="2026", address2="Temp_ivan_address",
                      phone2="build 1, flat 2",
                      notes="some notes about ivan")
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.update_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

