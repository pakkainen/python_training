import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contacts_from_edit_page = app.contact.get_contacts_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contacts_list()[0]
    contacts_from_view_page = app.contact.get_contacts_info_from_view_page(0)
    assert contact_from_home_page.home == contacts_from_view_page.home
    assert contact_from_home_page.work == contacts_from_view_page.work
    assert contact_from_home_page.mobile == contacts_from_view_page.mobile
    assert contact_from_home_page.phone2 == contacts_from_view_page.phone2


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile,
                                        contact.work, contact.phone2]))))

