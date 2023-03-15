from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                      nickname="russian_ivan", title="Temp_title", company="Temp_company",
                      address="Temp_company_address", home="+79987654321",
                      mobile="+79087654321", work="+79987654321", fax="89098765432",
                      email="ivanii@temp.com", email2="ivanii@temp.ru", email3="ivanii@temp.su",
                      homepage="ivan.temp.ru", bday="21", bmonth="February", byear="1986", aday="21",
                      amonth="February", ayear="2026", address2="Temp_ivan_address",
                      phone2="build 1, flat 2",
                      notes="some notes about ivan")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
