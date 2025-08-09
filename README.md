# 🔍 Password Analyzer

A Python tool to *analyze password strength* and *generate secure passwords*.  
This project was built with a focus on *cybersecurity best practices* and *clean code*.

---

## 📌 Features
- Analyze password strength based on:
  - Length
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- Provide feedback for weak and medium passwords
- Generate secure random passwords
- Simple and user-friendly CLI interface

---

## 🖥 How It Works
1. The user inputs a password.
2. The program analyzes it and returns:
   - *Strength level* (Weak, Medium, Strong)
   - *Feedback* on how to improve it
3. The user can choose to generate a new secure password.

---

## 📷 Example Output


=== Password Strength Analyzer ===
Enter a password to analyze: Hello123

Strength: 🟡 Medium
Your password is okay, but could be stronger: Add at least one special character.

Do you want to generate a secure password? (y/n)
y
Generated Secure Password: ^p!X2A9zQw#E


---

## 🚀 Installation & Usage
1. *Clone the repository*
bash
git clone https://github.com/joudsembabi-tech/password-analyzer.git


2. *Navigate to the project folder*
bash
cd password-analyzer


3. *Run the program*
bash
python password_analyzer.py


---

## 🎯 Future Improvements
- Add password breach check using HaveIBeenPwned API
- Create a GUI version
- Support multi-language output

---

## 🛡 Author
*Joud Sembabi*  
Passionate about *Cybersecurity* and *Python development*.
