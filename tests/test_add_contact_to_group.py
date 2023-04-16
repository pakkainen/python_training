import random
from models.group import Group
from models.contact import Contact


def test_add_contact_to_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    random_group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(random_group)) == 0:
        app.contact.create(Contact(firstname="test"))
    random_contact = random.choice(orm.get_contacts_not_in_group(random_group))
    app.contact.add_contact_to_group_by_id(random_contact.id, random_group.id)
    assert random_contact in orm.get_contacts_in_group(random_group)
