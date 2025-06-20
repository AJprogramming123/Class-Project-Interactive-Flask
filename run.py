'''
This is where the main execution happens. I set it up to use imports so Python knows exactly where to look for things based on the path—it just makes the program easier to manage and read.

From what I’ve learned, using a src folder is a cleaner way to organize the code. It helps keep things more expandable and straightforward. In my case, I went with App.__init__.py instead of just using src.__init__.py to make it a little more specific and modular.

I found out about simplifying Python project configuration by unifying package setups.
- "https://realpython.com/python-pyproject-toml/"
- 
'''

import sys

from App import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
#Flask is an HTTP server, anything that wants to talk to it (like Nginx or curl) needs to send HTTP requests to that port.
