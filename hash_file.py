import hashlib

file = open("example.txt", "r")
content = file.read()
#print(content)
file.close()

hash_object = hashlib.sha256()
hash_object.update(content.encode('utf-8'))
file_hash = hash_object.hexdigest()

print(f'Hash of the file is {file_hash}')
