import mysql.connector as msc
from prettytable import PrettyTable
from art import tprint

con = msc.connect(host='localhost',user='root',password='12345',auth_plugin='mysql_native_password',database='Store')
if con.is_connected():
    print("Connection established...")
cursor = con.cursor()

class manage():
    def available(self):
        print("Available items:-")
        table = PrettyTable(['Item No.', 'Name','Quantity','Price'])
        cursor.execute("select * from Stock")
        result = cursor.fetchall()
        if result != None:
            for i in result:
                table.add_row(i)
        print("\n",table)
        con.commit()

    def add_item(self):
        print("Adding new items...")
        while True:
            cursor.execute("select * from stock order by Item_No desc limit 1")
            result = cursor.fetchall()
            i = result[0]
            item_no = i[0] + 1 # type: ignore
            name = input("Enter name of item : ")
            if name == 'q':
                break
            qty = int(input("Enter quantity : "))
            price = int(input("Enter price : "))
            cursor.execute(f"insert into stock values({item_no},'{name}',{qty},{price})")
            con.commit()

    def update_item(self):
        print("Updating items...")
        while True:
            choice = input("Do you want to update quantity or price : ")
            if choice == 'qty':
                item_no = int(input("Enter item number to update : "))
                qty = int(input("Enter updated quantity : "))
                cursor.execute(f"update Stock set Quantity=Quantity+{qty} where Item_No={item_no}")
                con.commit()
            
            elif choice == 'price':
                item_no = int(input("Enter item number to update : "))
                price = int(input("Enter updated price : "))
                cursor.execute(f"update Stock set Price=Price+{price} where Item_No={item_no}")
                con.commit()

            else:
                break

class customer():
    def order(self):
        bill = PrettyTable(['Item','Quantity','Price','Amount'])
        total = 0
        m = manage()
        m.available()
        while True:
            item_no = int(input("Enter item number : "))
            if item_no == 0:
                break
            qty = int(input("Enter quantity : "))
            
            cursor.execute(f"select Name from Stock where Item_No={item_no}")
            for i in cursor.fetchall():
                for j in i:
                    item = j
            
            cursor.execute(f"select Price from Stock where Item_No={item_no}")
            for i in cursor.fetchall():
                for j in i:
                    price = int(j) # type: ignore

            amount = price * qty
            total += amount
            cursor.execute(f"update stock set Quantity=Quantity-{qty} where Item_No={item_no}")
            con.commit()
            bill.add_row([item,qty,price,amount])

        bill.add_row(["","","",""])
        bill.add_row(["Total","","",total])
        c = customer()
        c.design()
        print(bill) 
        print('\nThanks for shopping with us \2 :)') 
        print('Your total bill amount is ₹', total) 

    def design(self):
        tprint("WELCOME  TO  THE  STORE")

while (1):
    choice = input("Who is using this (cust,mang) : ")
    if choice == 'mang':
        mang = manage()
        choice = int(input("Enter your choice:\n1 Show available items\n2 Add new items\n3 Update items\n"))
        if choice == 1:
            mang.available()
        
        elif choice == 2:
            mang.add_item()

        elif choice == 3:
            mang.update_item()

        else:
            print("Enter valid choice...")
    
    elif choice == 'cust':
        cust = customer()
        cust.order()

    else:
        print("Enter valid choice...")