class Contact:
    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):
        """ (Contact, str, str, str) -> NoneType

        Initialize this Contact with first name first_name, last name
        last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """

        self.phone_number = telephone_num

    def __str__(self):
        """ (Contact) -> str
        Return a string representation of this contact.
        """
        return '{0} {1} <{2}>'.format(self.first_name, self.last_name, self.email_address)


if __name__ == '__main__':
    c1 = Contact('Paul', 'McCartney', 'paul@gmail.com')
    print(c1)
    c1.add_phone_number('555-1111')

    c2 = Contact('Paul', 'McCartney', 'paul@gmail.com')
    Contact.add_phone_number(c2, '555-1111')

    print(c1.phone_number)
    print(c2.phone_number)

    print(str.replace('abc 123', '123', '246'))
    print('abc 123'.replace('123', '246'))

