# Movie-Streaming-Analytics-System-

A **Movie Streaming Analytics System** built with Python, Tkinter, and MongoDB. 
<br>This application allows users to stream movies, manage subscriptions, and view analytics such as ratings and viewing history. 
<br>Admins can manage users, movies, and subscriptions.
<br>Simple GUI using python and connected to MongoDB.

---

## Features

- **User Authentication**: Login as an Admin or User.
- **Movie Search**: Search for movies by title or actor.
- **Subscription Management**: Add, view, and manage movie subscriptions.
- **Analytics**:
  - View movie ratings.
  - Track user viewing history.
- **Admin Panel**:
  - Add, edit, or delete users.
  - Manage movies and subscriptions.

---
## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
2. **MongoDB**: [Install MongoDB](https://www.mongodb.com/try/download/community)
3. **Python Libraries**:
   - `pymongo`: MongoDB driver for Python.
   - `tkinter`: Built-in Python library for GUI.

Install the required libraries using:
```bash
pip install pymongo
```

---

## Set Up
### 1. Clone the Repository
```
git clone https://github.com/your-username/movie-streaming-analytics-system.git
cd movie-streaming-analytics-system
```

### 2. Set Up MongoDB
Start your MongoDB server:
```
mongod
```
Import the sample data into MongoDB:
```
mongoimport --db MovieStream --collection Movies --file data/movies.json --jsonArray
mongoimport --db MovieStream --collection Users --file data/users.json --jsonArray
mongoimport --db MovieStream --collection Subscriptions --file data/subscriptions.json --jsonArray
mongoimport --db MovieStream --collection Admins --file data/admins.json --jsonArray
```

### 3. Run the Application
```
python main.py
```

## Usage
### For Users
1. Log in with your username and user ID.
2. Search for movies by title or actor.
3. Add subscriptions to movies.
4. View your subscribed movies and rate them after watching.

### For Admins
1. Log in with your admin credentials.
   <br>     Admin can not login without admin password which is included in the code.
3. Manage users (add, edit, or delete).
4. Add or update movie ratings.
5. View analytics for movies and users.

## Screenshots
### Home Page
![Home Page](https://github.com/user-attachments/assets/e3ee19de-c5a2-432b-bb04-a73d4e96c15d)

### Login Screen
![Login](https://github.com/user-attachments/assets/6400da25-3a76-4af0-ad04-d5db633c3e44)

### Sign Up as User
![User](https://github.com/user-attachments/assets/114c8481-bc78-4251-bbac-d093c953127b)

### Sign Up as Admin
![Admin](https://github.com/user-attachments/assets/e8bead95-0752-4f70-b8aa-6aeb64c60333)
![Admin2](https://github.com/user-attachments/assets/367bf3d5-8970-49f0-9311-c0f83b58c47e)

### Main Window (User)
![WhatsApp Image 2024-12-30 at 10 55 55 PM](https://github.com/user-attachments/assets/649bc956-3536-4e00-8f35-e0a3434ec3bd)

### Main Window (Admin)
![WhatsApp Image 2024-12-30 at 11 04 00 PM](https://github.com/user-attachments/assets/0096b73a-d104-4537-8523-9e6191eba296)

---
