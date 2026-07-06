#!/bin/bash

# Create admins group if it doesn't exist
getent group admins >/dev/null || groupadd admins

# Add sudo rule if not already present
grep -q "^%admins" /etc/sudoers || \
echo "%admins ALL=(ALL:ALL) ALL" >> /etc/sudoers

# Extract names, convert to lowercase
cut -d, -f2 members.csv | tail -n +2 | tr '[:upper:]' '[:lower:]' | awk '{print $1}' > members

# Password file
> memberpw

while read -r user; do
    # Create user
    useradd "$user"

    # Generate password
    pw=$(pwgen -s 12 1)

    # Set password
    echo "$user:$pw" | chpasswd

    # Add user to admins group
    usermod -aG admins "$user"

    # Save username and password
    echo "$user : $pw" >> memberpw

done < members

# Email the password file
mail -s "User creation completed" prakashshyam.sps@gmail.com < memberpw

echo "All users created successfully."
