import tkinter as tk
import random
import string
from models import Store, Staff, Customer, Product, Order


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class MainWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.num_of_last_product = 4
        self.product_objects = []
        self.is_receipt_open = False
        self.heading = tk.Label(
            self,
            pady=10,
            text='Welcome to Store Management System',
            font='Helvetica 16 bold'
        )

        self.heading.grid(row=0)
        # Frame for Staff and Customer Info
        self.infoFrame = tk.Frame(self)
        self.infoFrame.grid(row=1, sticky=tk.W, padx=20)

        self.staff_label = tk.Label(self.infoFrame, text='Staff Name')
        self.staff_label.grid(row=0, column=0, sticky=tk.EW, )

        self.staff_name = tk.Entry(self.infoFrame)
        self.staff_name.grid(row=0, column=1, sticky=tk.EW, )

        self.customer_label = tk.Label(self.infoFrame, text='Customer ID')
        self.customer_label.grid(row=1, sticky=tk.W)

        self.customer_id = tk.Entry(self.infoFrame)
        self.customer_id.grid(row=1, column=1, sticky=tk.W)

        # Frame for add more Button
        self.add_more_frame = tk.Frame(self)
        self.add_more_frame.grid(row=2, sticky=tk.W, padx=20, pady=10)

        self.add_more_label = tk.Label(self.add_more_frame, text='Add more products')
        self.add_more_label.pack(side=tk.LEFT)

        self.add_more_btn = tk.Button(
            self.add_more_frame,
            text='+',
            background='lightgreen',
            foreground='#fff',
            command=self.add_product_form
        )
        self.add_more_btn.pack(side=tk.LEFT)

        # Frame for products row
        self.pro_frame = tk.Frame(self, height=10)
        self.pro_frame.grid(row=3, sticky=tk.W)

        self.scroll_frame = tk.Scrollbar(self.pro_frame)
        self.scroll_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.products_frame = tk.Frame(self.pro_frame)
        self.products_frame.pack()

        # product headers
        self.pro_name_label = tk.Label(self.products_frame, text='Product Name')
        self.pro_name_label.grid(row=0, column=0)

        self.pro_code_label = tk.Label(self.products_frame, text='Product Code')
        self.pro_code_label.grid(row=0, column=1)

        self.pro_price_label = tk.Label(self.products_frame, text='Price')
        self.pro_price_label.grid(row=0, column=2)

        self.pro_qual_label = tk.Label(self.products_frame, text='Quantity')
        self.pro_qual_label.grid(row=0, column=3)

        self.pro_point_label = tk.Label(self.products_frame, text='Points')
        self.pro_point_label.grid(row=0, column=4)

        # initial four row inputs
        for item in range(1, 5):
            self.product_objects.append(ProductFrame(self.products_frame, item))

        self.warning_label = tk.Label(
            self,
            fg='#f0ad4e',
            text='',
            font='Helvetica 16 bold'
        )
        self.warning_label.grid(row=4)

        self.action_frame = tk.Frame(self)
        self.action_frame.grid(row=5, sticky=tk.W)

        self.print_btn = tk.Button(
            self.action_frame,
            text='Print',
            background='lightgreen',
            foreground='#fff',
            padx=50,
            command=self.print_action
        )
        self.print_btn.pack(side=tk.LEFT, padx=10, pady=20)

        self.close_btn = tk.Button(
            self.action_frame,
            text='Close',
            background='lightgreen',
            foreground='#fff',
            padx=50,
            command=self.exit
        )
        self.close_btn.pack(side=tk.LEFT, padx=10, pady=20)

    def exit(self):
        self.master.destroy()

    def on_receipt_close(self):
        self.t.destroy()
        self.is_receipt_open = False

    # to add new product input row
    def add_product_form(self):
        self.num_of_last_product = self.num_of_last_product + 1
        self.product_objects.append(ProductFrame(self.products_frame, self.num_of_last_product))

    def print_action(self):
        store = Store(
            name='Magnit',
            address='2, Amir Temur street, Tashkent',
            ID='2-A-T-T',
            tel='+9987188778877'
        )
        AkhmadjonClient = Customer(
            ssn=id_generator(),
            name=id_generator(),
            address='{}, {}, {}'.format(id_generator(1), id_generator(), id_generator()),
            ID=self.customer_id.get(),
            tel=id_generator(9),
            memberships=['Bronze']
        )

        RuziStaff = Staff(
            ssn=id_generator(),
            name=self.staff_name.get(),
            address='{}, {}, {}'.format(id_generator(1), id_generator(), id_generator()),
            job_id=id_generator(),
            job_title=id_generator(),
            salary=120
        )

        AbdulloOrder = Order(
            store=store,
            customer=AkhmadjonClient,
            staff=RuziStaff
        )

        if self.staff_name.get() is '' or self.customer_id.get() is '':
            self.warning_label['text'] = 'Please fill all fields'
            return False

        filtered_obj = [obj for obj in self.product_objects if obj.not_empty_fields()]

        for item in filtered_obj:
            if item.validate_empty(self.warning_label):
                product = Product(
                    product_code=int(item.product_code),
                    name=item.product_name,
                    description='Product of - {}'.format(id_generator()),
                    price=int(item.product_price),
                    points=int(item.product_point)
                )
                amount = int(item.product_qual)
                AbdulloOrder.add_product({"product": product, "amount": amount})

            else:
                self.warning_label['text'] = 'Please fill all fields'
                return False

        if not self.is_receipt_open:
            self.t = tk.Toplevel(self)
            self.t.wm_title("Receipt")
            self.t.protocol('WM_DELETE_WINDOW', self.on_receipt_close)
            self.draw_receipt(AbdulloOrder)
        self.is_receipt_open = True

    def draw_receipt(self, order):
        self.receipt_data = dict()
        receipt = self.receipt_data

        receipt['heading'] = tk.Label(
            self.t,
            pady=10,
            text='Welcome to {} Store Management System'.format(order.store.name),
            font='Helvetica 16 bold'
        )
        receipt['heading'].grid(row=0, columnspan=6, padx=30)

        # Frame for Staff and Customer Info
        receipt['staff'] = tk.Label(self.t, text='Staff Name: %s' % order.staff.name, padx=10)
        receipt['staff'].grid(row=1, column=0, sticky=tk.W)

        receipt['customer'] = tk.Label(self.t, text='Customer ID: %s' % order.customer.ID, padx=10)
        receipt['customer'].grid(row=2, sticky=tk.W)

        # product headers
        receipt['name_label'] = tk.Label(self.t, text='Product Name', pady=10)
        receipt['name_label'].grid(row=3, column=0)

        receipt['code_label'] = tk.Label(self.t, text='Product Code', pady=10)
        receipt['code_label'].grid(row=3, column=1)

        receipt['price_label'] = tk.Label(self.t, text='Price', pady=10)
        receipt['price_label'].grid(row=3, column=2)

        receipt['quant_label'] = tk.Label(self.t, text='Quantity', pady=10)
        receipt['quant_label'].grid(row=3, column=3)
        row = 4
        total_points = 0
        total_price = 0
        total_items = 0
        for index, obj in enumerate(order.products):
            row += index
            product = obj['product']
            amount = obj['amount']
            total_items += amount
            total_points = total_points + product.points
            total_price = total_price + (amount * product.price)
            tk.Label(self.t, text=product.name).grid(row=row, column=0)
            tk.Label(self.t, text=product.product_code).grid(row=row, column=1)
            tk.Label(self.t, text=product.price).grid(row=row, column=2)
            tk.Label(self.t, text=amount).grid(row=row, column=3)

        tk.Label(self.t, pady=10).grid(row=row + 1, sticky=tk.W)
        tk.Label(self.t, text='Total:    {}$'.format(total_price), padx=10).grid(row=row + 2, sticky=tk.W)
        tk.Label(self.t, text='Total items:    {}'.format(total_items), padx=10).grid(row=row + 3, sticky=tk.W)
        tk.Label(self.t, text='Points:    {}'.format(total_points), padx=10).grid(row=row + 4, sticky=tk.W)
        frame = tk.Frame(self.t)
        frame.grid(row=row + 5, sticky=tk.E, pady=10, column=3)
        tk.Button(frame, text='Close', padx=30, bg='lightgreen', fg='#fff', command=self.on_receipt_close).grid(row=0,
                                                                                                                column=3,
                                                                                                                sticky=tk.E)


def validate(in_str, acttyp):
    if acttyp == '1':  # insert
        if not in_str.isdigit():
            return False
    return True


# Class to easily control product input row

class ProductFrame():
    fields = ['product_name', 'product_code', 'product_price', 'product_qual', 'product_point']

    def __init__(self, frame, row):
        self.__product_name = tk.Entry(frame, borderwidth=1)

        self.__product_name.grid(row=row, column=0, padx=5, pady=2)

        validate_number = (frame.register(validate), '%P', '%d')

        self.__product_code = tk.Entry(frame, validate="key", validatecommand=validate_number)
        self.__product_code.grid(row=row, column=1, padx=5, pady=2)

        self.__product_price = tk.Entry(frame, validate="key", validatecommand=validate_number)
        self.__product_price.grid(row=row, column=2, padx=5, pady=2)

        self.__product_qual = tk.Entry(frame, validate="key", validatecommand=validate_number)
        self.__product_qual.grid(row=row, column=3, padx=5, pady=2)

        self.__product_point = tk.Entry(frame, validate="key", validatecommand=validate_number)
        self.__product_point.grid(row=row, column=4, padx=5, pady=2)

    @property
    def product_name(self):
        return self.__product_name.get()

    @property
    def product_code(self):
        return self.__product_code.get()

    @property
    def product_price(self):
        return self.__product_price.get()

    @property
    def product_qual(self):
        return self.__product_qual.get()

    @property
    def product_point(self):
        return self.__product_point.get()

    def not_empty_fields(self):
        vals = [self.product_code, self.product_name, self.product_qual, self.product_price, self.product_point]
        return not all(el == '' for el in vals)

    def validate_empty(self, label):
        vals = [self.product_code, self.product_name, self.product_qual, self.product_price, self.product_point]
        return all(vals)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    root.wm_title('Magnit')
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
