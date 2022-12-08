books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

def get_top_3(books):
    books = dict(sorted(books.items(), key=lambda x: x[1], reverse=True)[:3])
    for n, v in enumerate(books):
        print(f'{n + 1}. {v} : {books[v]}')

get_top_3(books)

