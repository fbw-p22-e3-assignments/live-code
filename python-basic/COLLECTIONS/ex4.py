import re   


natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}

def convert_to_snake_case(natural_case):
  snake_case = {}
  for key, value in natural_case.items():
    snake_case[re.sub(r'\s+', '_', key).lower()] = value
  return snake_case

print(convert_to_snake_case(natural_case))

natural_case = {
  'Movie name': 'James Bond 007: Skyfall',
  'Director': 'Sam Mendes',
  'Production Year': 2012,
  'Duration in minutes': 143,
  'Production countries': ['US', 'UK']
}

print(convert_to_snake_case(natural_case))
