import argparse
from argparse import Namespace

def create_header(text="Example text", borderwidth=2, btype="#"):
    """
    Create a header with a specified character, border width, and text.

    ##################
    ## Example text ##
    ##################
    
    :param text: The text to include in the header.
    :param borderwidth: The width of the border characters.
    :param btype: The character to use for the header border.
    """
    # Calculate the width for the top and bottom border
    width = len(text) + 2 * borderwidth + 2  # Include spaces on both sides of the text

    # Show the result
    print(btype * width)
    print(f"{btype * borderwidth} {text} {btype * borderwidth}")
    print(btype * width)