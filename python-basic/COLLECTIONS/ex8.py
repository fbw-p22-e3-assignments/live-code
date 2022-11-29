books = {
  'Harry Potter And The Sorcerer\'s Stone': 1241100000,
  'Harry Potter And The Chamber Of Secrets': 771300000,
  'Harry Potter And The Prisoner Of Azkaban': 65210000,
  'Harry Potter And The Goblet Of Fire': 645600000,
  'Harry Potter And The Order Of The Phoenix': 635600000,
  'Harry Potter And The Half Blood Prince': 661300000,
  'Harry Potter And The Deathly Hallows ': 652200000,
}

# def convert_to_millions(books):
#     return {k: v / 1000000 for k, v in books.items()}

# books = convert_to_millions(books)

def sort_helper(item):
  return item[1]

def get_top_3(books):
    books = dict(sorted(books.items(), key=sort_helper, reverse=True)[:3])
    for n, v in enumerate(books):
        print(f'{n + 1}. {v} : {books[v]}')

get_top_3(books)

