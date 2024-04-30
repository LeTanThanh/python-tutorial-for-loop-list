if __name__ == "__main__":
  # Using Python for loop to iterate over a list

  """
  for item in list:
    # process the item
  """

  cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]
  for city in cities:
    print(city)

  # Using Python for loop to iterate over a list with index

  cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

  for item in enumerate(cities):
    print(item)

  for index, city in enumerate(cities):
    print(f"{index}: {city}")

  for index, city in enumerate(cities, 1):
    print(f"{index}: {city}")
