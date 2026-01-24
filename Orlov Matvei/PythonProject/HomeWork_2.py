text = "The quick brown fox jumps over the lazy dog."


print (f"{text.lower()}")   
print(f"{text.replace('.', '')}")

text_2 = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]


print("\n\n")

for i in range(len(text_2)):
    print(text_2[i], end=" ")

text_2.sort()

print()


words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]

for i in range(0, len(words[i])):
    if len(words[i]) >= 3:
         print(f"Max len = {max(words[i])}")

