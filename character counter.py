import pprint
MESSAGE =  'I like to ride my bicycle I like to ride my biiiiike'
COUNT = {}

for CHARACTER in message.upper():
    COUNT.setdefault(CHARACTER, 0)
    COUNT[CHARACTER] = COUNT[CHARACTER] + 1

pprint.pprint(COUNT)
