# 🧰 Assisted RAID Creation Script

This Python script automates the creation, formatting, and mounting of **RAID arrays** on Linux systems.  
It helps system administrators and DevOps engineers quickly configure software RAID using `mdadm` without manual command entry.

---

## ⚙️ Features
- Automatically detects your package manager (`apt` or `yum`) and installs `mdadm` if missing.
- Creates RAID arrays with user-defined level (0, 1, 5, 10, etc.).
- Formats the created RAID array using `ext4`.
- Creates and mounts the RAID at your chosen mount point.
- Sets permissions to `777` for easy access.
- Displays RAID and disk status using:
  - `df -h`
  - `/proc/mdstat`
  - `lsblk`

---

## 📜 Script Overview

### **Filename**
`raid_creator.py`

### **Core Functions**
| Step | Action |
|------|--------|
| 1 | Detects and installs `mdadm` package |
| 2 | Prompts user for RAID level, mount point, and device list |
| 3 | Creates RAID array using the provided devices |
| 4 | Formats it with `ext4` filesystem |
| 5 | Mounts RAID to the specified mount point |
| 6 | Shows disk usage and RAID status |

---

## 🧑‍💻 Usage

### **Run the Script**
```bash
python3 raid_creator.py
```

### **Example Input**
```
Enter the RAID level (e.g., 0, 1, 5, 10): 1
Enter the mount point (e.g., /mnt/raid): /mnt/raid1
Enter the number of devices: 2
Enter the name of device 1: /dev/sdb
Enter the name of device 2: /dev/sdc
```

### **Example Output**
```
RAID array mounted at /mnt/raid1 with full permissions.
Filesystem summary:
Filesystem      Size  Used Avail Use% Mounted on
/dev/md1         20G  1.2G   19G   6% /mnt/raid1
```

---

## 🧩 RAID Levels Supported
| RAID Level | Description |
|-------------|-------------|
| **0** | Striping – fast, no redundancy |
| **1** | Mirroring – redundancy, slower write |
| **5** | Parity-based – balance of speed and redundancy |
| **10** | Stripe + Mirror – high speed and redundancy |

---

## 🛠️ Commands Used Internally
```bash
sudo mdadm --create --verbose /dev/md<level> --level=<level> --raid-devices=<count> <devices>
sudo mkfs.ext4 /dev/md<level>
sudo mkdir -p <mountpoint>
sudo mount /dev/md<level> <mountpoint>
sudo chmod 777 <mountpoint>
df -h
cat /proc/mdstat
lsblk
```

---

## ⚠️ Precautions
- Make sure the disks you use (e.g., `/dev/sdb`, `/dev/sdc`) **do not contain important data** — they will be overwritten.
- Run as a **user with sudo privileges**.
- Do not use mounted or system disks for RAID creation.

---

## 📂 Output Example
After successful execution:
- RAID device created as `/dev/md<level>`
- Mounted to `/mnt/<your_mount>`
- Status available via:
  ```bash
  cat /proc/mdstat
  lsblk
  ```

---

## 🧾 Author
**Shyam Prakash S**  
*Linux & DevOps Enthusiast | Python Developer*  
🌐 [linkedin.com/in/shyam-ps](https://linkedin.com/in/shyam-ps)
