thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
print(type(thistuple))

dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictionary)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)

x = car.keys()
print(x)

car.update({"color": "White"})
print(car)
