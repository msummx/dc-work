class Address:
    def __init__(self, street: str, city: str, state: str, zip_code: str):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.full = "%s, %s, %s %s" % self.street, self.city, self.state, self.zip_code

class User(Address):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        
    def add_address(self, address: list):
        
        
        newAddressList = newAddressList.append(address)
        return newAddressList
