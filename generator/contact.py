import jsonpickle
import random
import string
import os.path
import getopt
import sys
from models.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + '!"#＄%&()*+,-./:;=>?@[]^_`{|}~' + " " * 10
    # исключается при сохранении пробел ' ' в конце строки, '\\' из строки и все символы после <,
    # одинарная ковычка вызывает ошибку БД
    # повторяющиеся пробелы не отображаются в списке
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="")] + [
            Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20),
                    lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                    title=random_string("title", 20), company=random_string("company", 20),
                    address=random_string("address", 20), home=random_string("home", 20),
                    mobile=random_string("mobile", 20), work=random_string("work", 20), fax=random_string("fax", 20),
                    email=random_string("email", 20), email2=random_string("email2", 20),
                    email3=random_string("email3", 20), homepage=random_string("homepage", 20),
                    bday="21", bmonth="February", byear="1986", aday="21", amonth="February", ayear="2026",
                    address2=random_string("address2", 20), phone2=random_string("phone2", 20),
                    notes=random_string("notes", 20))
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
