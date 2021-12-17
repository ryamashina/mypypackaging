python3 -m venv .venv --prompt mypypackaging
source .venv/bin/activate

mkdir mypypackaging
mkdir tests
touch setup.py
touch setup.cfg
touch mypypackaging/__init__.py
touch tests/__init__.py

pip install ipython


