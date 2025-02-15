# Pararius Property Scraper  

This project scrapes property listings from Pararius and sends email alerts when new properties are found. It allows the separation of sensitive information like email credentials, passwords, and URLs to ensure secure handling. This README will guide you through setting up the project.

## Features
- Scrapes property listing information from Pararius based on filters.
- Sends email notifications for new property listings.
- Secure configuration using external files for sensitive data.

---

## How to Set Up

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/pararius-scraper.git
cd pararius-scraper
```

---

### 2. Create a Configuration File (Option 1: `config.json`)

Store sensitive information in a separate `config.json` file. Create this file in the project root directory.

#### Example: `config.json`
```json
{
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "email_from": "your_email@gmail.com",
    "email_to": ["recipient1@example.com", "recipient2@example.com"],
    "login_email": "your_email@gmail.com",
    "login_password": "your_app_specific_password",
    "pararius_login_url": "https://www.pararius.com/login",
    "pararius_login_payload": {
        "username": "your_email@gmail.com",
        "password": "your_pararius_password"
    }
}
```

Add `config.json` to your `.gitignore` file to prevent committing it to version control:
```plaintext
config.json
```

---

### 3. (Alternative) Use Environment Variables (Option 2: `.env`)

Instead of placing sensitive data in a file, you can use environment variables. Create a `.env` file in the project root directory. Install the `python-dotenv` library to handle environment variables.

#### Install `python-dotenv`
```bash
pip install python-dotenv
```

#### Example: `.env` File
```plaintext
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_FROM=your_email@gmail.com
EMAIL_TO=recipient1@example.com,recipient2@example.com
LOGIN_EMAIL=your_email@gmail.com
LOGIN_PASSWORD=your_app_specific_password
PARARIUS_LOGIN_URL=https://www.pararius.com/login
PARARIUS_USERNAME=your_email@gmail.com
PARARIUS_PASSWORD=your_pararius_password
```

Add `.env` to your `.gitignore` file:
```plaintext
.env
```

---

### 4. Configure the Code

The code is already set up to load sensitive information dynamically. It will check for a `config.json` file or `.env` file depending on your chosen setup.

---

### 5. Run the Script

Run the scraper using:
```bash
python pararius-scraper.py
```

---

## Handling Sensitive Data

- **Never hardcode sensitive data such as passwords or API keys into the source code.**
- Use `config.json` or environment variables (`.env`) for storing sensitive information securely.
- Ensure the `config.json` or `.env` file is excluded from version control by adding it to `.gitignore`.

---

## Troubleshooting

1. **Emails not sent?**
   - Check that you have set up an [App Password](https://support.google.com/accounts/answer/185833?hl=en) for your Gmail account.
   - Make sure the SMTP configuration (`smtp_server`, `smtp_port`) is correct.

2. **Login to Pararius failed?**
   - Verify your Pararius login credentials in the `pararius_login_payload` or `.env` file.

3. **Environment variable issues?**
   - Ensure you have installed the `python-dotenv` library if using a `.env` file.

---

## Contributions
Feel free to fork this repository, create a branch with your changes, and submit a pull request. PRs are welcome!

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
