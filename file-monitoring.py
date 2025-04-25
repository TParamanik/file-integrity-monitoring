import hashlib
import os

HASH_STORE = "hashes.txt"

# Function to compute the SHA-256 hash of a file
def compute_file_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
    hash_object = hashlib.sha256()
    hash_object.update(content)
    return hash_object.hexdigest()

# Function to load all saved hashes from hashes.txt
def load_saved_hashes():
    hashes = {}
    if os.path.exists(HASH_STORE):
        with open(HASH_STORE, "r") as f:
            for line in f:
                if ":" in line:
                    filename, filehash = line.strip().split(":", 1)
                    hashes[filename.strip()] = filehash.strip()
    return hashes

# Function to save updated hashes to hashes.txt
def save_all_hashes(hashes):
    with open(HASH_STORE, "w") as f:
        for filename, filehash in hashes.items():
            f.write(f"{filename}: {filehash}\n")

# Function to check integrity of multiple files
def check_files_integrity(file_paths):
    saved_hashes = load_saved_hashes()

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        current_hash = compute_file_hash(file_path)
        saved_hash = saved_hashes.get(file_name)

        if saved_hash != current_hash:
            print(f"{file_name} has been modified.")

        # Update the hash store
        saved_hashes[file_name] = current_hash

    save_all_hashes(saved_hashes)

# Example usage
file_paths = ["example.txt", "example1.txt"]
check_files_integrity(file_paths)
