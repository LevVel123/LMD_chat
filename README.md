[Russian version of README](README.ru.md)

# Local Chat Messenger LMD (CLI)

A simple command-line interface messenger for local network communication, written in Python.

## Features

- Real-time messaging
- Multi-user support
- Personalized nicknames
- Easy local network deployment

## Requirements

- Python 3.6 or newer
- Local network connectivity between computers

## Installation (for development)

1. Clone the repository or copy `src/server/server.py` and `src/client/client.py` files to your computers
2. Ensure Python is installed and added to PATH

## Installation (for end users)
### Windows

1. Download the zip archive
2. Extract to a convenient location on your PC

### Mac OS
Coming soon

### Linux
Coming soon

## Usage (for development)

### Starting the Server

On the computer that will act as server:
```bash
python server.py [--host IP] [--port PORT]
```
Arguments:
- `--host` - Server IP address (default: 0.0.0.0)
- `--port` - Server port (default: 5555)

### Starting the Client

On participant computers:
```bash
python client.py [--host SERVER_IP] [--port PORT]
```
Arguments:
- `--host` - Server IP address (required)
- `--port` - Server port (default: 5555)

After starting the client, you'll be prompted to enter a nickname for the chat.

## Usage (for end users)
### Windows
#### Starting the Server
On the server computer:
1. Navigate to the extracted archive folder
2. Open the `bin/win` directory
3. Run `LMDserver.exe`

#### Starting the Client
On participant computers:
1. Navigate to the extracted archive folder
2. Open the `bin/win` directory
3. Run `LMDclient.exe`

## Chat Commands

- Type messages and press Enter to send
- Type `\exit` to quit

## License

MIT License. Use at your own risk.

