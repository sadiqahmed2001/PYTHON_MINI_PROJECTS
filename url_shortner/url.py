import sqlite3
import hashlib

# Database setup
DB_FILE = 'urls.db'

def init_db():
    """Initialize the database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        original_url TEXT NOT NULL,
                        short_url TEXT NOT NULL UNIQUE)''')
    conn.commit()
    conn.close()

def shorten_url(original_url):
    """Generate a shortened URL and save it to the database."""
    short_url = hashlib.md5(original_url.encode()).hexdigest()[:6]
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
    conn.commit()
    conn.close()
    return short_url

def expand_url(short_url):
    """Retrieve the original URL from the database using the short URL."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None

def main():
    init_db()
    while True:
        print("\nURL Shortener")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            original_url = input("Enter the original URL: ")
            short_url = shorten_url(original_url)
            print(f"Shortened URL: {short_url}")
        elif choice == '2':
            short_url = input("Enter the short URL: ")
            original_url = expand_url(short_url)
            if original_url:
                print(f"Original URL: {original_url}")
            else:
                print("Short URL not found.")
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == '__main__':
    main()
