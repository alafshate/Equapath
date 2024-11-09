from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/portal', methods=['GET', 'POST'])
def portal():
    """ Login functionality for a user looking for a job.
    """
    return


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ Login functionality for a user looking for a job.
    """
    return


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    """ Logout functionality for a user looking for a job.
    """
    pass


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ Signup functionality for a user looking for a job.
    """
    pass


@app.route('/login/recruiter', methods=['GET', 'POST'])
def login_recruiter():
    """ Login functionality for a recruiter.
    """
    pass


@app.route('/logout/recruiter', methods=['GET', 'POST'])
def logout_recruiter():
    """ Logout functionality for a recruiter.
    """


def signup_recruiter():
    """ Signup functionality for a recruiter.
    """


if __name__ == "__main__":
    app.run(debug=True)
