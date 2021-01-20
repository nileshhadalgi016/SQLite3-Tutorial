import sqlite3


# cur.execute('CREATE TABLE admin(username TEXT,password TEXT)')
# conn.commit()
# cur.execute("INSERT INTO admin VALUES('nilesh','nilesh')")
# conn.commit()

def verif_admin(username, password):
    try:
        conn = sqlite3.connect('SuperMarket.db')
        cur = conn.cursor()
        print(username)
        print(password)
        data = cur.execute('SELECT password FROM admin WHERE username = "{}"'.format(username)).fetchall()[0][0]

        conn.close()
        if password == data:
            return True
        else:
            return False
    except:
        return False


def add_product(id_, name, quantity, cost):
    if id_ == '' and name == '' and quantity == '' and cost == '':
        return False, " You Cannot Leave It Empty  "
    try:
        conn = sqlite3.connect('SuperMarket.db')
        cur = conn.cursor()
        print(id_, name, quantity, cost)
        try:
            quantity = int(quantity)
            cost = int(cost)
            print(id_, name, quantity, cost)
            print(type(id_), type(name), type(quantity), type(cost))
            check = cur.execute(f"SELECT * FROM products WHERE id = '{id_}'").fetchall()
            if len(check) > 0:
                return False, " This Product Already Exist Try Updating "
            else:
                cur.execute('INSERT INTO products VALUES("{}","{}",{},{})'.format(id_, name, quantity, cost))
                conn.commit()
                conn.close()
                return True, " Product Added Successfully "
        except:

            return False, " Quantity and Cost are Integers "

    except:

        return False, " Failed Connecting Database "


def get_product_detail(prod_id):
    if prod_id == '':
        return False, " Enter Product Id "
    else:
        conn = sqlite3.connect('SuperMarket.db')
        cur = conn.cursor()
        data = cur.execute(f"SELECT rowid,* FROM products where id='{prod_id}'").fetchall()
        conn.close()
        if len(data) == 0:
            return False, " Product Don't Exist "
        return True, data


def update_delete_product(rowid, id_, name, quantity, cost, qry):
    if id_ == '' and name == '' and quantity == '' and cost == '':
        return False, " You Cannot Leave It Empty  "
    try:
        conn = sqlite3.connect('SuperMarket.db')
        cur = conn.cursor()
        try:
            quantity = int(quantity)
            cost = int(cost)
            if qry == 'update':
                cur.execute(
                    f"UPDATE products SET id = '{id_}',name='{name}',quantity = {quantity},cost={cost} WHERE rowid = {rowid}")
                conn.commit()
                return True, " Product Updated Successfully "
            if qry == "delete":
                cur.execute(f"DELETE FROM products WHERE rowid={rowid} ")
                conn.commit()
                return True, " Product Deleted Successfully "
            conn.commit()
            conn.close()

        except:

            return False, " Quantity and Cost are Integers "
    except:
        return False, " Failed Connecting Database "


def showProducts_all():
    conn = sqlite3.connect('SuperMarket.db')
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM products").fetchall()
    return True, data


def added_to_cart(prod_id, qry):
    if prod_id == '':
        return False, " Please Enter Product Id ",1
    else:
        conn = sqlite3.connect('SuperMarket.db')
        cur = conn.cursor()
        if qry == "add":
            try:
                cur.execute("""CREATE TABLE cart(
                                id TEXT,
                                name TEXT,
                                quantity INTEGER,
                                cost INTEGER) """)
            except:
                pass

            data = cur.execute(f"""SELECT * FROM products WHERE id = '{prod_id}'""").fetchall()
            cart_check = cur.execute(f"""SELECT * FROM cart WHERE id = '{prod_id}' """).fetchall()
            if len(cart_check) == 0:
                cur.execute(f"""INSERT INTO cart VALUES('{data[0][0]}','{data[0][1]}',1,{data[0][3]})""")
                conn.commit()
                cur.execute(f"""UPDATE products SET quantity = {(data[0][2] - 1)} WHERE id ='{prod_id}'""")
                conn.commit()
                all_prods = cur.execute("SELECT * FROM cart").fetchall()
                return True, " Product Added To Cart Successfully ",all_prods

            elif len(cart_check) > 0:
                cur.execute(
                    f"""UPDATE cart SET quantity = {(cart_check[0][2] + 1)},cost={(cart_check[0][3] + data[0][3])} WHERE id ='{prod_id}'""")
                conn.commit()
                cur.execute(f"""UPDATE products SET quantity = {(data[0][2] - 1)} WHERE id ='{prod_id}'""")
                conn.commit()
                all_prods = cur.execute("SELECT * FROM cart").fetchall()
                return True, " Product Added To Cart Successfully ",all_prods


        if qry == "remove":

            cart_check = cur.execute(f"""SELECT * FROM cart WHERE id = '{prod_id}' """).fetchall()
            if len(cart_check) == 0:
                all_prods = cur.execute("SELECT * FROM cart").fetchall()
                return True," Product Doesn't Exist ",all_prods
            elif len(cart_check) > 0:
                data = cur.execute(f"""SELECT * FROM products WHERE id = '{prod_id}'""").fetchall()
                cur.execute(f"UPDATE products SET quantity = {(data[0][2]+cart_check[0][2])} WHERE id ='{prod_id}'")
                conn.commit()
                cur.execute(f"DELETE FROM cart WHERE id = '{prod_id}'")
                conn.commit()
                all_prods = cur.execute("SELECT * FROM cart").fetchall()
                return True," Product Deleted Successfully ",all_prods

        conn.close()


def get_cost():
    conn = sqlite3.connect('SuperMarket.db')
    cur = conn.cursor()
    data = cur.execute("SELECT * FROM cart").fetchall()
    cost = 0
    for i in data:
        cost = cost+i[3]
    return cost


def done_Drp():
    conn = sqlite3.connect('SuperMarket.db')
    cur = conn.cursor()
    cur.execute("DROP TABLE cart")
    conn.commit()

