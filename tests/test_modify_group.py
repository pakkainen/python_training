import random
import string
from models.group import Group


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    new_data = Group(name=random_value())
    app.group.modify_group_by_id(random_group.id, new_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    new_data.id = random_group.id
    old_groups.remove(random_group)
    old_groups.append(new_data)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)


# def test_modify_first_group_header(app):
#     old_groups = app.group.get_groups_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.modify_first(Group(header=random_value()))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_modify_first_group_footer(app):
#     old_groups = app.group.get_groups_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.modify_first(Group(footer=random_value()))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
