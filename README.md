
# alphacount

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

Command-line tool that displays the frequency breakdown of every alphabetical character in a text file, sorted by default in descending order.

## How to run

*Note: to run this project you need to have [Python 3](https://www.python.org/downloads/) installed*

Clone this repository:

```bash
git clone https://github.com/s-gas/alphacount.git
```

Change to the project directory:

```bash
cd alphacount
```

Make the program executable:

```bash
chmod +x alphacount.py
```

Run:

```bash
./alphacount.py [options] <path/to/file.txt>
```

### Options

- `-h`: Show help message and exit
- `-c CHAR`: Count occurences of a specific alphabetic character
- `-r`: Sort in ascending order
- `-n COUNT`: Display the top COUNT alphabetic characters
