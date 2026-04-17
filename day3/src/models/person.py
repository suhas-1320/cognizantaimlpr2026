"""
Person model
"""
import re
class person:
    def __init__(self, adharCardNO:str, mobileNo:int):
        self._adharCardNO = adharCardNO
        self._mobileNo = mobileNo
    
    @property
    def adharCardNO(self):
        return self._adharCardNO
    @property

    def mobileNo(self):
        return self._mobileNo
    @mobileNo.setter
    def mobileNo(self, value):
        if not re.match(r'^\d{10}$', str(value)):
            raise ValueError("Mobile number must be a 10-digit number.")
        self._mobileNo = value
        