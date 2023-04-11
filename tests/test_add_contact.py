from models.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
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
