'''
Use case example:
    INPUT       bmhnYnpuZ3ZiYXZmbmpyZmJ6cg==
    KEY         13
    DECODED     nhgbzngvbavfnjrfbzr
    DECRYPTED   automationisawesome
'''
import string
import base64
import argparse
from argparse import RawTextHelpFormatter

# === GLOBAL VARS ===
useless_bar = 50 * "="


# === FUNCTIONS DEFINITION ===
def rot_cipher(input_text, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return input_text.translate(table)


def encode_b64(text, encode):
    if encode is None:
        return text
    if encode:
        return base64.urlsafe_b64encode(text.encode("utf-8"))
    else:
        return base64.b64decode(text)


def arguments_definition():
    parser = argparse.ArgumentParser(
        formatter_class=RawTextHelpFormatter,
        description=' Cipher/Decipher for binary 64 encoded or plain text.\n\
        Examples:\n\
        to encrypt and encode a text\n\
          python rot_cipher.py automationisawesome --encrypt --encode --key 13\n\
        to decrypt and decode a text:\n\
          python rot_cipher.py bmhnYnpuZ3ZiYXZmbmpyZmJ6cg== --decrypt --decode --key 13\n')
    parser.add_argument('input_text', type=str,
                        help="input string")

    parser.add_argument('--encrypt', dest='to_encrypt', action='store_true',
                        help='encrypt input text with Caesar rotation algorithm')
    parser.add_argument('--decrypt', dest='to_encrypt', action='store_false',
                        help='decrypt input text with Caesar rotation algorithm')
    parser.set_defaults(to_encrypt=False)

    parser.add_argument('--encode', dest='to_encode', action='store_true',
                        help='encode the text in base64 before encryption')
    parser.add_argument('--decode', dest='to_encode', action='store_false',
                        help='decode the text from base64 before encryption')
    parser.set_defaults(to_encode=None)

    parser.add_argument('--key', dest='key', type=int,
                        help='number of rotations of the alphabet letters')
    return parser


# === MAIN ===
if __name__ == "__main__":

    parser = arguments_definition()
    args = parser.parse_args()

    print(useless_bar + "\n" + " THE ULTIMATE CLARANET CRYPTO CHALLENGE \n" + useless_bar + "\n")

    if args.to_encrypt:
        encrypted = rot_cipher(args.input_text, args.key)
        out_text  = encode_b64(encrypted, args.to_encode)

    else:
        decoded  = encode_b64(args.input_text, args.to_encode)
        out_text = rot_cipher(decoded, args.key)

    print (" The final text is: {}".format(out_text))
