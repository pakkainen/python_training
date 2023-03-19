import random
import string
from models.group import Group


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    group = Group(name=random_value())
    group.id = old_groups[0].id
    app.group.modify_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
