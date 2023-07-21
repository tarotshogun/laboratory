"""
Try decompressing a file by brute force.
"""
import concurrent.futures
import itertools
import logging
import os
import subprocess
from typing import List

# This script works only on Windows.
assert os.name == "nt"

characters = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# Setting for the script
SEVEN_ZIP = r"C:\Program Files\7-Zip\7z.exe"

ARCHIVE_PATH = r".\test"
ARCHIVE_FILE_NAME = r"\test.rar"
ARCHIVE_FILE_PATH = ARCHIVE_PATH + ARCHIVE_FILE_NAME

logging.basicConfig(
    filename="example.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s:%(name)s - %(message)s",
)


class WrongPasswordError(Exception):
    pass


def decompress(password: str):
    """
    Decompress archive using 7-zip. Raises WrongPasswordError if password doesn't match.

    @param password Password to use for decompressing archive.
    """
    logging.info("try to open (password: %s)", password)
    command = [
        SEVEN_ZIP,
        "x",
        "-y",
        "-p" + password,
        "-o" + ARCHIVE_PATH,
        ARCHIVE_FILE_PATH,
    ]
    process = subprocess.Popen(
        command, stderr=subprocess.STDOUT, stdout=subprocess.PIPE
    )
    subprocess.Popen.wait(process)
    if process.returncode == 0:
        logging.info("success to open (password: %s)", password)
    else:
        logging.info("failed to open (password: %s)", password)
        raise WrongPasswordError


def create_password_list() -> List[str]:
    """
    Creates a list of passwords for brute force attack

    @return A list of passwords in alphabetical order ( first to last ).
    """
    min_password_length = 4
    max_password_length = 4
    passwords: List[str] = []
    for num in range(min_password_length, max_password_length + 1):
        for seed in itertools.product(characters, repeat=num):
            password = "".join(seed)
            passwords.append(password)
    return passwords


def main():
    """
    Try decompressing a file by brute force.
    """
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)

    tasks: List[concurrent.futures.feature] = []

    for password in create_password_list():
        task = executor.submit(decompress, password)
        tasks.append(task)

    for feature in concurrent.futures.as_completed(tasks):
        try:
            if feature.exception() is None:
                break
        except WrongPasswordError:
            continue

    executor.shutdown(wait=True, cancel_futures=True)


if __name__ == "__main__":
    main()
