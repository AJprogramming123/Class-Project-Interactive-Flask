# Email Breach Checker

This is a Flask web application that lets users check whether their email address has been involved in a data breach using an external API.

## How to Run the Application

1. **Set up your `.env` file:**

   * Create a `.env` file in the root directory.
   * Add your API key:

     ```
     RAPIDAPI_KEY=your_rapidapi_key_here
     ```

2. **Install dependencies:**

   ```
   pip install -e .
   ```

3. **(Optional)** Create and activate a virtual environment:

   ```
   python -m venv venv
   venv\Scripts\activate   # For Windows
   source venv/bin/activate  # For Mac/Linux
   ```

4. **Run the app:**

   ```
   python run.py
   ```

## API Used

* **Email Breach Search API**

  * Provided by RapidAPI
  * Link: [https://rapidapi.com/databreach-com-databreach-com-default/api/email-breach-search](https://rapidapi.com/databreach-com-databreach-com-default/api/email-breach-search)
  * Used to check if a submitted email address has appeared in known data breaches

## Features

* Clean and modular Flask app structure using `src/` layout
* `__init__.py` used for proper package initialization
* Dynamic HTML rendering using Jinja2
* Static webpage displaying breach info for each email
* `.env` support for secure API key management
* `pyproject.toml` used for dependency and path configuration
* Input validation using regular expressions
* Two client-side alert popups:

  * One for invalid email format
  * One when no breach data is found
* Three manual test cases using `print()` to simulate test validation logic
* Scalable design that supports expanding with more Flask Blueprints

