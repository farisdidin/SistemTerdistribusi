import hashlib

list_worker = ['PYRO:worker@127.0.0.1:9001','PYRO:worker@127.0.0.1:9002','PYRO:worker@127.0.0.1:9003','PYRO:worker@127.0.0.1:9004','PYRO:worker@127.0.0.1:9005']

# Python program to find MD5 hash value of a file
filename = raw_input("Enter the file name: ")
md5_hash = hashlib.md5()
with open(filename,"rb") as f:
    # Read and update hash in chunks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        md5_hash.update(byte_block)
location = ord(md5_hash.hexdigest()[-1::])%5
location_backup = (location+1)%5
# print(list_worker[location])
# print(list_worker[location_backup])
