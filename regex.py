import re
pattern = re.compile("y\w+")
string = """I don't think that you even realize
The joy you make me feel when I'm inside
Your universe
You hold me like I'm the one who's precious
I hate to break it to you but it's just
The other way around
You can thank your stars all you want but
I'll always be the lucky one"""
pattern.match(string)

