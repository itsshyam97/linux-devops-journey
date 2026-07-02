# 👥 Linux User Creation & Password Automation Script

This Bash script automates the creation of Linux users from a CSV file, generates secure random passwords, assigns administrative privileges, and emails the generated credentials using Gmail SMTP authentication via Postfix.

It is designed for Linux system administrators, DevOps engineers, and students who want to automate bulk user provisioning on RHEL/CentOS/AlmaLinux/Rocky Linux systems.

---

## ⚙️ Features

- Automatically installs all required dependencies.
- Configures Postfix to relay mail through Gmail SMTP.
- Configures SASL authentication for secure email delivery.
- Creates an **admins** group (if it doesn't already exist).
- Grants sudo privileges through `/etc/sudoers.d`.
- Reads usernames from a CSV file.
- Converts usernames to lowercase automatically.
- Generates secure 12-character random passwords using `pwgen`.
- Sets passwords for all users.
- Adds every user to the **admins** group.
- Creates a password report.
- Emails the password report as an attachment.
- Cleans up temporary files after execution.

---

# 📜 Script Overview

### **Filename**

```bash
user_creation.sh
```

### **Workflow**

| Step | Action |
|------|--------|
| 1 | Install required packages |
| 2 | Enable and configure Postfix |
| 3 | Configure Gmail SMTP relay |
| 4 | Configure SASL authentication |
| 5 | Create the `admins` group |
| 6 | Configure sudo privileges |
| 7 | Read usernames from `members.csv` |
| 8 | Generate secure passwords |
| 9 | Create Linux users |
| 10 | Assign passwords |
| 11 | Add users to the `admins` group |
| 12 | Generate password report |
| 13 | Email password report |
| 14 | Remove temporary files |

---

# 📦 Dependencies

The script automatically installs:

- epel-release
- pwgen
- s-nail
- postfix
- cyrus-sasl
- cyrus-sasl-lib
- cyrus-sasl-plain

---

# 📋 CSV Format

Create a file named:

```text
members.csv
```

Example:

```csv
ID,Name,Department
1,Alice Johnson,IT
2,Bob Smith,HR
3,Charlie Brown,Finance
4,David Miller,Support
```

The script extracts the **second column** (`Name`) and converts the first name to lowercase.

Example:

```
Alice Johnson
```

becomes

```
alice
```

---

# 📧 Gmail SMTP Configuration

This script uses Gmail as the SMTP relay.

Enable:

- Google 2-Step Verification
- Generate a Gmail App Password

Replace:

```text
YOUR_GMAIL@gmail.com
YOUR_APP_PASSWORD
```

inside:

```bash
/etc/postfix/sasl_passwd
```

Example:

```text
[smtp.gmail.com]:587 yourmail@gmail.com:abcdefghijklmnop
```

---

# 🧑‍💻 Usage

Make the script executable:

```bash
chmod +x user_creation.sh
```

Run as root:

```bash
sudo ./user_creation.sh
```

---

# 📁 Files Generated

During execution:

| File | Purpose |
|------|---------|
| members | Temporary username list |
| memberpw | Username/password report |

Both files are automatically removed after successful execution.

---

# 📨 Email Output

The script sends an email containing:

- Username/password report
- Attached `memberpw` file

Example subject:

```
User creation completed
```

---

# 🔑 Example Output

```
alice : hJ9#Lm2Pq8Ks
bob : vP7$Wr1Nx5Dt
charlie : Rm8@Xk3Qa6Lp
```

---

# 🛠️ Commands Used Internally

```bash
dnf install
systemctl
postconf
postmap
useradd
pwgen
chpasswd
usermod
mail
visudo
chmod
cut
tr
awk
```

---

# 📂 Project Structure

```
.
├── user_creation.sh
├── members.csv
├── README.md
```

---

# ⚠️ Prerequisites

- RHEL 9 / AlmaLinux 9 / Rocky Linux 9 / CentOS Stream 9
- Root privileges
- Internet connectivity
- Gmail account
- Gmail App Password
- Valid `members.csv`

---

# ⚠️ Notes

- Existing users are **not checked** by the script.
- Passwords are generated randomly every execution.
- Temporary files are deleted after email delivery.
- Store your Gmail App Password securely.
- This script is intended for trusted administrative environments.

---

# 🚀 Future Improvements

- Check if users already exist.
- Read email recipient from the command line.
- Support multiple user groups.
- Generate individual password PDFs.
- Log execution details.
- Improve error handling.
- Support other SMTP providers (Outlook, Zoho, Office365, etc.).

---

# 🧾 Author

**Shyam Prakash S**

*Linux System Administrator | DevOps Enthusiast | Automation & Scripting*

🌐 **LinkedIn:** https://linkedin.com/in/shyam-ps
