#!/bin/bash

# Ensure the script is run as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# 1. Disable password-based authentication.


# Backup the original sshd_config file
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak

# 1. Disable password authentication
echo ">>> Disabling password-based authentication..."
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config

# 2. Disable root account remote login.

echo ">>> Disabling root account remote login..."

# Disable root login
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/g' /etc/ssh/sshd_config

# 3. Limit maximum number of SSH authentication attempts.

echo ">>> Limiting maximum number of SSH authentication attempts..."

# Set the maximum number of authentication attempts
echo "MaxAuthTries 3" >> /etc/ssh/sshd_config

# 4. Change the SSH port. 

echo ">>> Changing the SSH port..."

# Change SSH default port to 2222
sed -i 's/#Port 22/Port 2222/g' /etc/ssh/sshd_config

# 5. Implement two-factor authentication.

echo ">>> Implementing two-factor authentication..."

# Install and configure Google Authenticator for Two-Factor Authentication
pacman -S --noconfirm google-authenticator
google-authenticator

# Set up challenge response authentication
echo "AuthenticationMethods publickey,keyboard-interactive:pam" >> /etc/ssh/sshd_config

# 6. Install Fail2Ban

echo ">>> Installing Fail2Ban..."

# Update the package lists
pacman -Sy

# Install Fail2Ban
pacman -S --noconfirm fail2ban

# Enable the default fail2ban rule set
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

# Enable and start fail2ban service
systemctl enable fail2ban
systemctl start fail2ban


# Restart SSHD service
systemctl restart sshd

echo ">>> SSH Hardening complete!"
