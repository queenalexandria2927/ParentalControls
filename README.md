
# PhoenixRoseMedia DNS Manager (Alpha)

**PhoenixRoseMedia DNS Manager** is a lightweight, low-level tool for managing DNS records with optional **parental control features**. Built for simplicity and local use, this alpha-stage utility allows you to configure DNS zones, edit records, and apply basic domain blocking for content filtering.

---

## ⚠️ Status: Alpha

This tool is in early development and **not production-ready**. Use it for testing, development, and experimentation. Expect bugs, minimal polish, and frequent changes.

---

## 🔑 Key Features (So Far)

* ✏️ Basic DNS zone file editing (A, CNAME, TXT)
* 🔍 CLI interface for record add/remove/list
* 📵 Parental Controls: Block access to adult or undesired domains by adding DNS redirects
* 💾 Local-only file operations (no upstream sync yet)
* 🧱 No external dependencies, works offline

---

## 🛠️ Requirements

* Python 3.10+ *(or insert actual language/runtime if different)*
* Run on Linux (Ubuntu,Debian,Arch) and also Windows (10/11)
* Basic understanding of DNS zones and Bind-style records

---

## 🚀 Getting Started

### Clone the Repo

```bash
git clone https://github.com/phoenixrosemedia/dns-manager.git
cd dns-manager
```

### Run the Manager

```bash
python dns_manager.py
```

### Example Usage

```bash
# Add A record
./dns_manager.py add A example.com 192.0.2.1

# Remove CNAME record
./dns_manager.py remove CNAME www.example.com

# Enable parental control mode
./dns_manager.py block-list enable

# Add domain to parental control list
./dns_manager.py block add adultsite.com
```

---

## 📦 Roadmap (Short-Term)

* [ ] Support for MX, NS, and SRV records
* [ ] Validate zone syntax before writing
* [ ] Expand parental blocklist categories (e.g. gambling, violence)
* [ ] Import/export parental blocklists
* [ ] Basic DNS-over-HTTPS forwarding (optional)

---

## 🧪 Contributing

Feedback, bug reports, and small patches are welcome during Alpha. Please open an issue or contact us by email.

---

## 📄 License

MIT License — see `LICENSE` file.

---

## 📬 Contact

PhoenixRoseMedia
✉️ [support@phoenixrosemedia.com](mailto:support@phoenixrosemedia.com)
🌐 [https://www.phoenixrosemedia.com](https://www.phoenixrosemedia.com)


