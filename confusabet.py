#!/usr/bin/python

import re, random, urllib2

letters = {}

for line in urllib2.urlopen('http://www.unicode.org/Public/security/revision-06/confusables.txt'):
   line = line.strip()

   parts = re.search(r'^(?!1D)([0-9a-fA-F]{4}).*LETTER +([A-Z])\b', line)
   if parts:
      code = parts.group(1)
      canonical = parts.group(2)
      letters.setdefault(canonical, []).append(code)

for key in sorted(letters.keys()):
   print '#' + key
   for l in letters.get(key):
      print l + ' : ' + ('\u' + l).decode('unicode-escape') + "<br>"
   print

for c in 'Hello, word! How are you doing?':
   a = ord(c.upper())
   if a >= ord('A') and a <= ord('Z'):
      uni = random.choice(letters.get(c.upper()))
      print ('\u' + uni).decode('unicode-escape'),
   else:
      print c,
