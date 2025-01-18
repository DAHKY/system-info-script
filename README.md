# System Info Script

A Python script to display detailed system information, including CPU, memory, disk, and network details.

## Features
- Display system details: OS, release, machine, and processor.
- Show CPU cores, frequency, and usage.
- List memory stats like total, used, and available memory.
- Display disk partition information.
- Retrieve network hostname and IP address.

## Requirements
- Python 3.8 or later
- Libraries: `psutil`, `platform`, `socket`

## Installation
1. Clone the repository:
   ```py
   git clone https://github.com/DAHKY/system-info-script.git

2. Navigate to the directory:
   ```py
   cd system-info-script

## Usage
1. Run the Script
   ```py
   python system_info.py

2. Output Example
   ```py
   pip install -r requirements.txtSystem Information: {'System': 'Windows', 'Node Name': 'PC', 'Release': '10', ...}
   CPU Information: {'Physical Cores': 4, 'Total Cores': 8, ...}
   ...
