# 🛒 Store Management System with QR Scanner & Billing

A Python-based store management application designed for retail environments. This system enables real-time product scanning using QR codes via webcam or IP camera, automated billing, and inventory management — all in a command-line interface.

---

## ✨ Features

- 📷 **QR Code Scanning** using webcam or mobile IP camera
- 📦 **Inventory Management** (Add, update, list products)
- 🧾 **Customer Billing System** with itemized bills
- 💾 **Auto-Save Bills** with timestamped receipts to local folder
- 📊 **PrettyTable Output** for neat, readable data display
- 🔐 **MySQL Database Integration** with safe and efficient queries
- 🎨 **ASCII Terminal Art** using `art` module
- 🔁 **Real-time Stock Validation** during purchases

---

## 🛠️ Technologies Used

- **Python 3**
- **MySQL** (with `mysql-connector-python`)
- **OpenCV** (`cv2`)
- **pyzbar** (for decoding QR codes)
- **PrettyTable** (for table formatting)
- **ASCII Art** (`art` library)
- `datetime`, `os`, `warnings`, and other standard Python modules

---

## 📸 How It Works

- **QR Scanning:** Uses webcam or mobile IP camera (via apps like DroidCam) to scan QR codes attached to products.
- **Stock Handling:** Store owners can add, view, and update stock using simple menu options.
- **Billing:** Automatically generates a bill table and calculates total.
- **Saving Bills:** Saves a text file of the customer's bill with the date and time in a `/bills` folder.

---

## 🚀 Setup Instructions

### 🔧 Requirements

- Python 3.x  
- MySQL Server  
- Python Libraries:  
  ```bash
  pip install mysql-connector-python opencv-python pyzbar prettytable art
  ```

### 🧱 Database Setup

1. Open your MySQL terminal or use a tool like phpMyAdmin.
2. Run the following SQL to create the database and table:

```sql
CREATE DATABASE Store;
USE Store;

CREATE TABLE Stock (
  Item_No INT PRIMARY KEY,
  Name VARCHAR(100),
  Quantity INT,
  Price INT
);
```

---

### ▶️ Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/11NINAD65/store-management.git
   cd store-management
   ```

2. Open and run the main Python file:
   ```bash
   python store_management.py
   ```

3. Choose a user role:
   - `mang` for manager
   - `cust` for customer
   - `q` to quit

---

## 📁 Sample QR Scanning Setup if you don't have Webcam

To scan using a **mobile camera**:
1. Download **DroidCam** on your phone and PC.
2. Connect both devices to the same network.
3. Use the IP camera URL like:  
   ```
   http://192.168.X.X:4747/video
   ```
4. Update the `cam = cv2.VideoCapture(...)` line in the script accordingly.

---

## 📌 Project Structure

```
store-management/
│
├── bills/                 # Folder where generated bills are saved
├── store_management.py    # Main script with all functionality
└── README.md              # Project documentation
```

---

## 🧠 Skills Demonstrated

- Python programming and OOP
- SQL and MySQL integration
- OpenCV and image decoding
- Command-line interface design
- Error handling and user validation
- File handling and data persistence

---

## 🙌 Acknowledgements

- [OpenCV](https://opencv.org/)
- [pyzbar](https://pypi.org/project/pyzbar/)
- [PrettyTable](https://pypi.org/project/PrettyTable/)
- [art](https://pypi.org/project/art/)
- ASCII Text Art by `art` for terminal branding

---

## 🔗 Connect

Built with ❤️ by [Ninad](https://github.com/11NINAD65)  
Feel free to ⭐️ the repo if you found it useful!
