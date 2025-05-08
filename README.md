🔐 Secure Data Encryption System
A simple yet powerful Streamlit-based app that allows users to securely register, login, encrypt, and retrieve sensitive personal data using industry-standard encryption (Fernet, PBKDF2). The app emphasizes data privacy, authentication, and a clean user experience.

🚀 Features
🔏 User Registration & Login
Securely register with a username and password. Passwords are hashed using PBKDF2_HMAC.

🧠 User Authentication
Prevent brute force with limited login attempts and salt-based hashing.

🧊 Data Encryption & Decryption
Sensitive data is encrypted using Fernet (symmetric encryption).

🗃 Persistent Storage
Encrypted data is stored in a local JSON file (user_data.json).

🎨 Beautiful Streamlit UI
Includes navigation, and a clean sidebar.

🛠️ Tech Stack
Tool	Purpose
Python	Core backend logic
Streamlit	Web app UI
Cryptography	Secure encryption (Fernet)
Hashlib	Password hashing (PBKDF2_HMAC)
JSON	Lightweight local storage

📂 Project Structure
bash
Copy code
secure_data_encryption_system/
│
├── encrypt_decrypt.py        # Core backend logic (Vault & User classes)
├── main.py                   # Streamlit app entry point
├── user_data.json            # Encrypted user data storage
├── .venv/                    # Virtual environment (recommended)
└── README.md                 # Project documentation
🧪 How to Run
Clone the repository

bash
Copy code
git clone https://github.com/your-username/secure-data-encryption-system.git
cd secure-data-encryption-system
Set up a virtual environment (optional but recommended)

bash
Copy code
python -m venv .venv
source .venv/bin/activate      # On macOS/Linux
.venv\Scripts\activate         # On Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app

bash
Copy code
streamlit run main.py
.

This project is for educational/demo use. For production-level apps, consider database storage, key vaults, and secure authentication layers.

🙌 Author
Khadija – Junior Frontend Developer & Graphic Designer

Empowering users to protect their data, one key at a time.

