#!/usr/bin/env python3

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return (' '.join((self.name, self.phone, self.email)))

class ContactList:
    def __init__(self):
        self.d = {}

    def add_contact(self, contact):
        self.d[contact.name] = contact

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return (str(self.d[name]))
        else:
            return 'None'

    def __str__(self):
        sorted_list = [str(self.d[a]) for a in sorted(self.d)]
        return ('\n'.join(['Contact list', '------------'] + sorted_list))
