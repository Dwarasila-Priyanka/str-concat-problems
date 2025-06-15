#  1. Input: chaitanya → Output: aiaa

text = "chaitanya"
vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch in vowels:
        result += ch

print(result)

# 2. Concatenate characters at even positions

text = "chaitanya"
result = ""

for i in range(len(text)):
    if i % 2 == 0:  # even index
        result += text[i]

print(result)

#  3. Take two indexes and concatenate characters in that range

text = "chaitanya"
start = 1
end = 4  # exclusive, so we go until end-1

result = ""

for i in range(start, end):
    result += text[i]

print(result)

