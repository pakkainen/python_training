import re
from random import randrange
from models.contact import Contact


def test_contact_by_index_on_home_page(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contacts_from_edit_page = app.contact.get_contacts_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contacts_from_edit_page.lastname
    assert contact_from_home_page.firstname == contacts_from_edit_page.firstname
    assert contact_from_home_page.address == contacts_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_edit_page)


def test_phones_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contacts_list()))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contacts_from_view_page = app.contact.get_contacts_info_from_view_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_view_page)


def test_contacts_homepage_and_db_matching(app, db):
    contact_list_from_homepage = sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
    contact_list_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_list_from_homepage)):
        contact_from_homepage = contact_list_from_homepage[i]
        contact_from_db = contact_list_from_db[i]
        assert contact_from_homepage.firstname == clear_space(contact_from_db.firstname)
        assert contact_from_homepage.lastname == clear_space(contact_from_db.lastname)
        assert contact_from_homepage.address == clear_space(contact_from_db.address)
        assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


# функция - заглушка против падения тестов из-за пропадающих пробелов в списке контактов, полученном в UI
def clear_space(s):
    return " ".join(s.split()) if s is not None else ""


def clear_phone(s):
    return re.sub('[() -]', '', s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear_space(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))
