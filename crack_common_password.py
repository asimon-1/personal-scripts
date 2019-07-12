"""Crack a password in a given password list."""
import hashlib
import multiprocessing
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from functools import partial
from os.path import exists


def hash_function(p, hashfunc="sha1"):
    """Generate hash from input string.

    Arguments:
        p {str, bytes} -- The input to be hashed.

    Keyword Arguments:
        hashfunc {str} -- Hashing algorithm to use. Options are "sha1" and "scrypt". (default: {"sha1"})

    Returns:
        bytes -- Hash of the input

    """
    if isinstance(p, str):  # Convert str to bytes if necessary
        p = p.encode()

    hashfunc = hashfunc.lower()  # Ensure the input will match the conditional case.

    if hashfunc == "sha1":
        return hashlib.sha1(p).hexdigest().encode()
    elif hashfunc == "scrypt":
        instance = Scrypt(
            salt=b"salt",
            length=32,
            n=2**14,
            r=8,
            p=1,
            backend=default_backend()
        )
        return instance.derive(p)
    else:
        raise ValueError


def check_password(hsh, guess, hash_function=hash_function):
    """Check a password against a known hash.

    Arguments:
        hsh {bytes} -- The hash to compare against
        guess {string} -- The guess of the password

    Keyword Arguments:
        hash_function {function} -- The hashing function used to generate hsh.

    Returns:
        bool -- True if the password matches the hash, False otherwise

    """
    guess = guess.strip().encode()
    guess_hsh = hash_function(guess)
    return guess_hsh == hsh


if __name__ == '__main__':
    # Load common password list
    password_list_file = "top-million-passwords.txt"
    with open(password_list_file, 'r') as f:
        password_list = f.read().splitlines()

    # Get the input to guess
    if exists("mypassword.hsh"):  # Load the hashed password if it exists.
        with open("mypassword.hsh", "rb") as f:
            hsh = f.read()
    else:  # Prompt for the password as save if it doesn't.
        password = input("Please enter a password to be hashed:").encode()
        with open("mypassword.hsh", "wb") as f:
            hsh = hash_function(password)
            f.write(hsh)

    # Crack the password using a single thread
    print(f"Target hash to crack is {hsh}")
    for count, guess in enumerate(password_list):
        result = check_password(hsh, guess, hash_function)
        if result:
            print(f"Your missing password is '{guess}'!")
            print(f"Tried {count + 1} passwords in total.")
            break
    else:
        print(f"Could not find the password in the list {password_list_file}!")

    # Crack the password with multiprocessing
    multiprocessing.freeze_support()
    processes = multiprocessing.cpu_count() - 1
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(partial(check_password, hsh, hash_function=hash_function), password_list)
        try:
            print(f"Your missing password is '{password_list[results.index(True)]}'!")
        except ValueError:
            print(f"Could not find the password in the list {password_list_file}!")
