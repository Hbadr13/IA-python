class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            raise AttributeError("--------------.")
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        cstr = ""
        for key in self.__dict__:
            cstr += "   " + str(key).ljust(8, ' ') + " = " + \
                str(self.__dict__[key]) + "\n"
        return cstr


class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        if isinstance(new_account, Account):
            for key in self.accounts:
                if key.name == new_account.name:
                    print("Account already added to Bank")
                    return False
            self.accounts.append(new_account)
            return True
        return False
    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        Origin = self.getAcount(origin)
        Dest = self.getAcount(dest)
        if Origin == None or Dest == None:
            return False
        if self.IfNoCorrupted(Origin) or self.IfNoCorrupted(Dest):
            return False
        if origin == dest:
            return True
        if amount < 0 or amount > Origin.value:
            return False
        Dest.value += amount
        Origin.value -= amount
        return True

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@////////////
    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            raise ValueError("account name must be a string")
        objectt = self.getAcount(name)
        if not isinstance(objectt, Account):
            return 1
        if len(objectt.__dict__) % 2 == 0:
            if "age" in objectt.__dict__:
                objectt.__dict__.pop("age")
            else:
                objectt.__dict__["age"] = 0
        flag = 0
        if "name" not in objectt.__dict__:
            objectt.__dict__["name"] = name
        if not "id" in objectt.__dict__:
            objectt.__dict__["id"] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if "value" not in objectt.__dict__:
            objectt.__dict__["value"] = 0.0
        copy = objectt.__dict__.copy()
        for key in copy:
            if key.startswith("b"):
                objectt.__dict__.pop(key)
            if key.startswith("zip") or key.startswith("addr"):
                flag = 1
        if flag == 0:
            objectt.__dict__["zip"] = ""
        if not isinstance(objectt.__dict__["name"], str):
            objectt.__dict__.pop("name")
            object.__dict__["name"] = name
        if type(objectt.__dict__["id"]) is not int:
            objectt.__dict__["id"] = Account.ID_COUNT
            Account.ID_COUNT += 1
        if type(objectt.__dict__["value"]) is not int and type(objectt.__dict__["value"]) is not float:
            objectt.__dict__.pop("value")
            objectt.__dict__["value"] = 0.0
        return 0
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@////////////

    def IfNoCorrupted(self, objectt):
        """
        Returns True if  if the Acount object is corrupted
        else return False
        """
        if not isinstance(objectt, Account):
            return 1
        if len(objectt.__dict__) % 2 == 0:
            return 2
        flag = 0
        if "name" not in objectt.__dict__ or "id" not in objectt.__dict__:
            return 3
        for key in objectt.__dict__:
            if key.startswith("b"):
                return 4
            if key.startswith("zip") or key.startswith("addr"):
                flag = 1
        if flag == 0:
            return 5
        if not isinstance(objectt.__dict__["name"], str):
            return 6
        if type(objectt.__dict__["id"]) is not int:
            return 7
        if not type(objectt.__dict__["value"]) is not int:
            return 8
        if type(objectt.__dict__["value"]) is not int and type(objectt.__dict__["value"]) is not float:
            return 9
        return 0

    def getAcount(self, name):
        for key in self.accounts:
            if key.name == name:
                return key

    def __print__(self, name):
        if self.getAcount(name) != None:
            print("All Attributes about " + name)
            print(self.getAcount(name))
        else:
            print("Unknown Acount ")
