🌱 GreenSwap – Sustainable Second-Hand Marketplace

GreenSwap is a web-based platform that promotes sustainability by enabling students and community members to buy, sell, or donate second-hand items. By fostering a circular economy, GreenSwap helps reduce waste, save money, and encourage eco-friendly habits.

💡 Problem Statement

Today, many usable items like books, clothes, electronics, and furniture are discarded prematurely. Students and local communities struggle to access affordable resources, leading to unnecessary expenses and a larger carbon footprint. GreenSwap addresses this challenge by creating a trusted community-driven marketplace where items are reused, resold, or donated.

🚀 Features

Marketplace: Browse, buy, and sell second-hand items.

Eco-Points System: Earn rewards for sustainable transactions.

User Profiles: Track personal eco-impact and transaction history.

Item Management: Easily add or remove items.

Verified Community: Focused on safety and trust, especially for students.

🛠 Tech Stack

Backend: Python, Flask, Flask-CORS

Frontend: HTML, CSS, JavaScript, Tailwind CSS

API: RESTful endpoints for user management and item listings

📁 Project Structure
GreenSwap/
 ├── backend/
 │   ├── app.py               # Flask backend server
 │   └── requirements.txt     # Python dependencies
 ├── templates/
 │   ├── index.html           # Home page
 │   ├── register.html        # User registration page
 │   ├── profile.html         # User profile page
 │   ├── marketplace.html     # Marketplace page
 │   └── add-item.html        # Add item page
 ├── static/
 │   └── css/                 # Custom styles (optional)
 └── README.md                # Project documentation

⚡ Installation

Clone the repository

git clone https://github.com/yourusername/GreenSwap.git
cd GreenSwap/backend


Create a virtual environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Run the server

python app.py


Open http://127.0.0.1:5000
 in your browser to view the app.

🔗 API Endpoints

POST /api/register – Register a new user

GET /api/user/<username> – Retrieve user profile and eco-points

GET /api/items – List all available items

🌱 How It Promotes Sustainability

Reduces Waste: Items get reused instead of being thrown away.

Saves Money: Affordable alternatives for students and communities.

Encourages Responsible Behavior: Gamified eco-points reward sustainable actions.

Community Engagement: Builds trust and collaboration in verified local communities.

📌 Future Enhancements

Real-time chat between buyers and sellers

Item donation tracking for charity

Advanced search and filtering

Mobile-friendly responsive design

Analytics dashboard for eco-impact metrics

👥 Contributors

Nandu – Fullstack Development & Design

[Add other team members here if applicable]

📄 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
