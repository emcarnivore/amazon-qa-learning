## Install Instructions

### Homebrew
1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

### Python
1. `brew install python3`
2. `brew upgrade python3`

### PIP
1. `cd /Users/nic/Documents/PY3/Amazon`
2. `python3 -m pip install -r requirements.txt`

### ChromeDriver
1. `brew install --cask chromedriver`
2. `ls -la /opt/homebrew/bin | grep chromedriver`
3. Copy the path to the chromedriver file (excluding "chromedriver" at end of path)
    - Example: "/opt/homebrew/Caskroom/chromedriver/99.0.4844.51/"
4. `open {copied path}`
    - Example: `open /opt/homebrew/Caskroom/chromedriver/99.0.4844.51/`
5. Right click on "chromdriver" file
6. Click "open"
7. Update Chrome Browser
