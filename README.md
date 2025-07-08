# Coding with AI

## First Project: CodeWords

First Copilot-assisted program in the Coding with AI book, takes a text file from Project Gutenberg and counts the word frequency.

Create the python virtual environment `.venv`

```zsh
python -m venv .venv
```

Activate the environment.

```zsh
source .venv/bin/activate
```

Download the text file of "Free Air" to your hard drive.

```zsh
wget https://www.gutenberg.org/cache/epub/26732/pg26732.txt
```

Use the `touch` command to create a new `main.py` file.

```zsh
touch main.py
```

Open the `main.py` file and type the following into the top of the file:

```python
def read_text_file(file_path):
```

Immediately Copilot has a suggestion ... 

```python
# create a function to convert the text to lowercase and remove punctuation.
```
