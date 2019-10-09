import json
import urllib.request
from urllib.error import URLError, HTTPError


while True:

    print('\nUpvotes Comparer\n')
    print('Menu:')
    print('1) Compare upvotes on recent post')
    print('2) Compare total upvotes and downvotes')


    choice = 0

    while True:
        print('Please enter a choice: ')
        a = input()

        if a=='1':
            choice = 1
            break
        elif a=='2':
            choice = 2
            break
        else:
            print('Wrong choice, please try again ')

   

    print('Enter username of first user:')
    user1 = str(input())
    print('Enter username of second user:')
    user2 = str(input())

    url = "http://www.reddit.com/user/"
   
    url1 = url + user1 + '.json'
    url2 = url + user2 + '.json'
    
    req1 = urllib.request.Request(url1, headers={'user-agent':'bot by arvindranjit'})
    req2 = urllib.request.Request(url2, headers={'user-agent':'bot by arvindranjit'})

    print('Gathering Data.........\n')
    urlflag = 0
    try:
        responseuser1 = urllib.request.urlopen(req1)

    except HTTPError as e:
        # do something
        print('\nError code: ', e.code)
        print('Please check whether username 1 is correct')
        urlflag = 1
    except URLError as e:
        # do something (set req to blank)
        print('\nReason: ', e.reason)
        print('Please check whether username 1 is correct')
        urlflag = 1


    

    try:
        responseuser2 = urllib.request.urlopen(req2)
    except HTTPError as e:
        # do something
        print('\nError code: ', e.code)
        print('Please check whether username 2 is correct\n')
        urlflag = 1

    except URLError as e:
        # do something (set req to blank)
        print('\nReason: ', e.reason)
        print('Please check whether username 2 is correct\n')
        urlflag = 1

    if urlflag == 1:
        break

    datauser1 = json.loads(responseuser1.read())
    datauser2 = json.loads(responseuser2.read())
    
    up1 = 0
    up2 = 0




    if choice == 1:

        dict1 = datauser1["data"]["children"][0]
        up1 = int(dict1["data"]["ups"])
        subreddit1 = dict1["data"]["subreddit_name_prefixed"]

        dict2 = datauser2["data"]["children"][0]
        up2 = int(dict2["data"]["ups"])
        subreddit2 = dict2["data"]["subreddit_name_prefixed"]

        upword = 0

        if up1 == 1 or up1 == -1:
            upword = 'upvote'
        else:
            upword = 'upvotes'

        print('Latest post by', user1, 'is in subreddit', subreddit1, 'and has', up1, upword)
        
        if up2 == 1 or up2 == -1:
            upword = 'upvote'
        else:
            upword = 'upvotes'
        print('Latest post by', user2, 'is in subreddit', subreddit2, 'and has', up2, upword)



        if up1==up2:
            print(user1, 'and', user2, 'have equal upvotes for their latest posts')
        else:

            if up1-up2 == 1 or up1-up2 == -1:
                upword = 'upvote'
            else:
                upword = 'upvotes'
            
            if up1>up2:
                print(user1, 'has ', up1-up2, 'more', upword, 'than', user2, 'in their latest post')
            else:
                print(user2, 'has ', up2-up1, 'more', upword, 'than', user1, 'in their latest post')

   
    elif choice == 2:

        upvotes1 = 0
        upvotes2 = 0
        downvotes1 = 0
        downvotes2 = 0

        for item1 in datauser1["data"]["children"]:
            upvotes1 += int(item1["data"]["ups"])
            downvotes1 += int(item1["data"]["downs"])

        for item2 in datauser2["data"]["children"]:
            upvotes2 += int(item2["data"]["ups"])
            downvotes2 += int(item2["data"]["downs"])

        

        upword = 0

        if upvotes1 == 1 or upvotes1 == -1:
            upword = 'upvote'
        else:
            upword = 'upvotes'

        if downvotes1 == 1 or downvotes1 == -1:
            downword = 'downvote'
        else:
            downword = 'downvotes'


        print(user1, 'has a total of', upvotes1, upword, 'and', downvotes1, downword, 'for their posts on Reddit')


        if upvotes2 == 1 or upvotes2 == -1:
            upword = 'upvote'
        else:
            upword = 'upvotes'
        
        if downvotes2 == 1 or downvotes2 == -1:
            downword = 'downvote'
        else:
            downword = 'downvotes'


        print(user2, 'has a total of', upvotes2, upword, 'and', downvotes2, downword, 'for their posts on Reddit')


        if upvotes1==upvotes2:
            print(user1, 'and', user2, 'have equal upvotes for their posts')
        else:

            if upvotes1-upvotes2 == 1 or upvotes1-upvotes2 == -1:
                upword = 'upvote'
            else:
                upword = 'upvotes'
            
            if upvotes1>upvotes2:
                print(user1, 'has', upvotes1-upvotes2, 'more', upword, 'than', user2)
            else:
                print(user2, 'has', upvotes2-upvotes1, 'more', upword, 'than', user1)



    print('Do you want to do this again? Y/N')      

    choice2 = 0

    while choice2 == 0:
        print('Please enter a choice: ')
        a = str(input())

        if a == 'Y':
            choice2 = 1
        elif a== 'N':
            choice2 = 2
        else:
            print('Wrong choice, please try again ')
        
        if choice2 != 0:
            break
    
    if choice2 == 2:
        break













