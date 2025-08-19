# ☕ Cafe & Wifi API

A simple **Flask REST API** built with **SQLite + SQLAlchemy** that serves data about cafes in London.  
The database (`cafes.db`) contains information such as cafe names, locations, amenities, and coffee prices.  

This project demonstrates:
- Building RESTful routes in Flask
- Serializing SQLAlchemy objects into JSON
- Handling CRUD operations (`GET`, `POST`, `PATCH`, `DELETE`)
- API testing with Postman

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask server
python main.py

By default, the API runs at:
👉 http://localhost:5000

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📌 API Endpoints

### 1. Get a random cafe
**GET** `/random`  
Returns a random cafe from the database.

---

### 2. Get all cafes
**GET** `/all`  
Returns all cafes as JSON.

---

### 3. Search cafes by location
**GET** `/search?loc=<location>`  
- Example: `/search?loc=Shoreditch`  
- Returns all cafes in a given location.  
- If no cafes found → returns an error message.

---

### 4. Add a new cafe
**POST** `/add`  
Add a new cafe by sending form data (via Postman or similar).  

Required fields:
- `name`, `map_url`, `img_url`, `location`, `seats`
- `has_toilet`, `has_wifi`, `has_sockets`, `can_take_calls`
- `coffee_price`

---

### 5. Update coffee price
**PATCH** `/update-price/<cafe_id>`  
Update the price of coffee for a specific cafe.  

Parameters:
- `new_price` (query param)

Example:  
`/update-price/22?new_price=£3.50`

---

### 6. Report a cafe as closed
**DELETE** `/report-closed/<cafe_id>`  

Requires an API key:
- Correct API Key → `"TopSecretAPIKey"`
- Passed as query param: `api-key`

Example:  
`/report-closed/15?api-key=TopSecretAPIKey`

Responses:
- ✅ Cafe deleted successfully
- ❌ Wrong API key → `403 Forbidden`
- ❌ Cafe not found → `404 Not Found`

---

## 🛠️ Tools & Tech
- Python 3.x
- Flask
- SQLAlchemy
- SQLite
- Postman (for API testing)

---

## 📖 API Testing with Postman
1. Download Postman → [https://www.postman.com/downloads/](https://www.postman.com/downloads/)  
2. Create a collection called **Cafe & Wifi**  
3. Add routes:
   - `/random`
   - `/all`
   - `/search?loc=...`
   - `/add`
   - `/update-price/<id>`
   - `/report-closed/<id>`

---

## 🔐 Notes
- **API Security**: Only DELETE requests require an API key.  
- **Error Handling**: Returns proper JSON error messages.

---

## ✨ Future Improvements
- Add authentication (JWT or OAuth2)
- Deploy API on cloud (Heroku, Render, or AWS)
- Add pagination & filtering
- Generate API documentation via Postman
