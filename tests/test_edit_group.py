import random
import string
from models.group import Group


def test_edit_first_group(app):
    random_name = ''.join(random.choices(string.ascii_letters, k=8))
    app.session.login(username="admin", password="secret")
    app.group.update_first(Group(name=random_name, header=random_name, footer=random_name))
    app.session.logout()
