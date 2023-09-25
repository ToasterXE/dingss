import hashlib
from einstellungen import *

def update_seed(string):
    global seed
    seed += string

def get_hash(seed):
    return int.from_bytes(hashlib.sha256(seed.encode('utf-8')).digest(), 'big')

def get_seedval():
    return(int(str(abs(get_hash(seed)))))
