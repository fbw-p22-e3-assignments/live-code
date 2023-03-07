from faker import Faker
import random

faker = Faker()

for _ in range(10):
    # sql = "INSERT INTO friends (name) VALUES ('{}');"
    # print(sql.format(faker.name()))
    sql = "INSERT INTO messages (friends_id, message) VALUES ({}, '{}');"
    print(sql.format(random.randint(1, 10), faker.text()))
