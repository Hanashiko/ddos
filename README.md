# DDoS Testing Tool

A simple Python script for network stress testing using UDP and TCP flood methods.

## Usage

```bash
python main.py
```

The script will prompt you for:
- **Target IP address**
- **Target port**
- **Protocol** — `y` for UDP, anything else for TCP
- **Number of packets** per thread
- **Number of threads**

Press `Ctrl+C` to gracefully exit.

## Requirements

- Python 3
- `figlet` (optional, for exit banner)
