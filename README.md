# AdminFinder

A Python-based tool for discovering admin panels and login pages on websites.

## Description

AdminFinder is a security testing tool that helps identify potential admin pages and login interfaces on web applications. It uses a comprehensive wordlist to test common admin panel paths and reports which URLs are accessible.

## Features

- 🎯 Tests multiple common admin panel paths
- 🎨 Colorful console output with status indicators
- 📝 Saves discovered admin pages to a file
- ⚡ Timeout handling for unresponsive URLs
- 🔍 Comprehensive wordlist covering various CMS and frameworks

## Requirements

- Python 3.x
- requests
- colorama

## Installation

1. Clone this repository:
```bash
git clone https://github.com/mmdMadi/AdminFinder
cd AdminFinder
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python main.py
```

Enter the target URL when prompted. The tool will:
1. Test all paths from the wordlist
2. Display results with color-coded status
3. Save successful URLs to `goods.txt`

## Supported Platforms

The wordlist includes paths for:
- WordPress
- Joomla
- Drupal
- Magento
- OpenCart
- PrestaShop
- Laravel
- Django
- Flask
- ASP.NET
- Spring
- Node.js/Express
- Ruby on Rails
- And many more...

## Output

- **Green**: Successfully found admin page (HTTP 200)
- **Red**: Page not found or access denied
- **Yellow**: Connection error or timeout

Results are saved to `goods.txt` for later reference.

## Disclaimer

⚠️ **Important**: This tool is for educational and authorized security testing purposes only. Always obtain proper authorization before testing any website. Unauthorized access attempts may be illegal.

## License

This project is open source and available for educational purposes.
