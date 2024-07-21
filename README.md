# pySimpleHeader

A cli and module help to make a header border text like this.

> [!NOTE]
> It doesn't always work with character that longer than one character like 👽 or ※

```bash
####################    ======================  //////////////////////
### Example text ###    ===  Example text  ===  ///  Example text  ///
####################    ======================  //////////////////////

$$$$$$$$$$$$$$$$$$$$$$  @@@@@@@@@@@@@@@@@@@@@@  ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
$$$  Example text  $$$  @@@  Example text  @@@  ₪₪₪  Example text  ₪₪₪
$$$$$$$$$$$$$$$$$$$$$$  @@@@@@@@@@@@@@@@@@@@@@  ₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

(●)(●)(●)(●)(●)(●)(●)(●)
(●)   Example text   (●)
(●)(●)(●)(●)(●)(●)(●)(●)

```

## Install
```bash
pip install https://github.com/super-SuPer-dev/pySimpleHeader.git
```

## Usage
CLI :
```bash
python -m simpleheader -t "Hello World" -b 4 -bt "&" -s 2
python -m simpleheader -t "Hello"
```
```bash
python -m simpleheader [-h] [-t TEXT] [-b BWIDTH] [-bt BTYPE] [-s SPACE]
```

Module :
```python
from SimpleHeader import create_header

def main():
    create_header(text="Example text", borderwidth=3, btype="#", space=1)

if __name__ == "__main__":
    main()
```
output :
```bash
####################
### Example text ###
####################
```

## Installation
You can use this to setup a venv.
```bash
python -m venv venv
.\venv\Scripts\activate
```

```bash
python.exe -m pip install --upgrade pip
```

Install it.
```bash
pip install https://github.com/super-SuPer-dev/pySimpleHeader.git
```

If you want you can clone it using this.
```bash
git clone https://github.com/super-SuPer-dev/pySimpleHeader.git
cd New_setup
```

## LICENSE
[MIT_LICENSE](./LICENSE)