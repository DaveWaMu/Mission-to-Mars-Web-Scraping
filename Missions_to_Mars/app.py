from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)

#PyMongo
app.config["MONGO_URI"] = "mongodb://localhost:27017/phone_app"
mongo = PyMongo(app)

@app.route("/scrape")
def call_scrape():
    mars = mongo.db.mars
    scrape_dict = scrape_mars.scrape()
    mars.update({}, scrape_dict, upsert=True)
    return redirect('/', code=302)

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars_key=mars)

if __name__ == "__main__":
    app.run(debug=True)