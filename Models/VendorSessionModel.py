class VendorSessionModel:

    vendor_session_db = dict()

    def __init__(self):
        pass

    def login(self, username):
        # Adding the username in class variable created above.

        VendorSessionModel.vendor_session_db[username] = True
        return True

    # performing the logout operation for the given username

    def logout(self, username):
        if (username in VendorSessionModel.vendor_session_db):
            del VendorSessionModel.vendor_session_db[username]
            return True
        else:
            return False

    # Checking if the username is available in the class variable that is declared as dictionary

    def check_login(self, username):
        if (username in VendorSessionModel.vendor_session_db):
            return True
        else:
            return False
