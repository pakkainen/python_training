import re

from selenium.webdriver.support.ui import Select
from models.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def open_contacts_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_form()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd

        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_selected_value("bday", contact.bday)
        self.change_selected_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_selected_value("aday", contact.aday)
        self.change_selected_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_selected_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_list()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_list()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # accept alert
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first(self):
        self.delete_contact_by_index(0)

    def add_contact_to_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_list()
        self.select_contact_by_id(contact_id)
        # select group by id
        wd.find_element_by_name("to_group").find_element_by_css_selector("option[value='%s']" % group_id).click()
        # add contact to group
        wd.find_element_by_name("add"). click()
        self.contact_cache = None

    def filter_contacts_by_group_id(self, group_id):
        wd = self.app.wd
        wd.find_element_by_name("group").find_element_by_css_selector("option[value='%s']" % group_id).click()

    def remove_contact_from_group_by_id(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contacts_list()
        # select group by id
        self.filter_contacts_by_group_id(group_id)
        self.select_contact_by_id(contact_id)
        # remove contact from group
        wd.find_element_by_name("remove").click()
        self.open_contacts_list()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_list()
        entry = wd.find_elements_by_name("entry")[index]
        entry.find_element_by_xpath("./td[8]").click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_list()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_list()
        entry = wd.find_elements_by_name("entry")[index]
        entry.find_element_by_xpath("./td[7]").click()

    def update_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.open_contacts_list()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def update_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_list()
        self.open_contact_to_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def update_first(self):
        self.update_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.open_contacts_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_list()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath("./td[2]").text
                firstname = element.find_element_by_xpath("./td[3]").text
                address = element.find_element_by_xpath("./td[4]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname, address=address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contacts_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address, email=email, email2=email2,
                       email3=email3, home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_contacts_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)
