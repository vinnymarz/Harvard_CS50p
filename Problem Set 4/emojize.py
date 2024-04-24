import emoji

emojicon = input("Input: ").strip()
print(emoji.emojize(emojicon, language = "alias"))
