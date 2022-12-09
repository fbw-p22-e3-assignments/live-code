data = {
  'key1': 1,
  'key2': 2,
  'key3': 3,
  'key4': 4,
  'key5': 5,
  'key6': 6,
}

def chunk(data, num):
    result = []
    for i in range(int(len(data)/num)):
        dict_data = {}
        for key, value in list(data.items())[i*num:(i + 1)*num]:
            dict_data[key] = value
        result.append(dict_data)
    return result

print(chunk(data, 3))
print(chunk(data, 2))
print(chunk(data, 1))
print(chunk(data, 6))
print(chunk(data, 5))
