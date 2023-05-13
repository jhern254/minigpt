"""
  Goal: Working on building a gpt transformer model following Karpathy 
        tutorial.
"""
import numpy as np
import os
import logging
import requests
import torch


logging.basicConfig(level=logging.DEBUG)


CSV_LINK  = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
BLOCK_SIZE = 8

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

# TODO: following def. signature needs >= Python 3.9
#def create_mapping(chars: str) -> tuple[dict[str, int], dict[int, str]]:
def create_mapping(chars: str) -> tuple:
    """
    Create a mapping from characters to integers and integers to characters.

    Args:
    - chars (str): a string containing the characters for mapping

    Returns:
    - stoi (dict): a dictionary mapping characters to integers
    - itos (dict): a dictionary mapping integers to characters
    """
    stoi = {ch: i for i, ch in enumerate(chars)}
    itos = {i: ch for i, ch in enumerate(chars)}
    return stoi, itos

#def encode(s: str, mapping: dict[str, int]) -> list:
def encode(s: str, mapping: dict) -> list:
    """
    Encode a string into a list of integers using a character-to-integer mapping.

    Args:
    - s (str): the input string to be encoded
    - mapping (dict): a dictionary mapping characters to integers

    Returns:
    - encoded (list): a list of integers representing the encoded string
    """
    encoded = lambda s: [mapping[c] for c in s]
    return encoded(s)

#def decode(encoded: list[int], mapping: dict[int, str]) -> str:
def decode(encoded: list, mapping: dict) -> str:
    """
    Decode a list of integers into a string using an integer-to-character mapping.

    Args:
    - encoded (list): a list of integers to be decoded
    - mapping (dict): a dictionary mapping integers to characters

    Returns:
    - decoded (str): the decoded string
    """
    decoded = lambda l: ''.join([mapping[i] for i in l])
    return decoded(encoded)

# Example usage
# chars = "abcdefghijklmnopqrstuvwxyz"
# stoi, itos = create_mapping(chars)
# encoded_string = encode("hii there", stoi)
# decoded_string = decode(encoded_string, itos)

def split_data(data: torch.Tensor) -> tuple:
    """
    Split the input data into training and validation datasets.

    Args:
    - data (torch.Tensor): Input tensor to be split

    Returns:
    - tuple[torch.Tensor, torch.Tensor]: Tuple containing the training data and validation data tensors
    """
    # 90/10 split
    n = int(0.9*len(data))
    train_data = data[:n]
    val_data = data[n:]
    return train_data, val_data





if __name__ == "__main__":
    # get data from github
    text = getData()
#    print(type(text))
    logging.debug("length of dataset in characters: %d", len(text))
    logging.debug((text[:100]))

# NOTE: turn str text into set, then list so it's ordered, then sort
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
    logging.debug(''.join(chars))
    logging.debug(vocab_size)

    # make mapping
    stoi, itos = create_mapping(chars)
    logging.debug(encode("hi there", stoi))
    logging.debug(decode(encode("hi there", stoi), itos))

    # encode the entire text dataset and store it into a torch.Tensor
    data = torch.tensor(encode(text, stoi), dtype=torch.long)
    logging.debug(data.shape, data.dtype)
    logging.debug(data[:100])

    train_data, val_data = split_data(data)
    logging.debug(train_data[:BLOCK_SIZE+1])











