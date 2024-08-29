import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from spy.network import start_server

if __name__ == "__main__":
    start_server()