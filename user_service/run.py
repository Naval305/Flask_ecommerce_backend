# command line run : flask --debug --app run run

import os
import sys


sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.main import create_app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
