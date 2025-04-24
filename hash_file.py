import hashlib

with open("example.txt", "r") as file:
    content = file.read()

hash_object = hashlib.sha256()
hash_object.update(content.encode('utf-8'))
file_hash = hash_object.hexdigest()

print(f'Hash of the file is {file_hash}')
