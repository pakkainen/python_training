import re
from random import randrange


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


def clear(s):
    return re.sub('[() -]', '', s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))

