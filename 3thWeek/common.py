# 2022 - YemekSepeti Python Web Development BootCamp
# common functions and constants

import re
class RE:

    defaultNone = "None"
    defaultZero = "0"
    defaultYear = "1000"
    defaultMonth = "01"
    defaultDay = "01"
    defaultAP = "1"
    
    @staticmethod
    def verifyUsernamelk(username, email):
        """
        Username contains part of the user's first or last name
        if that is true, it returns 1 else it returns zero
        """
        return "1" if username in email else "0"

    @staticmethod
    def verifyEmailuserlk(username, email):
        """
        E-mail contains part of the user's first or last name
        if that is true, it returns 1 else it returns zero
        """
        return "1" if username in email else "0"
        
    @staticmethod
    def verifyEmail(email):
        """
        E-mail verification
        """
        regex = '^([a-zA-Z0-9.!#$%`*+/=?^_{|}~-]|\d)+@([a-z]|\d\-)+(\.([a-z]|\d|-)+)+$'
        return re.match(regex, str(email).lower())
    

