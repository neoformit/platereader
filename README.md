# platereader
Measure fungal growth with computer vision

## Installation

- Install Git to clone repository (USC software centre)
- Requires a python 3.7 + installation (USC software centre or download windows installer [click here](https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe))
- On the command line:

```
cd <path/to/wherever/you/want/it>
git clone https://github.com/neoformit/platereader.git
cd platereader
pip install -r requirements.txt
```

## Analysing images

- Add `.jpg` files to be analysed into a subfolder `images`
- Run `plates.py` (double click on it)
- Fungal growth area for each image can be found in the output file `area.csv`
- Annotated images can be found in the folder `output`. Check these to make sure the computer recognised the fungal growth correctly!
