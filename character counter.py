import pprint
message =  'I like to ride my bicycle I like to ride my biiiiike'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
