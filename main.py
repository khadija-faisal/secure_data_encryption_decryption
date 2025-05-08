from encrypt_decrypt import SecureVault, UserAcount
import streamlit as st # type: ignore #
# type: ignore

def show_home():
    st.markdown(
        """
        <div style="text-align:center;">
            <h1 style='color:#4CAF50;'>🔐 Welcome to Secure Data Vault</h1>
            <p style='font-size:18px;'>Keep your secrets safe with encryption 🔒</p>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <div style="margin-top: 30px;">
            <h3>🌟 Features:</h3>
            <ul style="font-size:16px;">
                <li>Secure data encryption using <code>Fernet</code></li>
                <li>Easy-to-use interface for storing and retrieving information</li>
                <li>Password-protected access to your vault</li>
                <li>Personalized encryption key for each user</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Get started by navigating to the sidebar ➡️")

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; color:gray;'>Developed with ❤️ by Khadija</p>",
        unsafe_allow_html=True
    )

def main():
    secure_vault = SecureVault()
    user_account = UserAcount(secure_vault)

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""


    menu = ["Home", "Register", "Login"]
    if st.session_state.logged_in:
         menu.extend(["Store Data", "Retrieve Data", "Logout"])

    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
       show_home()

    elif choice == "Register":
        st.subheader("User Registration 👤")
        user_name = st.text_input("Enter your Username: ")
        password = st.text_input("Enter your Password:", type="password")
        if st.button("Register"):
            save_details = user_account.register_user(user_name, password)
            st.write(save_details)

    elif choice == "Login":
        st.subheader("User Login 👤")
        user_name_login = st.text_input("Enter your UserName:")
        password_login = st.text_input("Enter your Password:", type="password")
        if st.button("login In"):
          check_user_details = user_account.login(user_name_login, password_login)
        
          st.write(check_user_details)
          if check_user_details == "login successfully!":
             st.session_state.logged_in = True
             st.session_state.username = user_name_login
             st.rerun()
        

    elif choice == "Store Data":
        if st.session_state.logged_in:
          st.subheader("Store Your Private Data 🔐")
          user_name_enter_data = st.text_input("Enter your username: ")
          password_enter_data = st.text_input("Enter your registered Password", type="password")
          data = st.text_area("Enter your Sensitive data")
          if st.button("Store Data"):
           store_data = secure_vault.encrypt_data(data,  user_name_enter_data, password_enter_data)
           st.write(store_data)
        else:
            st.warning("please Login First to Store Data")
    
    elif choice == "Retrieve Data":
        if st.session_state.logged_in:
           st.subheader("Get Your Private Data 🔓")
           user_name_get_data = st.text_input("Enter your user name ")
           password_get_data = st.text_input("Enter your Registered Password: ", type="password")
           if st.button("Retrieve Data"):
             get_data = secure_vault.decrypt_data(user_name_get_data, password_get_data)
             if get_data:
                user_account.failure_attempts = 0
                st.write(get_data)
             else:
                st.session_state["redirect_to_login"] = True
                st.experimental_rerun()
                st.write("Invalid username or passkey")
        else: 
            st.warning("Please log in first to retrieve data.")

    elif choice == "Logout":
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.success("You have been logged out.")
        st.rerun()
    


if __name__ == "__main__":
    main()





        
    
    