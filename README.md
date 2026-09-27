Secure Password Strength Analyzer

A web-based academic project that analyzes password characteristics and provides an estimated password strength, entropy value, security checks, and recommendations for improvement.


Objective
The objective of this project is to develop a tool that evaluates password strength by analyzing:

Password length
Lowercase letters
Uppercase letters
Numbers
Special characters
Common password patterns
Sequential patterns
Repeated characters
Estimated entropy
A project-specific strength score
Recommendations for improving password security


Features

Password length analysis
Character composition analysis
Common password detection
Sequential pattern detection such as abc or 123
Repeated character detection
Estimated entropy calculation
Strength score from 0–10
Strength categories: Weak, Moderate, Strong, Very Strong
Security recommendations
Dynamic result panel that changes appearance according to the detected strength
Passwords are processed in memory and are not intentionally stored by the application


Technologies Used

Python – backend logic
Flask – Python web framework
HTML – webpage structure
CSS – webpage styling
Jinja2 – dynamic HTML rendering through Flask


Project Structure

Secure-Password-Strength-Analyzer/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css


How the Analyzer Works

The user enters a test password in the web interface.
Flask receives the submitted password.
The Python backend analyzes the password.
The application checks its length and character composition.
It checks for common passwords, sequential patterns, and repeated characters.
An estimated entropy value is calculated.
A project-specific score from 0 to 10 is generated.
The password is classified as Weak, Moderate, Strong, or Very Strong.
The application displays recommendations to improve the password.


Strength Score

The project uses a simple heuristic scoring system for demonstration purposes.
The score considers:
Password length
Lowercase letters
Uppercase letters
Numbers
Special characters
Common password detection
Sequential patterns
Repeated characters
Longer passwords receive additional points in the project-specific scoring system.
Entropy
The application provides a simplified entropy estimate using:
Entropy = Password Length × log2(Character Set Size)
The character set size is estimated from the types of characters detected in the password.
This is an educational estimate and should not be treated as a guarantee of real-world password security.


Running the Project Locally

1. Open the project folder
Open the Secure-Password-Strength-Analyzer folder in VS Code.

2. Activate the virtual environment
On Windows PowerShell:
.venv\Scripts\Activate.ps1

3. Install dependencies
python -m pip install -r requirements.txt

4. Run the Flask application
python app.py

5. Open the application

Open the local address shown by Flask, normally:
http://127.0.0.1:5000/


Important Security Note

Do not enter real passwords, banking passwords, email passwords, college passwords, or other sensitive credentials into this academic application.

Use only fake/test passwords when demonstrating the project.


Limitations

This project is designed as an academic demonstration. It has several limitations:
The common-password database is a small built-in educational list.
Sequential-pattern detection is simplified.
Repeated-character detection is simplified.
The entropy calculation is an estimate based on the detected character set.
The 0–10 strength score is a project-specific heuristic and is not an official password-strength standard.
The application does not perform a real password-cracking simulation.
The tool cannot guarantee that a password is secure.


Future Enhancements

Possible future improvements includes
Using a larger compromised/common-password database
More advanced pattern detection
Detection of dictionary words and personal information
More sophisticated password-strength estimation
Privacy-preserving password breach checking
Improved accessibility and responsive design
Additional password-generation functionality


Academic Project

Project: Secure Password Strength Analyzer

This project was developed as an academic project to demonstrate concepts related to password security, web development, Python programming, and basic security analysis.


 