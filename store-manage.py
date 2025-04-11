import mysql.connector as msc
from prettytable import PrettyTable
from art import tprint
import cv2
from pyzbar.pyzbar import decode
import warnings
import datetime
import os

warnings.filterwarnings("ignore")


con = msc.connect(host='localhost',user='root',password='12345',database='Store')
if con.is_connected():
    print("Connection established...")
cursor = con.cursor()

def scan():
    try:
        cam = cv2.VideoCapture("http:192.168.1.10:4747/video")
        cam.set(3, 640)
        cam.set(4, 480)
        item_no = None

        while True:
            success, frame = cam.read()
            if not success:
                break

            for barcode in decode(frame):
                item_no = barcode.data.decode('utf-8')
                print(f"Item No: {item_no}")
                cam.release()
                cv2.destroyAllWindows()
                return item_no
            cv2.imshow("QR Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release()
        cv2.destroyAllWindows()
        return item_no
    except Exception as e:
        print(f"Error during scanning: {e}")

class manage():
    def available(self):
        print("Available items:-")
        table = PrettyTable(['Item No.', 'Name','Quantity','Price'])
        cursor.execute("select * from Stock")
        result = cursor.fetchall()
        if result != None:
            for i in result:
                table.add_row(i) # type: ignore
        print("\n",table)
        con.commit()

    def add_item(self):
        print("Adding new items...")
        while True:
            try:
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
            except ValueError as e:
                print(f"Invalid input: {e}")
            except msc.Error as e:
                print(f"Database error: {e}")
            except Exception as ex:
                print(f"An unexpected error occurred: {ex}")
            finally:
                cursor.close()

    def update_item(self):
        print("Updating items...")
        while True:
            try:
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
            except msc.IntegrityError as ie:
                con.rollback()
                print(f"Data integrity error: {ie}")
            except msc.ProgrammingError as pe:
                con.rollback()
                print(f"Programming error (check your SQL syntax): {pe}")
            except msc.Error as e:
                con.rollback()
                print(f"Database error: {e}")
            except ValueError as ve:
                print(f"Invalid input: {ve}")
            finally:
                cursor.close()

class customer():
    def order(self):
        bill = PrettyTable(['Item','Quantity','Price','Amount'])
        total = 0
        m = manage()
        try:
            m.available()
            while True:
                item_no = scan()
                if item_no == 'q' or item_no == 'Q':
                    break
                
                cursor.execute(f"select Name from Stock where Item_No={item_no}")
                for i in cursor.fetchall():
                    for j in i:
                        item = j
                print(item)        
                qty = int(input("Enter quantity : "))
                
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
            print(f'Your total bill amount is ₹{total}')
            self.save_bill(bill, total)
        except msc.Error as e:
            con.rollback()
            print(f"Database error occurred: {e}")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
        finally:
            cursor.close()

    def design(self):
        tprint("WELCOME  TO  THE  STORE")

    def save_bill(self, bill_table, total):
        now = datetime.datetime.now()
        folder = "bills"
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(folder, f"bill_{now.strftime('%Y%m%d_%H%M%S')}.txt")
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("WELCOME TO THE STORE\n")
                file.write(now.strftime("Date: %Y-%m-%d   Time: %H:%M:%S\n\n"))
                file.write(str(bill_table))
                file.write(f"\n\nTotal Amount: ₹{total}\n")
                file.write("Thanks for shopping with us!\n")
            print(f"Bill saved as '{filename}'")
        except Exception as e:
            print(f"Could not save bill: {e}")

while (1):
    choice = input("Who is using this (cust,mang) : ")
    if choice == 'mang':
        mang = manage()
        choice = int(input("Enter your choice:\n1 Show available items\n2 Add new items\n3 Update items\n4 Exit\n"))
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

    elif choice == 'q':
        break
    
    else:
        print("Enter valid choice...")
