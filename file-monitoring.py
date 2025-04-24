import hashlib

# Function to compute the hash of a file
def compute_file_hash(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    # Create the hash object and update it with file content
    hash_object = hashlib.sha256()
    hash_object.update(content.encode('utf-8'))
    
    # Return the computed hash
    return hash_object.hexdigest()

# Function to save the hash to a file
def save_hash(file_name, hash_value):
    with open(f"saved_{file_name}_hash.txt", "w") as f:
        f.write(hash_value)

# Function to read the saved hash of a file
def read_saved_hash(file_name):
    try:
        with open(f"saved_{file_name}_hash.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

# Function to check if the file has changed
def check_files_integrity(file_paths):
    for file_path in file_paths:
        current_hash = compute_file_hash(file_path)
        file_name = file_path.split("/")[-1]  # Get file name (e.g., "example.txt")
        
        # Read saved hash for each file
        saved_hash = read_saved_hash(file_name)

        if saved_hash == current_hash:
            print(f"{file_name} has not been modified.")
        elif saved_hash is None:
            print(f"{file_name} is being checked for the first time. Saving current hash.")
            save_hash(file_name, current_hash)  # Save the current hash for future comparisons
        else:
            print(f"{file_name} has been modified.")
            save_hash(file_name, current_hash)  # Update the saved hash with the new one

# Example usage for two files
file_paths = ["example.txt", "example1.txt"]
check_files_integrity(file_paths)

