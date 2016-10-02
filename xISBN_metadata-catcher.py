import urllib.request
from urllib.error import URLError, HTTPError

def xisbn_func(ISBN):
    # Here starts connection check
    try:
        resp = urllib.request.urlopen("http://xisbn.worldcat.org/webservices/xid/isbn/"+str(ISBN)+"?method=getMetadata&format=xml&fl=*")
    except HTTPError as err:
        print('The server couldn\'t fulfill the request.'); print('Error code: ', err.code);
    except URLError as err:
        print('Failed to reach the server.'); print('Reason: ', err.reason);

    else:
        data = resp.read(); text = data.decode('utf-8')     # Here the response is converted and decoded

        # Here starts ISBN check
        if text.find('stat="ok"') >= 0 :    # stat="ok" is present in the xml response to the HTTP request
                                            # if the digited ISBN is valid and if is found in the xISBN database
            print('\n... Book [-FOUND-]')
            newline = '\n'; content = text + newline        # formatting the text
            f = open("Books_ls.xml", "a+t")        # creating the file
            if ISBN in open("Books_ls.xml").read():     # checking if your ISBN was already added to your list
                print('\n>> The digited ISBN is already in your list.')
            else:
                f.write(content)        # writing formatted text into the file
                f.close()       # close the file
        else:
            print('Invalid ISBN!/t This means that digited ISBN is wrong or not present in the WorldCat database')

def answering(ans):
    ans = input('\nAny other ISBN?  (y/n) ... ')
    if ans == 'y' :
        ISBN = input('\n> Digit ISBN : '); xisbn_func(ISBN); answering(ans)     # repeat the loop
    elif ans == 'n' :
        print('.\n.\n.\nQuit')      # Quit
    else:
        print('Unespected character!')


ISBN = input('\n> Digit ISBN : ')
xisbn_func(ISBN)
ans = None      # resetting the variable
answering(ans)
