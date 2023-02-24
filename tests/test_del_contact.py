def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()
