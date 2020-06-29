"""Crack a password in a given password list."""
import hashlib
import multiprocessing
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from functools import partial
from os.path import exists
import bcrypt


def hash_function(p, hashfunc="bcrypt", salt=None):
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
        if not salt:
            salt = b"salt"
        instance = Scrypt(
            salt=b"salt", length=32, n=2 ** 14, r=8, p=1, backend=default_backend()
        )
        return instance.derive(p)
    elif hashfunc == "bcrypt":
        if not salt:
            salt = bcrypt.gensalt()
        return bcrypt.hashpw(p, salt)
    else:
        raise ValueError


def check_password(hsh, event, guess, hash_function=hash_function, salt=None):
    """Check a password against a known hash.

    Arguments:
        hsh {bytes} -- The hash to compare against
        guess {string} -- The guess of the password

    Keyword Arguments:
        hash_function {function} -- The hashing function used to generate hsh.

    Returns:
        bool -- True if the password matches the hash, False otherwise

    """
    try:
        if not event.is_set():
            guess = guess.strip().encode()
            guess_hsh = hash_function(guess, salt=salt)
        if guess_hsh == hsh:
            event.set()
    except AttributeError:
        guess = guess.strip().encode()
        guess_hsh = hash_function(guess, salt=salt)
    return guess_hsh == hsh


if __name__ == "__main__":
    # Load common password list
    password_list_file = "top-million-passwords.txt"
    with open(password_list_file, "r") as f:
        password_list = f.read().splitlines()

    salt = b"$2b$12$Ntzcv8ZwbMs1UK0oq2.j4."

    # Get the input to guess
    if exists("mypassword.hsh"):  # Load the hashed password if it exists.
        with open("mypassword.hsh", "rb") as f:
            hsh = f.read()
    else:  # Prompt for the password as save if it doesn't.
        password = input("Please enter a password to be hashed:").encode()
        with open("mypassword.hsh", "wb") as f:
            hsh = hash_function(password, salt=salt)
            f.write(hsh)

    # Crack the password using a single thread
    print(f"Target hash to crack is {hsh}")
    for count, guess in enumerate(password_list):
        result = check_password(
            hsh, None, guess, hash_function=hash_function, salt=salt
        )
        if result:
            print(f"Your missing password is '{guess}'!")
            print(f"Tried {count + 1} passwords in total.")
            break
    else:
        print(f"Could not find the password in the list {password_list_file}!")

    # Crack the password with multiprocessing
    multiprocessing.freeze_support()
    processes = multiprocessing.cpu_count() - 1
    manager = multiprocessing.Manager()
    event = manager.Event()
    with multiprocessing.Pool(processes=processes) as pool:
        results = pool.map(
            partial(check_password, hsh, event, hash_function=hash_function, salt=salt),
            password_list,
        )
        try:
            print(f"Your missing password is '{password_list[results.index(True)]}'!")
        except ValueError:
            print(f"Could not find the password in the list {password_list_file}!")
        event.wait()
        pool.terminate()
