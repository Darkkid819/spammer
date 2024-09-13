# Discord Spam Bot

This is a Python script that you can use to annoy your friends on Discord

## Installation

```bash
git clone https://github.com/Darkkid819/spammer.git
python -m venv venv
pip install -r requirements.txt
```

## Usage

### Command-line Arguments

- `-m`, `--message` (optional): The message you want to spam.
- `-f`, `--file` (optional): The path to a text file that contains the message to spam.
- `-c`, `--count` (default: 10): Number of times to repeat the spam message.
- `-d`, `--delay` (default: 1.0): Delay (in seconds) between each message send.

### Example Usage

1. **Spamming a message from a file**:

```bash
python spammer.py -f /path/to/message.txt -c 5 -d 5.0
```
