import hashlib
import os
import sys

BLOCKSIZE = 65536  # Use 16 bit blocks


def compute_hash(filename, hashname="md5"):
    """Computes the hash digest of filename using the hash function specified.

    Arguments:
        filename {str} -- Path to file to be hashed.

    Keyword Arguments:
        hashname {str} -- Specifies the hashing algorithm. (default: {'md5'})

    Returns:
        {hex} -- The hash digest of the file
    """

    if hashname in hashlib.algorithms_available:
        hsh = hashlib.new(hashname)
        with open(filename, "rb") as f:
            buf = f.read(BLOCKSIZE)
            while len(buf) > 0:
                hsh.update(buf)
                buf = f.read(BLOCKSIZE)
        return hsh.hexdigest()


if __name__ == "__main__":
    # Get inputs
    args = sys.argv
    filename = args[1]
    try:
        hashname = args[2]
    except:
        hashname = "md5"

    # Compute and return hashes
    hash_digest = compute_hash(filename, hashname)
    print(hash_digest)
