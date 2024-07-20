from argparse import Namespace, ArgumentParser
from .create_header2 import create_header

parser = ArgumentParser(description='Create a header with specified text, border width, and border type.')
parser.add_argument('-t', '--text', type=str, help='The text to include in the header.', default="Example text")
parser.add_argument('-b', '--bwidth', type=int, help='The width of the border characters.', default=2)
parser.add_argument('-bt', '--btype', type=str, help='The character to use for the header border.', default="#")
args: Namespace = parser.parse_args()

def main():
    # Call the create_header function with arguments
    create_header(args.text, args.bwidth, args.btype)

if __name__ == "__main__":
    main()
