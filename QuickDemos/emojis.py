import emoji

print(emoji.emojize(":thumbs_up:", use_aliases=True))
print(emoji.emojize(":angry:", use_aliases=True))
print(emoji.emojize(":cry:", use_aliases=True))
print(emoji.demojize('👍'))
print(emoji.demojize('😠'))
print(emoji.demojize('😢'))