## AI Lab - Environment & Workflow Setup

This document captures the full setup used for the **AI Lab** repository.
It ensures consistent reproducibility for all projects under this workspace.

### System Environment
**Platform:** Ubuntu on WSL2 (Windows 11) Python 3.10
**Python version:** 3.10.12
**Primary Tools:**
- Git
- GPG (Optional)
- Python virtualenv
- pip + wheel + setuptools
- IPython (terminal-based REPL)

---

### Repository Initialization
```bash
mdkir ai-lab
cd ai-lab
git init
git remote add origin https://github.com/naverdocker/ai-lab.git;

## OR ##

git clone https://github.com/naverdocker/ai-lab.git
cd ai-lab
```
```
create .gitignore:
add a minimal README.md
```

### Python Virtual Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install "pandas<2.3" numpy matplotlib scikit-learn ipython
```

### GPG Setup for Signed Commits (Optional)
```bash
gpg --full-generate-key
gpg --list-sectet-keys --keyid-format=long
git config --global user.signingkey <keyid>
git config --global commit.gpgsign true
```

### Git Operations
```bash
git add .
git commit -m "commit message"
git push -u origin main
```

### Repository Structure Convention
```
ai-lab/
├── .venv/                 # virtual environment (ignored)
├── .gitignore
├── README.md              # overview
├── SETUP.md               # this document
├── requirements.txt       # dependency record
└── projects/
    ├── house-price/
    │   ├── README.md
    │   ├── NOTES.md
    │   └── src/main.py
    └── ...
```

### Workflow Summary
```
Activate venv → source .venv/bin/activate
Work inside projects/<project-name>
Run experiments → commit → push
Document notes in NOTES.md
```
