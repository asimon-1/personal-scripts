import hashlib
import os
import sys

BLOCKSIZE = 65536  # Use 16 bit blocks

# Define available hash functions
HASHES = {
    'md5': hashlib.md5(),
    'sha1': hashlib.sha1(),
    'sha256': hashlib.sha256(),
}


def compute_hash(filename, hsh=None):
    '''Computes the hash digest of filename using the hash function specified in hsh.

    Arguments:
        filename {str} -- Path to file to be hashed.

    Keyword Arguments:
        hsh {hashlib object} -- Specifies the hashing algorithm. Defaults to md5 (default: {None})

    Returns:
        {hex} -- The hash digest of the file
    '''

    if not hsh:
        hsh = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read(BLOCKSIZE)
        while len(buf) > 0:
            hsh.update(buf)
            buf = f.read(BLOCKSIZE)
    return hsh.hexdigest()


if __name__ == "__main__":
    # Get inputs
    args = sys.argv
    filename = args[1]
    if len(args) > 2:
        hsh = args[2]
        if hsh in HASHES.keys():
            hsh = HASHES[hsh]
    else:
        hsh = None

    # Compute and return hashes
    hash_digest = compute_hash(filename, hsh)
    print(hash_digest)
