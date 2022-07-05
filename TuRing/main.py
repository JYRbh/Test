# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

response = urllib2.urlopen("http://openapi.turingapi.com/v1/robot/create")
print (response.read())

