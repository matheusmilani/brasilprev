class Roles():
    def __init__(self):
        self.switcher_by_name = {
            'admin': 1,
            'common': 2
        }

        self.switcher_by_number = {
            1: 'admin',
            2: 'common'
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Invalid Number')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Invalid Name')

class Active():
    def __init__(self):
        self.switcher_by_name = {
            True: 1,
            False: 0
        }

        self.switcher_by_number = {
            0: True,
            1: False
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Invalid Number')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Invalid Name')

class Status():
    def __init__(self):
        self.switcher_by_name = {
            'Waiting Approvement': 0,
            'Payment Approved': 1,
            'On Deliver': 2,
            'Delivered': 3,
            'Canceled': 4,
        }

        self.switcher_by_number = {
            0 : 'Waiting Approvement',
            1 : 'Payment Approved',
            2 : 'On Deliver',
            3 : 'Delivered',
            4 : 'Canceled',
        }

    def enum_to_name(self, enum):
        return self.switcher_by_number.get(enum, 'Invalid Number')

    def name_to_enum(self, name):
        return self.switcher_by_name.get(name, 'Invalid Name')
