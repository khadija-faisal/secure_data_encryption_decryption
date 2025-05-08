import hashlib
import streamlit as st # type: ignore #
from cryptography.fernet import Fernet # type: ignore
import json
import os

# defining logic in class (beckend only):
class SecureVault:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.store_data = {}
        self.data_file = "user_data.json"
        self.failure_attempt = 0
        self.attempt_limit = 3
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.store_data = json.load(file)

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.store_data, file, indent=4)
  
            
    def hash_key(self, passkey, username):
        salt = username.encode()
        hash_password = hashlib.pbkdf2_hmac("sha256", passkey.encode(), salt, 100000)
        return hash_password.hex()
    
    def verify_passkey(self, stored_hash, passkey,username):
        salt = username.encode()
        test_hash = hashlib.pbkdf2_hmac("sha256", passkey.encode(), salt, 100000).hex()
        return stored_hash == test_hash 

    def check_user(self, username, passkey):
        name = self.store_data.get(username)
    
        if not name:
             return "User does not exist. Please sign up first or enter a correct name."
        
        key = self.verify_passkey(name.get("hashed_key", ""), passkey, username) 
        if not key:
            self.failure_attempt +=1
            return "Incorrect passkey. Data not encrypted."
        
        if self.failure_attempt >= self.attempt_limit:
            return "too many attempts. please reauthorize! "
        return True
    

    def encrypt_data(self, data, username, passkey):
        
        user_check = self.check_user(username,passkey)
        
        if user_check is True:
            encrypt_text = self.fernet.encrypt(data.encode()).decode()
            self.store_data[username]["encrypted_text"] = encrypt_text
            self.store_data[username]["key"] = self.key.decode()
            self.save_data()
            return "Data encrypted and stored successfully."
        return user_check


    def decrypt_data(self, username, passkey):
        
        user_check = self.check_user(username,passkey)
        if user_check is True:

            encrypted_text = self.store_data.get(username, {}).get("encrypted_text", "")
            stored_key = self.store_data.get(username, {}).get("key", None) 

            if encrypted_text and stored_key:
                fernet = Fernet(stored_key.encode())
                decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
                self.failure_attempt = 0
                print(decrypted_text)
                return decrypted_text
            return "No encrypted data found for this user."
        return user_check





class UserAcount:

    def __init__(self, vault):
        self.vault  = vault

    def check_user(self, username):
        return username in self.vault.store_data
    
    def register_user(self, username, passkey):
        username = username.strip().lower()

        if self.check_user(username):
            return "username already exists. please choose a different username"
        hash_key = self.vault.hash_key(passkey, username)
        self.vault.store_data[username] = {
            "hashed_key" : hash_key,
            "encrypted_text": "",
            
        }
        self.vault.save_data()
        return "User Registered Successfully!"
    
    def login(self, username, passkey):
        username = username.strip().lower()

        if not username or not passkey:
          return "Username and password cannot be empty."

        if not self.vault.check_user(username,passkey):
            return "username not exists. please register first"
        
        stored_data = self.vault.store_data.get(username)

        if stored_data is None:
         return "User not found. Please register first."

        if not self.vault.verify_passkey(stored_data.get("hashed_key", ""), passkey, username):
          self.vault.failure_attempt += 1
          if self.vault.failure_attempt >= self.vault.attempt_limit:
            return "Too many attempts. Please reauthorize!"
          return "Incorrect passkey. Try again."
    
        self.vault.failure_attempt = 0  
        return "login successfully!"

       


        


    




