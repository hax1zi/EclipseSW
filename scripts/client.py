import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from spy.network import handle_client

if __name__ == "__main__":
    handle_client()