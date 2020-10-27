import hashlib

bucket = hashlib.md5('100'.encode()).hexdigest()[:1]
print(bucket)
