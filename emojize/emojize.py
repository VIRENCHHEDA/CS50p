import emoji

message = input("Input: ")                    #taking input of the command

print(emoji.emojize("Output: " + message, language = "alias"))

#using emojize function of the emoji package (installed through pip)which converts the text to emoji
#By default, only the official list is enabled but doing emoji.emojize(language='alias') enables both the full list and aliases.
