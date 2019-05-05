import datetime


class StoreChain():
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


class Store(StoreChain):
    """docstring for Store"""

    def __init__(self, name, address, ID, tel):
        super(Store, self).__init__(name, address)
        self.__ID = ID
        self.__tel = tel

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    def __str__(self):
        return ' Welcome to Store - {}\n ID: {}\n Phone: {} \n Address: {}\n'.format(self.name, self.ID, self.tel,
                                                                                     self.address)


# CITIZEN CLASS

class Citizen():
    """docstring for Staff"""

    def __init__(self, ssn, name, address):
        self.__ssn = ssn
        self.__name = name
        self.__address = address

        super(Citizen, self).__init__()

    @property
    def ssn(self):
        return self.__ssn

    @ssn.setter
    def ssn(self, ssn):
        self.__ssn = ssn

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address


class Staff(Citizen):
    """docstring for Staff"""

    def __init__(self, ssn, name, address, job_id, job_title, salary):
        self.__job_id = job_id
        self.__job_title = job_title
        self.__salary = salary

        super(Staff, self).__init__(ssn, name, address)

    @property
    def job_id(self):
        return self.__job_id

    @job_id.setter
    def job_id(self, job_id):
        self.__job_id = job_id

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        self.__job_title = job_title

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def __str__(self):
        print(' Staff: {} \n SSN: {} \n Job ID: {}'.format(self.name, self.ssn, self.job_id, ))
        print(' Job Title: {} \n Salary: {}\n Address: {}'.format(self.__job_title, self.salary, self.address))

        return ''


class Customer(Citizen):
    """docstring for Customer"""

    def __init__(self, ssn, name, address, ID, tel, memberships):
        self.__ID = ID
        self.__purchasing_points = 0
        self.__tel = tel,
        self.__memberships = memberships
        super(Customer, self).__init__(ssn, name, address)

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID):
        self.__ID = ID

    @property
    def purchasing_points(self):
        return self.__purchasing_points

    @purchasing_points.setter
    def purchasing_points(self, purchasing_points):
        self.__purchasing_points = purchasing_points

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel):
        self.__tel = tel

    @property
    def memberships(self):
        return self.__memberships

    @memberships.setter
    def memberships(self, memberships):
        self.__memberships = memberships

    def __str__(self):
        print(' Customer: {} \n SSN: {} \n ID: {} \n Points: {}'.format(self.name, self.ssn, self.ID,
                                                                        self.purchasing_points))
        print(' Phone: {0} \n Address: {1}'.format(self.tel, self.address))
        print(' MemberShips: ')
        for mem in self.memberships:
            print('  -' + mem)

        return ''


# ORDER CLASS

class Order():
    def __init__(self, store, customer, staff):
        self.__store = store
        self.__customer = customer
        self.__staff = staff
        self.__products = []
        self.__quantity = 0

    @property
    def store(self):
        return self.__store

    @store.setter
    def store(self, store):
        self.__store = store

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def staff(self):
        return self.__staff

    @staff.setter
    def staff(self, staff):
        self.__staff = staff

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        self.__products = products

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def add_product(self, product):
        self.__products.append(product)
        self.__quantity = len(self.__products)



class Product():

    def __init__(self, product_code, name, description, price, points):
        self.__product_code = product_code
        self.__name = name
        self.__description = description
        self.__price = price
        self.__points = points

    @property
    def product_code(self):
        return self.__product_code

    @product_code.setter
    def product_code(self, product_code):
        self.__product_code = product_code

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    def is_any_field_empty(self):
        attrs = [self.price, self.name, self.product_code, self.points]


    def __str__(self):
        print(' Product {} \n Code: {} \n Price: {} \n Points: {} \n Description'.format(self.name, self.product_code,
                                                                                         self.price, self.points,
                                                                                         self.description))
