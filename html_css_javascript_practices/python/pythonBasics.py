x = 10

type(x)

print(x)

if x > 9 :
    print('bigger than 9')

for i in [1, 2, 3, 4, 5] :
    print(i)

smallest = None
print('Before')
for value in [9, 41, 12, 3, 74, 15] : 
    if smallest is None :
        smallest = value
    elif value < smallest : 
        smallest = value
    print(smallest, value)
print('After', smallest)

# "is" is the equivalent to "===" , preferable just use "==" most of the time

word = 'word'
print(word[0])
print(len(word))

# python was named after the "monty python flying circus"

s = 'Monty Python'
print(s[0:4]) # starts at 0 index and up to 4 but not including 4 . so Mont
print(s[6:20]) # it will just print Python 
print(s[:]) # will print whole thing

fruit = 'banana'
'n' in fruit # true
'm' in fruit # false
if 'n' in fruit :
    print("Found it")

greet = "Hello Bob"
zap = greet.lower()
zip = greet.upper()
print(zap) # will print "hello bob"
print(zip) # will print "HELLO BOB"

stuff = 'Hello world'
dir(stuff) # will give you most if not all built-in methods that can work with this type of value

food = 'banana'
a = food.find('a')
print(a) # will print 3
b = food.find('z')
print(b) # will print -1 if not found

greetTwo = 'Hello Bob'
greetReplaced = greetTwo.replace('Bob', 'Jane')
print(greetReplaced) # will print 'Hello Jane'
greetReplacedTwo = greetTwo.replace('o', 'X')
print(greetReplacedTwo) # will print 'HellX BXb'

greetWithSpace = '      Hello Bob  '
greetWithSpace.lstrip() # "Hello Bob   "
greetWithSpace.rstrip() # "       Hello Bob"
greetWithSpace.strip() # "Hello Bob" also striped \n at ends 

line = "Please have a nice day"
line.startswith('Please') # true
line.startswith('P') # false 

fhand = open('stuff.txt') # file handle open for read
for line in fhand : 
    print(line)
# will print each line in that file
count = 0
for line in fhand :
    count = count + 1
print("Line Count: ", count) # will print how ever many lines there are in that file 
allLines = fhand.read() # will but all content in file into a single string with '\n' inbetween lines
print(len(allLines)) # will print all characters in string

fname = input("Enter the file name :   ")
fFile = open(fname) # instead of a fixed file , you could use are responsive 

try: 
    print(fFile)
except:
    print("hello world")
    quit()
# try block 

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
purse['candy'] = purse['candy'] + 2
print(purse)

lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

# basically objects in javascripts but called Dictionary Literals > Dictionary > Dict 

ccc = dict()
'cven' in ccc # will return false

counts = dict()
names = ['richard', 'ricky', 'jenn', 'miu', 'vu']
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
x = counts.get('Henry', 0) # will return 0 because there is no henry 

jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100 }
for aaa,bbb in jjj.items() :
    print(aaa, bbb)

# little excercise # 1 
name1 = input('Enter file: ')
handle = open(name1)

counts = dict()
for line in handle :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
# this exercise should give you biggest count of the same word and count value of that word 

#tuples are 'immutable' unlike a list, once you create a tuple, you cannot alter its contenets - similar to a string
c = (4, 2, 1) 
# c[0] = 0        will not work
# you can dir(tuple) for availability

(0, 1 , 2) < (5, 1, 2) # equals true , it checks first element and moves until its true 

d = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in d.items() :
    tmp.append( (v, k) )
print(tmp) # [(10, 'a'), (22, 'c'), (1, 'b')]
tmp = sorted(tmp, reverse=True)
print(tmp) # [(22, 'c'), (10, 'a'), (1, 'b')]

fhand = open('romeo.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)

# shorter form of above exercise
d = {'a': 10, 'b': 1, 'c': 22}
print( sorted( [ (v,k) for k, v in c.items() ] ) )
# will print [(1, 'b'), (10, 'a'), (22, 'c')]

import re # for regex

#re.search() returns a True/False depending on whether the string matches the regular expresssion 
#If we actually want the matching strings to be extracted, we use re.findall() 
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y) #    ['2', '19', '42']

y = re.findall('[AEIOU]+', x)
print(y) #   []

#socket practice , a HTTP Request in Python
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # making the socket
mysock.connect(('data.pr4e.org', 80)) # makes phone call and connects to a web server, if crash if server is not up 
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #usually the server will talk but we will talk first in this line
mysock.send(cmd) # send the talk through phone call 

# needs '\n\n' to indicate end of headers and then contents of file will start printing to console

while True: 
    data = mysock.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode())
mysock.close() 

# this is vey simple web browser 

# using ASCII w/ UTF-8 instead of UTF-16 or UTF-32 is better because UTF-8 is 1-4 bytes 
# which is very compatible with ASCII , although UTF-32 is the full version with almost every

# Since HTTP is so common, we have a library that does all the socket work for us and makes web pages look like a file

import urllib.request, urbllib.parse, urllib.error

fhand = urllib.request.urlopen('http:..data.pr4e.org/romeo.txt') # open file
for line in fhand: # read through it 
    print(line.decode().strip()) # print it 

# less lines for a simple web browser , will not output headers , just contents of file

# web scraping is when a program or script pretends to be a browser and retrieves web pages , 
# looks at those web pages, extracts information, and then looks at more web pages
# Search engines scrape web pages - we call this "spidering the web" or "web crawling"
# There is some controversy about web page scraping and some sites are a bit snippy about it
# republiching copyrighted information is not allowed
# Violating terms of service is not allowed 

# There is broken HTML code everywhere so Beautiful Soup was created to fix that for parsing HTML
# Install BeautifulSoup 

# simple beautifulSoup exercise 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags 
tags = soup('a')
for tag in tags: 
    print(tag.get('href', None))

# summary 
# TCP/IO gives us pipes / sockets between applications 
# We designed application protocols to make use of these pipes 
# HyperText Transfer Protocol (HTTP) is a simple yet powerful protocol
# Python has good support for sockets, HTTP, and HTML parsing

# Sending Data across the "Net" like : PHP Arrays, JavaScript Objects, Python Dictionaries, Java Hashmaps, 
# we need some sort of protocol with multi-type data, "Wire protocol", they need to agree on a format for this
# "Wire format", from (serialize) python dict format to "common format" to (De-serialize) java hashmap format

# most common "universal formats" are XML & JSON , JSON is more common but XML is more precise 

# XML stands for eXtensible Markup Language
# Start tag, end tag, text content, attribute, self closing tag

# XML Schema 
# Description of the legal format of an XML document
# Expressed in terms of contraints on the structure and content of documents 

# XML example 
import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.formastring(input)
lst = stuff.findall('users/user')
print('User count:', len(let))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))


# JSON example

import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "int1", 
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data) # info is a dictionary because it has curly braces 
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])


# another JSON example with a little more depth 

import json
input = '''[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "Chuck"
    }
]'''
info = json.loads(input) # in this case info is a list becuase of square bracket
print('User count:', len(info))
for item in info: 
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# Service Oriented Approach is Most non-trivial web applications use services 
# They use services from other aplications 
    # Credit Card Charge 
    # Hotel Reservation systems 
# Services publish the "rules" applications must follow to make use of the service(API)

# APIs Example 
import urllib.request, urllib.parse, urllib.error
import json

serviceur1 = 'http://maps.googleapis.com/maps/api/geocode/json?' # grabbed URL 

while True:
    address = input("Enter Location: ") # entered Ann Arbor, MI
    if len(address) < 1: break

    url = serviceur1 + urllib.parse.urlencode({'address': address})

    print("Retriveing", url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Faulure to Retrieve ====')
        print(data)
        continue

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]
print('lat', lat, 'lng', lng)
location = js['results'][0]['formatted_address']
print(location)

# Api security and Rate limiting , 
# The compute resources to run these APIs are not "free"
# The data privided by these APIs is usually valuable 
# The data providers might limit the number of requests per day, demand an API "key", or even charge for usage

# Twitter api example 
import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/firends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account: ')
    if (len(acct) < 1) : break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name' : acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.gethearders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('  ', s[:50])

# Twitter api uses OAuth to authenicate users , SOAP and REST are two styles of web services 
"""
 A program is made up of many cooperating objects 
 Instad of being the "whole program" - each object is a little "island" within the 
 program and cooperatively working with other objects. 
 A program is made up of one or more objects working together - objects make use of each other's
 capabilities. An object is abit of self-contained code and Data 
 A key aspect of the Object approach is to break the problem into smaller understandable parts
 (divide and conquer). Objects have boundaries that allow us to ignore un-needed detail.
 We have been using objects all along: string objects, integer objects, dictionary objects , list objects...

"""

"""
Class - a template - Dog 
Method or Message - A defined capability of a class - bark()
field or attribute - A bit of data in a class - length
Object or Instance - A particular instance of a class - Lassie

Terminology - Defines the abstract characteristics of a thing(object), including the thing's characteristics
(its attributes, fields or properties) and the thing's behaviors (the things it can do, or methods,
operations or features). One might say that a class is a blueprint or factory that describes the nature of
somthing. For example, the class Dog would consist of traits shared by all dogs, such as breed and fur color
(characteristics), and the ability to bark and sit (behaviors).

Terminology : Instance , one can have an instance of a class or a particular object. The instance is the
acutal object created at runtime. In programmer jargon, the Lassie object is an instance of the Dob class. 
The set of values of the attributes of a particular object is called its state. The object consists of state
and the behavior that's defined in the object's class. 

Terminology : Method, An object's abilities. In language, methods are berbs. Lassie, being a Dog, had the 
ability to bark. So bark() is one of Lassie's methods. She may have other methods as well, for example sit()
or eat() or walk() or save_timmy(). Within the program, using a method usually affects only one particular
object; all Dogs can bark, but you need only one particular dog to do the barking.

Method and Message are often used interchangeably.

"""

# class example 
class PartyAnimal:
    x = 0 

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)
    
an = PartyAnimal()
an.party()  # will print So far 1
an.party()  # will print So far 2


"""
Contructor - The primary purpose of the constructor is to set up some instance variables to set up some
instance variables to have the proper initial values when the object is created. 

"""

# exercise 1 of class/contructor

class PartyAnimal: 
    x = 0

    def __init_(self):
        print('I am constructed')

    def party(self) :
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)

"""
In object oriented programming, a constructor in a class is a special block of statements called
when an object is created

"""

# example 2 of multiple instances 

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

"""
Inheritance - when we make a new class - we can reuse an existing class and inferit all the capabilities 
of an existing class and then add our own little bit to make our new class 
Another form of store and reuse, Write once - reuse many times 
The new class (child) has all the capabilities of the old class (parent) - and then some more

Terminology: Inheritance , 'Subclasses' are more specialized versions of a class, which inherit attributes
behaviors from their parent classes, and can introduce their own.

"""

# example of inheritance 

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def party(self) :
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "points", self.points)

# FootballFan is a class which extends PartyAnimal. It has all the capabilities of PartyAnimal and more. 

"""
For Python Personal Data Mining - some suggested Technologies 
https://hadoop.apache.org/
http://spark.apache.org/
https://aws.amazon.com/redshift/
http://community.pentaho.com/
"""