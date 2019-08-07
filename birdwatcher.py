#
#
#  notanewbie made this.
#  ____________________
# |  ________________  |
# | |________________| |
# |                    |
# |  ________________  |
# | |                | |
# | |   __________   | |
# | |  |          |  | |
# | |__|          |__| |
# |____________________|
#
#
#

import urllib2;
def GetURL2(link):
    req = urllib2.Request(link, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
    response = urllib2.urlopen(req).read()
    return response;
def main():
    handle = raw_input("What Twitter account would you like to view using ActivityPub?\n");
    if ".com" in handle:
        handle = handle.split(".com/")[1];
    if "@" in handle:
        handle = handle.replace("@", "");
    GetURL2("https://birdsite.monster/" + handle);
    print "ActivityPub account: @" + handle + "@birdsite.monster";
    main();
main();
