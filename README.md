# 🛡️ File Integrity Monitoring

This project helps track changes in files by using SHA-256 hashing. If any file is modified, it alerts the user. Built using simple and readable Python code.

---

## ✅ Current Features

### 1. Read File Content
- Open and read any `.txt` file using basic Python file handling.

### 2. Generate Hash
- Use Python’s `hashlib` to generate a SHA-256 hash of file contents.

### 3. Store Hashes
- Save hashes of files in a single `hashes.txt` file.
- Format: `filename: hash`

### 4. Compare Hashes
- On each run, compares current hash with saved hash.
- Detects:
  - First-time check
  - Unmodified files
  - Modified files

### 5. Check Multiple Files
- Supports checking two or more files in one go.

---

## 🛠 How It Works

1. Reads file content.
2. Generates a SHA-256 hash.
3. Compares it with the saved hash in `hashes.txt`.
4. Alerts user if the file was changed, or if it’s the first time it’s being checked.
5. Updates `hashes.txt` accordingly.

---

## ▶️ How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/file-integrity-monitoring.git
   cd file-integrity-monitoring
