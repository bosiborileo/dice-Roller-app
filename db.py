import sqlite3

# Create a new database and table
conn = sqlite3.connect('responses.db')
c = conn.cursor()
c.execute('CREATE TABLE responses (id INTEGER PRIMARY KEY, text TEXT, category TEXT)')
conn.commit()

# Insert responses into the table
responses = [
    ('Hello!', 'greeting'),
    ('How can I help you today?', 'help'),
    ('Sorry, I did not understand your request.', 'unknown')
]
c.executemany('INSERT INTO responses (text, category) VALUES (?, ?)', responses)
conn.commit()

# Retrieve a response based on user input
user_input = 'Hello'
c.execute('SELECT text FROM responses WHERE category=?', ('greeting',))
result = c.fetchone()
if result:
    response = result[0]
else:
    response = 'Sorry, I did not understand your request.'

# Update a response in the table
new_response = ('Hello there!', 'greeting')
c.execute('UPDATE responses SET text=? WHERE category=?', new_response)
conn.commit()

# Delete a response from the table
c.execute('DELETE FROM responses WHERE category=?', ('unknown',))
conn.commit()

# Close the database connection
conn.close()
