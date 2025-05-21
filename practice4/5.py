#Є словник, де ключ — ім’я, а значення — місто.
#Створіть новий словник, де міста стануть ключами,
# а значенням буде список людей, які там живуть.
people = {
    "Anna": "Kyiv",
    "Bohdan": "Lviv",
    "Oksana": "Kyiv",
    "Dmytro": "Odesa"
}
v=people.values()
values=list(set(v))
print(values)
m={}
for i in values:
  m[i] = []
print(m)
for key, value in people.items():
  m[value].append(key)
print(m) 