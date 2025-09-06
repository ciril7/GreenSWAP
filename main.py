from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ---------- Page Routes ----------
@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/register-page")
def register_page():
    return render_template("register.html")

@app.route("/profile-page")
def profile_page():
    return render_template("profile.html")


# ---------- API Routes ----------
@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    return {"message": f"User {username} registered successfully!"}


@app.route("/api/user/<username>", methods=["GET"])
def get_user(username):
    return {
        "username": username,
        "eco_points": 50,   # demo
        "history": [{"action": "bought", "item": {"name": "Book"}}]
    }



@app.route("/marketplace-page")
def marketplace_page():
    return render_template("marketplace.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    # Expanded demo items
    items = [
        {"name": "Book", "category": "Books", "price": 50},
        {"name": "Laptop", "category": "Gadgets", "price": 1500},
        {"name": "Chair", "category": "Furniture", "price": 200},
        {"name": "Smartphone", "category": "Gadgets", "price": 1200},
        {"name": "Desk Lamp", "category": "Electronics", "price": 80},
        {"name": "Notebook", "category": "Stationery", "price": 30},
        {"name": "Backpack", "category": "Accessories", "price": 100},
        {"name": "Headphones", "category": "Gadgets", "price": 300},
        {"name": "Coffee Table", "category": "Furniture", "price": 350},
        {"name": "Pen Set", "category": "Stationery", "price": 25},
        {"name": "Water Bottle", "category": "Accessories", "price": 40},
        {"name": "Gaming Console", "category": "Electronics", "price": 400},
        {"name": "T-shirt", "category": "Clothing", "price": 60},
        {"name": "Sneakers", "category": "Clothing", "price": 150},
        {"name": "Wristwatch", "category": "Accessories", "price": 250},
        {"name": "Tablet", "category": "Gadgets", "price": 900},
        {"name": "Bookshelf", "category": "Furniture", "price": 500}
    ]
    return jsonify(items)



@app.route("/add-item-page")
def add_item_page():
    return render_template("add-item.html")



if __name__ == "__main__":
    app.run(debug=True)
