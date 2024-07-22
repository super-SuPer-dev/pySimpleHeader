import argparse
import math
from argparse import Namespace

# to-do add space between text and border

def create_header(text="Example text", borderwidth=2, btype="#", space=1):
    """
    Create a header with a specified character, border width, and text.
    
    :param text: The text to include in the header.
    :param borderwidth: The width of the border characters.
    :param btype: The character to use for the header border.
    :param space: The space between text and border.
    """

    x = math.ceil(len(text) / len(btype),)
    y = len(btype) * x
    u = abs(len(text) - y)

    text_space_s = (" "*u) + ((len(btype)*" ")*space)
    text_space_f = (len(btype)*" ")*space

    center_text = f"{btype * borderwidth}{text_space_f}{text}{text_space_s}{btype * borderwidth}"
    width = len(center_text)
    border_text = btype * int((width/len(btype)))

    # Show the result
    print(border_text)
    print(center_text)
    print(border_text)
