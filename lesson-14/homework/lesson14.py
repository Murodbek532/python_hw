# 1
import json

def read_students():
    with open("students.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    for student in data["students"]:
        print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

read_students()

# 2
import requests

def get_weather(city="Tashkent", api_key="YOUR_API_KEY"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}:")
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Condition:", data["weather"][0]["description"])
    else:
        print("Error:", data.get("message"))

# 3
import json

BOOKS_FILE = "books.json"

def load_books():
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"books": []}

def save_books(data):
    with open(BOOKS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_book(title, author):
    data = load_books()
    data["books"].append({"title": title, "author": author})
    save_books(data)

def update_book(old_title, new_title=None, new_author=None):
    data = load_books()
    for book in data["books"]:
        if book["title"] == old_title:
            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
    save_books(data)

def delete_book(title):
    data = load_books()
    data["books"] = [b for b in data["books"] if b["title"] != title]
    save_books(data)

# 4

import requests, random

def recommend_movie(genre, api_key="YOUR_API_KEY"):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    response = requests.get(url)
    data = response.json()

    if "Search" in data:
        movies = data["Search"]
        chosen = random.choice(movies)
        print(f"Recommended movie: {chosen['Title']} ({chosen['Year']})")
    else:
        print("No movies found for this genre.")



