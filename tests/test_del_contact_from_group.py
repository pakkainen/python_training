import random
from models.group import Group
from models.contact import Contact


def test_del_contact_from_group(app, orm):
    # test preparing
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    random_group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(orm.get_contacts_in_group(random_group)) == 0:
        random_contact = random.choice(orm.get_contact_list())
        app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    # test body
    random_contact = random.choice(orm.get_contacts_in_group(random_group))
    app.contact.remove_contact_from_group_by_id(random_contact.id, random_group.id)
    assert random_contact not in orm.get_contacts_in_group(random_group)
