count = int(input("Enter the number of devices: "))
devices = []

for i in range(count):
    devices.append(input(f"Enter the name of device {i + 1}: "))
print("The devices are:", devices)

import os

os.system("command -v apt")

if os.system("$?") == 0:
    os.system("sudo apt install lvm2 -y")

else:
    os.system("sudo yum install lvm2 -y")

vgname = input("Enter the name of the volume group: ")
lvname = input("Enter the name of the logical volume: ")
lvsize = input("Enter the size of the logical volume (e.g., 1G, 500M): ")
mountpoint = input("Enter the mount point (e.g., /mnt/data): ")

i = ' '.join(f"{device}" for device in devices)

#print (i)
os.system(f"sudo pvcreate {i}")
os.system(f"sudo vgcreate {vgname} {i}")
os.system(f"sudo lvcreate -n {lvname} -L {lvsize}G {vgname}")

os.system(f"sudo mkfs.ext4 /dev/{vgname}/{lvname}")

if (os.system(f"sudo mkdir -p {mountpoint}") == 0):
    os.system(f"sudo mount /dev/{vgname}/{lvname} {mountpoint}")
    os.system(f"sudo chmod 777 {mountpoint}")
    print(f"Logical volume mounted at {mountpoint} with full permissions.")

else:
    print("Failed to create mount point directory.")

os.system("df -h")