# 🔐 Secure Data Encryption System

A **Streamlit-based secure vault** application that allows users to register, log in, and **encrypt/decrypt sensitive data** using hashed passwords and symmetric encryption (Fernet).

---

## 📁 Project Structure

secure_data_encryption_system/
│
├── encrypt_decrypt.py # Core backend logic (vault + user account)
├── main.py # Streamlit frontend UI
├── user_data.json # File to store hashed keys and encrypted data
└── README.md # This file

yaml
Copy code

---

## 🚀 Features

- ✅ **User Registration & Login**  
- ✅ **Password Hashing with Salt (using PBKDF2 + SHA256)**  
- ✅ **Fernet-based Symmetric Encryption**  
- ✅ **Stores Encrypted Data in JSON**  
- ✅ **Attempt Limit for Login Security**  
- ✅ **Streamlit UI with Pages: Home, Register, Login, Store, Retrieve, Logout**  


---

## 📦 Dependencies

Install all requirements with:

```bash
pip install -r requirements.txt
requirements.txt
txt
Copy code
streamlit
cryptography
🛠️ How to Run
Clone the repository or download the code.

Open a terminal in the project folder.

Run the Streamlit app:

bash
Copy code
streamlit run main.py
🔑 Usage Instructions
Register:
Go to the "Register" page, choose a unique username and strong password.

Login:
Use your credentials on the "Login" page.

Store Data:
After logging in, go to "Store Data", enter your credentials again, and securely store sensitive information.

Retrieve Data:
Go to "Retrieve Data" to view your decrypted content after entering credentials.

Logout:
Securely log out of the session using the "Logout" option.


Clean sidebar navigation.

📌 Security Notes
Passwords are never stored directly, only hashed using salted PBKDF2.

Data is encrypted using Fernet with a unique session key.

JSON file stores user data but does not expose raw passwords or plaintext data.

🧑‍💻 Author
Khadija — Junior Frontend Developer | Python Enthusiast | Building real-world apps!

📬 Feedback
Feel free to reach out or fork this project to extend it! You can add:

Email-based recovery

Database integration (SQLite, MongoDB)

Multi-user sessions

UI improvements with animations

