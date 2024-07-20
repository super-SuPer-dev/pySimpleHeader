# SimpleHeader

A cli and module help to make a header border text like this.

```bash
####################    ===================     ~~~~~~~~~~~~~~~~~~~~~
### Example text ###    === Hello World ===     ~~~~ Hello World ~~~~
####################    ===================     ~~~~~~~~~~~~~~~~~~~~~
```

## Install
```bash
pip install https://github.com/super-SuPer-dev/New_setup.git
```

## Usage
CLI :
```bash
python -m SimpleHeader -t "Hello World" -b 4 -bt "&"
python -m SimpleHeader -t "Hello"
```
```bash
python -m SimpleHeader [-h] [-t TEXT] [-b BWIDTH] [-bt BTYPE]
```

Module :
```python
from SimpleHeader import create_header

def main():
    create_header(text="Example text", borderwidth=3, btype="#")

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
pip install https://github.com/super-SuPer-dev/New_setup.git
```

If you want you can clone it using this.
```bash
git clone https://github.com/super-SuPer-dev/New_setup.git
cd New_setup
```

## LICENSE
[MIT_LICENSE](./LICENSE)