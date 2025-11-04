#1-misol
numbers = [-2, -1, 0, 1, 2, 3, 4]
positive_squares = [x**2 for x in numbers if x > 0]
print(positive_squares)

#2-misol
div_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(div_by_3)

#3-misol
text = input("Matn kiriting: ")
uppercase_letters = [ch.upper() for ch in text]
print(uppercase_letters)

#4-misol
numbers = [1, 4, 6, 8, 3, 9]
greater_than_5 = [x for x in numbers if x > 5]
print(greater_than_5)

#5-misol
primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)

#6-misol
text = "Salom dunyo"
vowels = [ch for ch in text if ch.lower() in 'aeiou']
print(vowels)

#7-misol
numbers = [2, 4, 6, 8]
indexed_product = [i * x for i, x in enumerate(numbers)]
print(indexed_product)

#8-misol
numbers = [1, 2, 3, 4, 5, 6]
doubled_evens = [x * 2 for x in numbers if x % 2 == 0]
print(doubled_evens)

#9-misol
texts = ["salom", "hi", "python", "ok", "comprehension"]
long_texts = [t for t in texts if len(t) >= 5]
print(long_texts)

#10-misol
odd_squares = [x**2 for x in range(1, 21) if x % 2 != 0]
print(odd_squares)
