a=["Never gonna give you up",
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']
hack=0
for i in range(int(input())):
    if input() in a:
        continue
    else:
        hack=1
print('Yes' if hack else 'No')