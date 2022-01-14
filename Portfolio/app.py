from flask import Flask, render_template
from data import portfolio_data
# Create instance of the flash application
app = Flask(__name__)


@app.route("/")
def home():
 #   return render_template('home.html', portfolio_data=portfolio_data, contact_details=contact_details, author_info=author_info)
    return render_template('home.html', portfolio_data=portfolio_data)


# @app.route("/about")
# def about():
#     return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
