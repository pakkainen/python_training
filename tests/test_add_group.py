from models.group import Group


def test_add_group(app):
    app.group.create(Group(name="test group 1", header="test", footer="test"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
