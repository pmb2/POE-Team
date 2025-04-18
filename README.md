![POE‑Team “Game Paused” banner](poe-team-banner.png)

# 🛡️ PoE Team (ESC Sync)

Effortlessly synchronize the **Escape (ESC) key** across your Path of Exile 2 party!  
If any teammate presses ESC, everyone with Path of Exile 2 open instantly gets the same input—no matter where they are in the world.

---

## ✨ Features

- **Instant ESC Sync:** Press ESC on one PC, and all Path of Exile 2 clients in your party receive it.
- **Automatic Game Detection:** Only triggers if Path of Exile 2 is running.
- **Ultra Lightweight:** No bloat, no lag, and no extra dependencies.
- **Zero Setup for Teammates:** Just run the EXE, enter your host’s IP, and play.
- **Works Over the Internet:** Not limited to LAN parties!

---

## 🚀 Quick Start

### 1. Download & Extract

- Download the latest [Release](#) (or build from source).
- Extract the folder anywhere on your PC.

### 2. Host Setup

1. The party leader runs **host.exe**.
2. Share your **public IP address** with your friends.
   - Find it easily at [whatismyip.com](https://www.whatismyip.com/) or by searching “my IP” on Google.
3. **(Required)** Forward UDP port `51987` on your router to your PC.  
   - [How to Port Forward (guide)](https://portforward.com/)
   - The script tries to open the Windows firewall for you.

### 3. Client Setup

1. Each teammate runs **client.exe**.
2. When prompted, enter the host’s public IP address.

---

## 🎮 How It Works

- The host acts as a relay server.
- When anyone presses ESC, the script checks if Path of Exile is running.
- If so, it sends an ESC signal to all connected teammates with the game open.
- Only Path of Exile 2 windows are affected—no accidental ESCs elsewhere!

---

## 📝 Requirements

- **Windows 10/11** (64-bit)
- **Path of Exile 2** (English window title)
- **Internet connection**
- **UDP port 51987** open (host only)

---

## 🛠️ Advanced: Build from Source

1. Install [Python 3.11+](https://www.python.org/downloads/)
2. Install PyInstaller:
```

pip install pyinstaller

```
3. Build the executables:
```

pyinstaller --onefile --noconsole host.py
pyinstaller --onefile --noconsole client.py

```
Find your `.exe` files in the `dist/` folder.

---

## ❓ FAQ

**Q: Is this safe?**  
A: Yes! No personal data is sent. The script only listens for ESC key events and only simulates ESC for Path of Exile.

**Q: Will this get me banned in Path of Exile?**  
A: No. The script simply simulates a local ESC keypress, just as if you pressed it yourself.

**Q: My firewall/antivirus warns me!**  
A: The script opens a single UDP port and simulates a keypress. You may need to allow it through your firewall.

**Q: It’s not working!**  
A:  
- Make sure the host’s port is forwarded and not blocked by a firewall.
- All users must have Path of Exile 2 open (English title).
- Double-check the IP address you entered.

---

## 💡 Credits

Created by [The Backus Agency](https://backus.agency)  
Inspired by the need for seamless party coordination in Path of Exile.

---

## 🏆 Enjoy your synchronized adventures, Exiles!

*Feel free to open issues or contribute!*
```

# POE-Team
