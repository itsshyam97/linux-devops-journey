# 🧾 LVM Automation Script for Linux (`lvm.py`)

## 🧠 Purpose
This Python script automates the creation of **Logical Volume Management (LVM)** on Linux systems.  
It simplifies setting up **Physical Volumes (PVs)**, **Volume Groups (VGs)**, and **Logical Volumes (LVs)**, then formats and mounts the LV to a specified directory — all through interactive inputs.

---

## ⚙️ Features
✅ Detects whether the system uses `apt` or `yum` package manager  
✅ Installs `lvm2` automatically if missing  
✅ Creates Physical Volumes (PVs) from user-provided devices  
✅ Creates a Volume Group (VG) and Logical Volume (LV)  
✅ Formats the LV with `ext4` filesystem  
✅ Mounts the LV to a given mount point and applies `777` permissions  
✅ Displays disk usage (`df -h`) at the end  

---

## 🧩 How It Works

1. **Prompt for devices**
   - Asks how many disks you want to include (e.g., `/dev/sdb`, `/dev/sdc`)
   - Collects all devices into a list

2. **Check and install LVM package**
   - Detects the package manager (`apt` or `yum`)
   - Installs `lvm2` accordingly

3. **Create LVM structure**
   ```bash
   pvcreate <devices>
   vgcreate <vgname> <devices>
   lvcreate -n <lvname> -L <lvsize>G <vgname>
   ```

4. **Format and mount**
   - Formats the LV as `ext4`
   - Creates the mount directory if not present
   - Mounts the LV
   - Sets full permissions for accessibility

5. **Verifies the result**
   - Prints updated disk usage via `df -h`

---

## 🧱 Example Run

```bash
$ python3 lvm.py
Enter the number of devices: 2
Enter the name of device 1: /dev/sdb
Enter the name of device 2: /dev/sdc
Enter the name of the volume group: vgdata
Enter the name of the logical volume: lvbackup
Enter the size of the logical volume (e.g., 1G, 500M): 5
Enter the mount point (e.g., /mnt/data): /mnt/backup
```

🟢 **Output:**
```
Physical volume "/dev/sdb" successfully created
Volume group "vgdata" successfully created
Logical volume "lvbackup" created
Filesystem created
Logical volume mounted at /mnt/backup with full permissions.
```

---

## ⚠️ Notes / Precautions
- Run this script as **root** or with `sudo`.
- Ensure disks (e.g., `/dev/sdb`, `/dev/sdc`) are **not in use or mounted**.
- Double-check device names before proceeding — this process is destructive.

---

## 🧰 Commands Used Internally

```bash
pvcreate <devices>
vgcreate <vgname> <devices>
lvcreate -n <lvname> -L <lvsize>G <vgname>
mkfs.ext4 /dev/<vgname>/<lvname>
mkdir -p <mountpoint>
mount /dev/<vgname>/<lvname> <mountpoint>
chmod 777 <mountpoint>
df -h
```

---

## 🧑‍💻 Author
**Shyam Prakash S**  
Systems Engineer | Python Developer | Linux & DevOps Enthusiast  
[LinkedIn](https://linkedin.com/in/shyam-ps) | [Portfolio](https://shyamprakash.in)

---

## 💡 Git Commit Suggestion
```bash
git add lvm.py README.md
git commit -m "Added LVM automation script and documentation"
git push origin main
```
