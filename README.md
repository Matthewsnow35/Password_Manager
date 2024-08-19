# Password Manager

## Project Overview

This Password Manager is a simple application designed to store and manage passwords securely. It allows users to add, view, and delete passwords associated with various services. The passwords are encrypted to ensure their security. The application is currently a command-line tool, but there are plans to enhance it with additional features and a graphical user interface.

## Features

- **Add New Password**: Securely store new passwords for various services.
- **View Stored Passwords**: Display stored passwords in an encrypted format.
- **Delete Password**: Remove passwords from the storage.
- **Encryption**: Passwords are encrypted using the `cryptography` library to protect them from unauthorized access.

## Future Enhancements

1. **Master Password**
   - **Plan**: Implement a master password feature to secure access to the application. Users will need to enter the master password to access or modify stored passwords.
   - **Implementation**: Prompt for a master password at application startup, and validate this password before allowing access to the main features.

2. **Improved User Interface**
   - **Plan**: Transition from a command-line interface to a graphical user interface (GUI) for a more user-friendly experience.
   - **Implementation**: Develop the GUI using libraries such as `Tkinter` or `PyQt`, featuring input fields, buttons, and dialogs for interacting with the password manager.

3. **Password Strength Validation**
   - **Plan**: Ensure that users create strong and secure passwords.
   - **Implementation**: Add validation checks during password creation to enforce rules such as minimum length and inclusion of special characters.

4. **Password Generator**
   - **Plan**: Provide users with a tool to generate strong passwords.
   - **Implementation**: Add a feature to generate random, secure passwords that users can use for their services.

5. **Secure Key Management**
   - **Plan**: Improve the management of the encryption key to enhance security.
   - **Implementation**: Explore secure key storage options or use environment variables to manage the encryption key securely.

6. **Logging and Monitoring**
   - **Plan**: Track user actions for security audits and debugging.
   - **Implementation**: Implement logging to record significant actions, such as adding, viewing, or deleting passwords.

7. **Error Handling and Validation**
   - **Plan**: Improve application robustness by handling errors and validating user inputs.
   - **Implementation**: Add error handling for file operations and input validation to prevent misuse.

8. **Documentation**
   - **Plan**: Provide comprehensive documentation to assist users and developers.
   - **Implementation**: Update the README file with detailed instructions and guidelines for using and contributing to the project.

## Installation and Setup

1. **Clone the Repository**

   ```bash
   git clone <repository-url>

2. **Navigate to the Project Directory**

   ```bash
   cd password-manager

3. **install Dependencies**

   Ensure you have Python and cryptography installed. You can install cryptography using pip:

   ```bash
   pip install cryptography

4. **Run the Application**

   Execute the script to start the password manager:   
   ```bash
   python password_manager.py


## Usage

1. **Add a New Password**

   Select option 1 and follow the prompts to add a password.

2. **View Stored Passwords**

   Select option 2 to view the list of stored passwords.

3. **Delete a Password**

   Select option 3 to delete a specific password.

4. **Exit the Application**

   Select option 4 to exit the application. Your passwords will be saved automatically.


## Security Considerations

   Encryption: Passwords are encrypted using the cryptography library. The encryption key is stored in a file (secret.key), which should be kept secure.
   Master Password: Future updates will include a master password feature to enhance security.


## Contributing

   Contributions are welcome! If you have suggestions or improvements, please submit a pull request or open an issue on the project's GitHub repository.   


## License

   This project is licensed under the MIT License. See the LICENSE file for details.


## Contact
  For any questions or support, please contact:

  Email: Matthewsnow35@gmail.com
  GitHub: Matthewsnow35
  
