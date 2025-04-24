# File Integrity Monitoring

This project implements a basic **File Integrity Monitoring (FIM)** system using Python. It reads a file, computes its SHA-256 hash, and checks for changes by comparing the current hash with a previously saved hash.

## Features

- **File Hashing**: Reads the content of `example.txt` and computes its SHA-256 hash.
- **Change Detection**: Compares the current hash with a stored hash to detect file modifications.
- **Safe File Handling**: Uses Python's `with` statement to ensure safe opening and closing of files.

## Steps Completed

### 1. **Read File Content**
The file `example.txt` is read using Python, and its content is displayed in the console.

### 2. **Compute and Display Hash**
The SHA-256 hash of the file content is computed and displayed. The hash uniquely represents the content of the file.

### 3. **Store the Initial Hash**
The computed hash is stored in `saved_hash.txt` for future comparison.

### 4. **File Integrity Check**
The script checks if the file has been modified by comparing the current hash with the stored hash. If they differ, it indicates that the file has been altered.

## Usage

1. Ensure that `example.txt` exists in the same directory as the script.
2. Run the script to check the integrity of the file:
   ```bash
   python hash_example.py
