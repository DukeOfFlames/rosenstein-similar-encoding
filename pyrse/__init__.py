import json
import 

with open('charmap.json', 'rt') as f_in:
    charmap = json.load(f_in)

def decode(rse_string: bytes) -> str:
    header = bin(rse_string[:2])[2:]  # split 2 byte-header into 16 bit; remove leading 0b
    body = rse_string[2:]
    rse_byte_size = header[:2]  # first two bits define size of every rse-char in byte
    rse_char_num = header[2:]  # last 14 bits define number of characters in rse-string
    decoded_string = ''

    for i in range(0, rse_char_num, rse_byte_size):
        rse_code = hex(body[i:i+rse_byte_size-1])[2:]  # parses the RSE character byte code
        decoded_string += charmap[rse_code][0]
    
    return decoded_string


def encode(string: str) -> bytes:
    # TODO: header
    rse_byte_string = b''
    for char in string:
        char_code = hex(char.encode())[2:]
        for k in charmap:
            if char_code in charmap[k]:
                rse_byte_string += b''
    return 0