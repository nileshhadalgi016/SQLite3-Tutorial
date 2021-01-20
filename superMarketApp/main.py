import database
from tkinter import *

flag = False


def addProduct_ui(app):
    app.destroy()
    add_p = Tk()
    add_p.attributes("-fullscreen", True)
    Label(add_p, text = " Product id :", font = (" ", 20)).place(x = 800, y = 400)
    Label(add_p, text = " Name       :", font = (" ", 20)).place(x = 800, y = 450)
    Label(add_p, text = " Quantity   :", font = (" ", 20)).place(x = 800, y = 500)
    Label(add_p, text = " Cost       :", font = (" ", 20)).place(x = 800, y = 550)

    product_id = Entry(add_p, font = ('', 20))
    product_name = Entry(add_p, font = ('', 20))
    product_quantity = Entry(add_p, font = ('', 20))
    product_cost = Entry(add_p, font = ('', 20))
    product_id.place(x = 900, y = 400)
    product_name.place(x = 900, y = 450)
    product_quantity.place(x = 900, y = 500)
    product_cost.place(x = 900, y = 550)
    pop_up = Label(add_p)
    pop_up.place(x = 800, y = 350)

    def verif_add():
        verif, text = database.add_product(product_id.get(), product_name.get(), product_quantity.get(),
                                           product_cost.get())
        if verif:
            pop_up.config(text = text)
            product_id.delete(0, 'end')
            product_name.delete(0, 'end')
            product_quantity.delete(0, 'end')
            product_cost.delete(0, 'end')


        else:
            pop_up.config(text = text)

    Button(add_p, text = " Add Product ", font = (" ", 20), command = lambda: verif_add()).place(x = 900, y = 600)
    Button(add_p, text = " Home ", font = (" ", 20), command = lambda: app_ui(add_p, "nilesh", "nilesh")).place(
        x = 1800, y = 1000)

    add_p.mainloop()


def update_delete_ui(app):
    app.destroy()
    up_del = Tk()
    up_del.attributes("-fullscreen", True)
    up_del.title("Show Products")

    Label(up_del, text = " Product id :", font = ('', 20)).place(x = 500, y = 100)
    enter_product_id = Entry(up_del, font = ('', 20))
    enter_product_id.place(x = 650, y = 100)

    def test():
        verif, data = database.get_product_detail(enter_product_id.get())
        pop_up = Label(up_del)
        pop_up.place(x = 800, y = 350)
        if verif:
            Label(up_del, text = " Product id :", font = (" ", 20)).place(x = 800, y = 400)
            Label(up_del, text = " Name       :", font = (" ", 20)).place(x = 800, y = 450)
            Label(up_del, text = " Quantity   :", font = (" ", 20)).place(x = 800, y = 500)
            Label(up_del, text = " Cost       :", font = (" ", 20)).place(x = 800, y = 550)

            product_id = Entry(up_del, font = ('', 20))
            product_id.delete(0, END)
            product_id.insert(0, data[0][1])

            product_name = Entry(up_del, font = ('', 20))
            product_name.delete(0, END)
            product_name.insert(0, data[0][2])

            product_quantity = Entry(up_del, font = ('', 20))
            product_quantity.delete(0, END)
            product_quantity.insert(0, data[0][3])

            product_cost = Entry(up_del, font = ('', 20))
            product_cost.delete(0, END)
            product_cost.insert(0, data[0][4])

            product_id.place(x = 900, y = 400)
            product_name.place(x = 900, y = 450)
            product_quantity.place(x = 900, y = 500)
            product_cost.place(x = 900, y = 550)

            def update_delete(qry):
                check, text = database.update_delete_product(data[0][0], product_id.get(), product_name.get(),
                                                             product_quantity.get(), product_cost.get(), qry)
                if check:
                    pop_up.config(text = text)
                else:
                    pop_up.config(text = text)
                if qry == "delete":
                    product_id.delete(0, 'end')
                    product_name.delete(0, 'end')
                    product_quantity.delete(0, 'end')
                    product_cost.delete(0, 'end')

            Button(up_del, text = " Update ", command = lambda: update_delete("update"), font = ("", 20)).place(x = 800,
                                                                                                                y = 600)
            Button(up_del, text = " Delete ", command = lambda: update_delete("delete"), font = ("", 20)).place(x = 900,
                                                                                                                y = 600)
        else:
            pop_up.config(text = data)

    Button(up_del, text = " Search ", command = lambda: test(), font = ("", 20)).place(x = 950, y = 100)
    Button(up_del, text = " Home ", font = (" ", 20), command = lambda: app_ui(up_del, "nilesh", "nilesh")).place(
        x = 1800, y = 1000)

    up_del.mainloop()


def showproducts_ui(app):
    check, data = database.showProducts_all()
    if check:
        app.destroy()
        import tkinter as tk
        from tkinter import ttk
        scores = tk.Tk()
        scores.attributes("-fullscreen", True)
        label = tk.Label(scores, text = " All Products ", font = ("Arial", 30)).place(x = 800, y = 100)
        cols = (' Product ID ', ' Product Name', ' Product Quantity ', ' Product Cost ')
        listBox = ttk.Treeview(scores, columns = cols, show = 'headings')
        style = ttk.Style()
        style.configure('Treeview.Heading', font = ("", 20))
        style.configure('Treeview', font = ("", 15))

        for col in cols:
            listBox.heading(col, text = col)
        listBox.place(x = 500, y = 150)

        check, data = database.showProducts_all()
        if check:
            for id_, name, quantity, cost in data:
                listBox.insert("", "end", values = (id_, name, quantity, cost))
        Button(scores, text = " Home ", font = (" ", 20), command = lambda: app_ui(scores, "nilesh", "nilesh")).place(
            x = 1800, y = 1000)
        scores.mainloop()


def pay_done(print_bill):
    database.done_Drp()
    app_ui(print_bill, "nilesh", "nilesh")

def print_bill_ui(bill):
    bill.destroy()
    print_bill = Tk()
    print_bill.attributes("-fullscreen", True)
    price = Label(print_bill,font=(" ",50))
    price.place(x = 400,y = 400)
    cost = database.get_cost()
    price.config(text = str(cost)+ ' RS')
    Button(print_bill, text = " Payment Done ", font = (" ", 20), command = lambda: pay_done(print_bill) ).place(
            x = 700, y = 700)
    print_bill.mainloop()


def make_bill_ui(app):
    app.destroy()
    import tkinter as tk
    from tkinter import ttk
    bill = Tk()
    bill.attributes("-fullscreen", True)
    Label(bill, text = " Product id :", font = ('', 20)).place(x = 500, y = 100)
    enter_product_id = Entry(bill, font = ('', 20))
    enter_product_id.place(x = 650, y = 100)

    def cart_add_fuc(qry):
        check, text, details = database.added_to_cart(enter_product_id.get(), qry)
        if check:
            cols = (' Product ID ', ' Product Name', ' Product Quantity ', ' Product Cost ')
            listBox = ttk.Treeview(bill, columns = cols, show = 'headings')
            style = ttk.Style()
            style.configure('Treeview.Heading', font = ("", 20))
            style.configure('Treeview', font = ("", 15), rowheight = 80)

            for col in cols:
                listBox.heading(col, text = col)
            listBox.place(x = 500, y = 150)

            if check:
                for id_, name, quantity, cost in details:
                    listBox.insert("", "end", values = (id_, name, quantity, cost))

            Button(bill, text = " Print Bill  ", font = (" ", 20), command = lambda: print_bill_ui(bill)).place(
        x = 900, y = 1000)

    Button(bill, text = " Add To Cart ", command = lambda: cart_add_fuc("add"), font = ("", 20)).place(x = 950, y = 100)
    Button(bill, text = " Remove ", command = lambda: cart_add_fuc("remove"), font = ("", 20)).place(x = 1150, y = 100)
    Button(bill, text = " Home ", font = (" ", 20), command = lambda: app_ui(bill, "nilesh", "nilesh")).place(
        x = 1800, y = 1000)

    bill.mainloop()


def app_ui(login, username, password):
    auth_check = database.verif_admin(username, password)
    if auth_check:
        login.destroy()
        app = Tk()
        app.attributes("-fullscreen", True)
        app.title("home Page")
        Button(app, text = "add Product", font = (" ", 20), command = lambda: addProduct_ui(app)).place(x = 900,
                                                                                                        y = 400)
        Button(app, text = " Update / Delete Product ", font = (" ", 20),
               command = lambda: update_delete_ui(app)).place(x = 900,
                                                              y = 450)
        Button(app, text = " Show All Products ", font = (" ", 20), command = lambda: showproducts_ui(app)).place(
            x = 900,
            y = 500)
        Button(app, text = " Make A Bill ", font = (" ", 20), command = lambda: make_bill_ui(app)).place(x = 900,
                                                                                                         y = 550)
        Button(app, text = "Quit", font = (" ", 20), command = lambda: quit()).place(x = 1800, y = 1000)
        app.mainloop()


    else:
        print(username)
        print(password)
        login.destroy()
        global flag
        flag = True
        login_ui()


def login_ui():
    login = Tk()
    login.attributes("-fullscreen", True)
    login.title("log-in")
    Label(login, text = "SuperMarket", font = (' ', 50)).place(x = 900, y = 400)
    Label(login, text = "Username :", font = (' ', 20)).place(x = 900, y = 500)
    Label(login, text = "Password :", font = (' ', 20)).place(x = 900, y = 550)
    if flag:
        Label(login, text = " incorrect Username / Password ", font = ("", 20)).place(x = 900, y = 650)
    enter_username = Entry(login, width = 10)
    enter_username.place(x = 1010, y = 500)
    enter_password = Entry(login, width = 10, show = "*")
    enter_password.place(x = 1010, y = 550)
    Button(login, text = "Login", font = (" ", 20), command = lambda: app_ui(login, enter_username.get(),enter_password.get())).place(x = 1000,
                                                                                                               y = 600)
    Button(login, text = "Quit", font = (" ", 20), command = lambda: quit()).place(x = 1800, y = 1000)
    login.mainloop()


if __name__ == '__main__':
    login_ui()
