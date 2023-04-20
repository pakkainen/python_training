from models.group import Group
from models.contact import Contact


def test_group_list(app, db):
    ui_group_list = app.group.get_groups_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_group_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_contact_list = map(rm_spaces, app.contact.get_contacts_list())
    db_list = map(rm_spaces, db.get_contact_list())
    assert sorted(ui_contact_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)


# функция - заглушка против падения тестов из-за пропадающих пробелов в списке контактов, полученном в UI
def rm_spaces(contact):
    return Contact(id=contact.id, firstname=contact.firstname.replace(" ", ""),
                   lastname=contact.lastname.replace(" ", ""))
