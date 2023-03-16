import textblob#to import
from textblob import TextBlob
def get_sentiment(text):
    """
    This function takes in a text string and returns the sentiment polarity as a float value ranging from -1 to 1,
    where -1 is a negative sentiment, 0 is a neutral sentiment, and 1 is a positive sentiment.
    """
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    return sentiment_polarity

# Example usage:
text = "I really enjoyed our conversation today!"
sentiment = get_sentiment(text)
if sentiment > 0:
    print("That's great to hear!")
elif sentiment == 0:
    print("Thanks for letting me know.")
else:
    print("I'm sorry to hear that.")



    #
    import random
from textblob import TextBlob

#1 name and nickname conversation

print("Hello hooman, what's your name?!")
name = input()
print('Do you have a nickname?! [y/n] 🙃')
ans = input()
if 'y' in ans.lower():
  print("What's your nickname?!😍")
  nickname = input()
  print('Good to meet you ' + nickname + '😁')
else:
  name_list = ['killua', 'gon', 'naruto', 'idiot', 'xoxo', 'kimchi', 'fatty-mcFat', 'mother-coconuts', 'phineas',
               'ferb', 'tennison', 'gwen', 'prarthana', 'meow', 'tuple', 'silly goose', 'babe', 'rose', 'tupperware', 'dude']
  nickname = random.choice(name_list)
  print('I will call you '+nickname + '😜')

#2 greeting selection
greetings = [
    'How are you today ' + nickname + '?',
    'Howdy ' + nickname + " friend, how you feelin' today?",
    "What's up " + nickname + '?',
    'Greetings ' + nickname + ' are you well?',
    'How are things going ' + nickname + '?'
]
print(random.choice(greetings))
ans = input()
blob = TextBlob(ans)

if blob.polarity > 0:
  print('Glad you are doing well!😊')
else:
  print('Sorry to hear that! 😔')


#3 several random opinions

topics = [
    'football',
    'coding',
    'Marvel',
    'DC',
    'Python',
    'Computer Games',
    'pubg',
    'COD'
]

questions = [
    'What is your take on ',
    'What do u think about ',
    'How do u feel about ',
    'What do u reckon about ',
    'I would like your opinion on '
]
for i in range(0, random.randint(3, 4)):
  question = random.choice(questions)
  questions.remove(question)
  topic = random.choice(topics)
  topics.remove(topic)
  print(question + topic+'?')
  ans = input()
  blob = TextBlob(ans)

  if blob.polarity > 0.5:
    print("OMG, you really love "+topic)
  elif blob.polarity > 0.5:
    print("Well, you clearly like "+topic)
  elif blob.polarity < -0.5:
    print("Uff, you totally hate "+topic)
  elif blob.polarity < -0.1:
    print("So you don't like "+topic)
  else:
    print('That is a very neutral view on '+topic)

  if blob.subjectivity > 0.6:
    print('and you are so biased!')
  elif blob.subjectivity > 0.3:
    print('and you are bit biased!')
  else:
    print('and you are quite objective, huh!')

#4 random goodbye

goodbyes = [
    'It was good talking to u ' + nickname + 'I gotta go now!',
    "OK I'm bored, I go watch NetFlix",
    "Bye Bye American Pie, I'm out!",
    "Catch ya later " + nickname
]

print(random.choice(goodbyes))
