class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete_first(self):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # delete first group
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def update_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        wd.find_element_by_name("selected[]").click()
        # edit first group
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        # submit group update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
