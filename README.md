# platereader
Measure fungal growth with computer vision

## Installation

- Requires a python 3.7 + installation (to download windows installer [click here](https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe))
- On the command line:

```
git clone https://github.com/neoformit/platereader.git
cd platereader
pip install -r requirements.txt
```

## Analysing images

- Add `.jpg` files to be analysed into a subfolder `images`
- Run `plates.py` (double click on it)
- Fungal growth area for each image can be found in the output file `area.csv`
- Annotated images can be found in the folder `output`. Check these to make sure the computer recognised the fungal growth correctly!
