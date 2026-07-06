import os

if os.system("command -v apt") == 0:
    os.system("sudo apt install mdadm -y")
else:
    os.system("sudo yum install mdadm -y")

rlevel = input("Enter the RAID level (e.g., 0, 1, 5, 10): ")

mountpoint = input("Enter the mount point (e.g., /mnt/raid): ")

count = int(input("Enter the number of devices: "))
devices = []

for i in range(count):
    devices.append(input(f"Enter the name of device {i + 1}: "))
print("The devices are:", devices)

i = ' '.join(f"{device}" for device in devices)

os.system(f"sudo mdadm --create --verbose /dev/md{rlevel} --level={rlevel} --raid-devices={count} {i}")   

os.system(f"sudo mkfs.ext4 /dev/md{rlevel}")

if (os.system(f"sudo mkdir -p {mountpoint}") == 0):
    os.system(f"sudo mount /dev/md{rlevel} {mountpoint}")
    os.system(f"sudo chmod 777 {mountpoint}")
    print(f"RAID array mounted at {mountpoint} with full permissions.")
else:
    print("Failed to create mount point directory.")

os.system("df -h")
os.system("cat /proc/mdstat")
os.system("lsblk")
