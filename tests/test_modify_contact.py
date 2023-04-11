import random
import string
from models.contact import Contact


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    new_data = Contact(firstname=random_value(), middlename=random_value(), lastname=random_value(),
                       nickname=random_value(), title=random_value(), company=random_value(),
                       address=random_value(), home=random_value(),
                       mobile=random_value(), work=random_value(), fax=random_value(),
                       email=random_value(), email2=random_value(), email3=random_value(),
                       homepage=random_value(), bday="21", bmonth="February", byear="1986", aday="21",
                       amonth="February", ayear="2026", address2=random_value(),
                       phone2=random_value(),
                       notes=random_value())
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.update_contact_by_id(random_contact.id, new_data)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    new_data.id = random_contact.id
    old_contacts.remove(random_contact)
    old_contacts.append(new_data)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(rm_spaces, db.get_contact_list())
        ui_contacts = map(rm_spaces, app.contact.get_contacts_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(ui_contacts, key=Contact.id_or_max)


# функция - заглушка против падения тестов из-за пропадающих пробелов в списке контактов, полученном в UI
def rm_spaces(contact):
    return Contact(id=contact.id, firstname=contact.firstname.replace(" ", ""),
                   lastname=contact.lastname.replace(" ", ""))
