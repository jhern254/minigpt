"""
  Goal: Working on building a gpt transformer model following Karpathy 
        tutorial.
"""
import numpy as np
import os
import logging
import requests


CSV_LINK  = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"

def confirm_overwrite(filename: str) -> bool:
    """Check if the specified file already exists and prompt the user for confirmation before overwriting.

    :param filename: The name of the file to check.
    :type filename: str
    :return: True if the file can be overwritten, False otherwise.
    """
    if os.path.exists(filename):
        overwrite = input(f"{filename} already exists. Overwrite? (y/n) ")
        if overwrite.lower() != 'y':
            return False
    return True


def download_file(url: str) -> None:
    """Download a file from the given URL.

    :param url: The URL of the file to download.
    :type url: str
    :raises requests.exceptions.RequestException: If the request fails.
    :return: None

    Example:
    >>> download_file('https://example.com/myfile.txt')  # downloads myfile.txt from example.com
    >>> download_file('https://example.com/myfile.zip')  # downloads myfile.zip from example.com
    """
    filename = url.rsplit('/', 1)[-1]

    if os.path.exists(filename):
        if not confirm_overwrite(filename):
            return 

    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def read_file(filename: str) -> str:
    """Read the contents of the given file and return them as a string.

    :param filename: The name of the file to read.
    :type filename: str
    :return: The contents of the file as a string.
    :rtype: str
    :raises FileNotFoundError: If the specified file does not exist.

    Example:
    >>> contents = read_file('example.txt')
    >>> print(contents)
    'This is an example file.'
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"{filename} does not exist.")
    with open(filename, 'r') as file:
        contents = file.read()
    return contents


def getData() -> str:
    """Download data from link"""
    download_file(url = CSV_LINK)
    arr = read_file("./input.txt")
    return arr






if __name__ = "__main__":

    if(True):
        text = getData()
#        print(book[:1000])

# ask chatgpt for explanation and learn to code like karpathy
        if(True):
            chars = sorted(list(set(text)))
            vocab_size = len(chars)
            print(''.join(chars))
            print(vocab_size)















