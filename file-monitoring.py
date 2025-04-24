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
def save_hash(hash_value):
    with open("saved_hash.txt", "w") as f:
        f.write(hash_value)

# Function to check if the file has changed
def check_file_integrity(file_path):
    # Step 1: Compute the current hash of the file
    current_hash = compute_file_hash(file_path)
    
    # Step 2: Read the saved hash
    try:
        with open("saved_hash.txt", "r") as f:
            saved_hash = f.read().strip()
    except FileNotFoundError:
        saved_hash = None
    
    # Step 3: Compare the hashes
    if saved_hash == current_hash:
        print("File has not been modified.")
    elif saved_hash is None:
        print("File is being checked for the first time. Saving current hash.")
        save_hash(current_hash)  # Save the current hash as the reference for future checks
    else:
        print("File has been modified.")
        save_hash(current_hash)  # Update the saved hash to the new one

# Example usage
file_path = "example.txt"
check_file_integrity(file_path)
