import random
import string
from models.group import Group


def random_value():
    return ''.join(random.choices(string.ascii_letters, k=8))


def test_modify_first_group_name(app):
    app.group.modify_first(Group(name=random_value()))


def test_modify_first_group_header(app):
    app.group.modify_first(Group(header=random_value()))


def test_modify_first_group_footer(app):
    app.group.modify_first(Group(footer=random_value()))
