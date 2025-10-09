🔐 Password Manager (Tkinter)

A simple yet powerful desktop password manager built with Python and Tkinter.
This application helps users generate, store, and search strong passwords securely in a local file.

✨ Features

✅ Random Password Generator – Creates secure, random passwords with a mix of letters, numbers, and symbols.
✅ One-Click Copy – Automatically copies the generated password to the clipboard using pyperclip.
✅ Data Storage (JSON) – Saves website, email/username, and password in a structured JSON file (data.json).
✅ Search Functionality – Instantly find saved credentials using the Search button.
✅ User-Friendly GUI – A clean and interactive interface built with Tkinter.
✅ Error Handling – Handles missing files or empty inputs gracefully with alerts.

🛠️ Technologies Used

🐍 Python 3

🪟 Tkinter – for the GUI interface

📋 pyperclip – to copy passwords to clipboard

🔢 random – for password generation

💾 json – for structured data storage

🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/KrishnaTeja8/Password-Manager.git

2️⃣ Install Dependencies
pip install pyperclip

3️⃣ Add an App Logo

Place a file named logo.png in the project directory (any 200x200 image works).

4️⃣ Run the Application
python main.py

📁 File Structure
📦 Password-Manager
├── main.py         # Main application code
├── data.json       # Stores saved credentials in JSON format
├── logo.png        # App logo
└── README.md       # Project documentation

🔮 Future Enhancements

🔒 Encrypt Stored Passwords – Add encryption for more security.
🔍 Advanced Search Filters – Filter results by website or username.
🗂️ Category Management – Organize credentials by account type (e.g., social, work, finance).
☁️ Cloud Sync – Optionally sync data securely to a cloud storage service.

🧩 Key Functionalities Snapshot
Feature	Description
Generate Password	Randomly creates a secure password
Copy to Clipboard	Instantly copies generated password
Add Entry	Saves credentials locally in data.json
Search	Finds and displays stored credentials
Error Alerts	Notifies if file/data is missing or invalid
👤 Author

Krishna Teja
💻 GitHub: @KrishnaTeja8

⭐ If you found this project useful, don’t forget to star the repository and share it!
