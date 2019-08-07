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
    code = 0;
    while code < 1:
        try:
            GetURL2("https://birdsite.monster/" + handle);
            code = 1;
        except urllib2.HTTPError:
            print "There was an error on Birdsite's servers; the website might be down.";
            time.sleep(5);
    print "ActivityPub account: @" + handle + "@birdsite.monster";
    main();
main();
