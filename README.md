# ✈️ TravelTrail – Business Travel Optimizer

## 📖 Overview
**TravelTrail** is a Streamlit web application that helps business travelers find and rank the **best flight + hotel combinations**.  
It uses the **Amadeus Travel API** to fetch real-time flight and hotel data, then ranks the results based on:
- **Total cost**
- **Flight duration**
- **Randomized loyalty score** (for demonstration)

---

## ✨ Features
- 🔍 Search flights between cities for given travel dates
- 🏨 Search hotels in the destination city for matching dates
- 📊 Rank and recommend **top 5** flight + hotel combinations
- 🛠 Uses **Amadeus API** for real-time results
- 💻 Built with **Streamlit** for a simple and interactive UI
- 🗂 Modular code structure (separate files for config, flights, hotels, and utilities)

---

## 📂 Project Structure

---

## 🖼 Screenshots

![TravelTrail UI](ScreenShot/Screenshot1.png)
![TravelTrail UI](ScreenShot/Screenshot2.png)

---

## ⚙️ Prerequisites
- Python **3.9+**
- pip (Python package manager)
- An [Amadeus Developer Account](https://developers.amadeus.com/) (for API credentials)

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/nitinrana1504/TravelTrail-Business-Travel-Optimizer.git

cd TravelTrail-Business-Travel-Optimizer

---

### 2️⃣  Set Up Environment Variables
Create a file named `.env` in the project folder and add:
AMADEUS_CLIENT_ID=your_client_id_here

AMADEUS_CLIENT_SECRET=your_client_secret_here

---


### 3️⃣ Run the Application
```bash
streamlit run app.py




