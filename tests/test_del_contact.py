import random
import time

from models.contact import Contact


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(random_contact.id)
    time.sleep(1)  # без паузы ответ из БД приходит раньше, чем выполняется запрос из UI на удаление
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(rm_spaces, db.get_contact_list())
        ui_contacts = map(rm_spaces, app.contact.get_contacts_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(ui_contacts, key=Contact.id_or_max)


# функция - заглушка против падения тестов из-за пропадающих пробелов в списке контактов, полученном в UI
def rm_spaces(contact):
    return Contact(id=contact.id, firstname=contact.firstname.replace(" ", ""),
                   lastname=contact.lastname.replace(" ", ""))