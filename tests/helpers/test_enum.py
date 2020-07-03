from helpers.enum import *

class TestEnums:
    def test_roles(self):
        assert Roles().enum_to_name(1) == 'admin'
        assert Roles().enum_to_name(2) == 'common'

        assert Roles().name_to_enum('admin') == 1
        assert Roles().name_to_enum('common') == 2

    def test_active(self):
        assert Active().enum_to_name(0) == False
        assert Active().enum_to_name(1) == True

        assert Active().name_to_enum(True) == 1
        assert Active().name_to_enum(False) == 0

    def test_status(self):
        assert Status().enum_to_name(0) == 'Waiting Approvement'
        assert Status().enum_to_name(1) == 'Payment Approved'
        assert Status().enum_to_name(2) == 'On Deliver'
        assert Status().enum_to_name(3) == 'Delivered'
        assert Status().enum_to_name(4) == 'Canceled'

        assert Status().name_to_enum('Waiting Approvement') == 0
        assert Status().name_to_enum('Payment Approved') == 1
        assert Status().name_to_enum('On Deliver') == 2
        assert Status().name_to_enum('Delivered') == 3
        assert Status().name_to_enum('Canceled') == 4
