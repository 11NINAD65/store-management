import mysql.connector as msc
from prettytable import PrettyTable

con = msc.connect(host='localhost',user='root',password='12345',auth_plugin='mysql_native_password',database='Store')
if con.is_connected():
    print("Connection established...")
cursor = con.cursor()


def avb_items():
    print("Available items :-")
    print("Item_No\tItem_Name\tQuantity\tPrice")
    cursor.execute("select * from Stock")
    result = cursor.fetchall()
    if result != None:
        for i in result:
            # for j in i:
            #     print(j,end="\t")
            # print("\n")
            print(i)

def option():
    print("What do you want to do :-\n1. Add items to store\t\t2. Place order\t\t3. Show available items")
    choice = int(input())

    if choice == 1:
        print("Adding items...")
        add_items()
        con.commit()

    elif choice == 2:
        print("Placing orders...")
        order()
        con.commit()

    elif choice == 3:
        avb_items()

    else:
        print("Enter valid option b/w 1 and 2")
        option()

def add_items():
    upd_or_add = input("Do you want to update or add new item (update/add) :")

    if upd_or_add=='update':
        avb_items()
        item_no = int(input("Enter item number to update : "))
        qty = int(input("Enter quantity : "))
        cursor.execute(f"update Stock set Quantity=Quantity+{qty} where Item_No={item_no}")
        avb_items()
    
    elif upd_or_add=='add':
        avb_items()
        item_no = int(input("Enter item number : "))
        item_name = input("Enter item name : ")
        qty = int(input("Enter quantity : "))
        price = int(input("Enter price of item : "))
        cursor.execute(f"insert into stock(Item_No,Item_Name,Quantity,Price) values({item_no},'{item_name}',{qty},{price})")
        avb_items()

def order():
    avb_items()
    print("Enter 0 to stop.")
    
    bill = open('C:\\Users\\ninad\\OneDrive\\Desktop\\PY\\Store\\store.txt','w')
    bill.write(f"Item\t\tQuantity\tPrice\tAmount")
    total = 0
    while True:
        item_no = int(input("Enter item no. : "))
        if item_no==0:
            break
        qty = int(input("Enter quantity : "))
        
        cursor.execute(f"select Item_Name from stock where Item_No={item_no}")
        result = cursor.fetchall()
        # if result != None:
        for i in result:
            for j in i:
                item_name=j
        cursor.execute(f"select Price from stock where Item_No={item_no}")
        result = cursor.fetchall()
        # if result != None:
        for i in result:
            for j in i:
                price=j
        amount=qty*price
        bill = open('C:\\Users\\ninad\\OneDrive\\Desktop\\PY\\Store\\store.txt','a')
        bill.write(f"\n{item_name}\t\t{qty}\t\t\t{price}\t\t{amount}")
        total += amount
        cursor.execute(f"update stock set Quantity=Quantity-{qty} where Item_No={item_no}")
    bill.write(f"\n\nTotal\t\t\t\t\t\t\t\t{total}")    
    bill.close()


while True:
    option()
    ch = input("Do you want to stop (y/n) : ")
    if ch == 'y':
        break