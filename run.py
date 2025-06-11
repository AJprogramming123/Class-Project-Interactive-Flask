'''
This is where the main execution happens. I set it up to use imports so Python knows exactly where to look for things based on the path—it just makes the program easier to manage and read.

From what I’ve learned, using a src folder is a cleaner way to organize the code. It helps keep things more expandable and straightforward, especially when using the __name__ == '__main__' trick. In my case, I went with App.__init__.py instead of just using src.__init__.py to make it a little more specific and modular.

I found out about simplifying Python project configuration by unifying package setups.
- "https://realpython.com/python-pyproject-toml/"
- 
'''

import sys

#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from App import app

if __name__ == '__main__':
    app.run(debug=True)


