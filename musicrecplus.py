# Ria Konar, Molly DiCampli, Daniel Detore
# I pledge my honor that I have abided by the Stevens Honor System


def readDictionary():
  """ Daniel Detore: takes no parameters and 
    returns a dictionary of users and their saved artists.
    creates and returns an empty dictionary if it doesn't exist. """
  dic = {}
  text_file = 'musicrecplus.txt'
  try:
    with open(text_file, "r") as f:
      for line in f:
        [username, artists] = line.strip().split(":")
        artistsList = artists.split(",")
        for i in artistsList:
          i = i.title()
        dic[username] = artistsList
  except FileNotFoundError:
    f = open(text_file, "x")
  return dic


#def printDictionaryCleanly(dic):
#	for key in dic.keys():
#		print(key + ":", dic[key])


def rewriteDictionary(dic):
  """ Daniel Detore: takes a dictionary and writes it to the saved preferences file 
    (creating one if it doesn't exist), overwriting the original file. returns None. """
  usernames = sorted(dic.keys())
  text_file = 'musicrecplus.txt'
  with open(text_file, "w") as f:
    for key in usernames:
      f.write(key)
      f.write(":" + ','.join(dic[key]) + "\n")


def startupSurvey():
  """ Daniel Detore: takes no parameters and returns None.
    asks the user for their name. if they already exist it skips to the menu.
    otherwise it asks for their liked artists. sends the user to the menu on completion. """
  preferences = readDictionary()
  print(
      "Enter your name (put a $ symbol after your name if you wish your preferences to remain private): "
  )
  username = input()
  if username not in preferences:
    thisChoice = " "
    artistList = []
    while True:
      print("Enter an artist that you like (Enter to finish):")
      thisChoice = input().strip().title()
      if thisChoice != "" and thisChoice not in artistList:
        artistList += [thisChoice]
      elif thisChoice == '':
        break
    preferences[username] = sorted(artistList)
  menu(preferences, username)


def menu(preferences, user):
  """ collaborative: preferences must be a dictionary (keys are users and values are
  lists of their liked artists) and user is the name of the current user. returns None."""
  newDict = {}
  for key in preferences.keys():
    if key[-1] != "$" or key == user:
      newDict[key] = preferences[key]

  while True:
    print(
        "Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nq - Save and quit"
    )
    choice = input()
    if choice == "e":  # Enter preferences
      enterPreferences(user, newDict)
    elif choice == "r":  # Get recommendations
      getRecommendations(user, newDict)
    elif choice == "p":  # Show most popular artists
      mostPopularArtist(newDict)
    elif choice == "h":  # How popular is the most popular
      howPopular(newDict)
    elif choice == "m":  # Which user has the most likes
      whichUser(newDict)
    elif choice == "s": # show user preferences
      showPreferences(user, newDict)
    elif choice == "d": # delete preferences
      deletePreferences(user, newDict)
    elif choice == "q":  # Save and quit
      rewriteDictionary(newDict)
      exit()


def enterPreferences(user, dict):
  """Ria Konar: takes a user and the dictionary of usernames and their artist preferences.
  Replaces the preferences saved under that user with their new preferences"""
  dict[user].clear()
  while True:
    print("Enter an artist that you like (Enter to finish):")
    artist = input().strip().title()
    dict[user].append(artist)
    if artist == "":
      break


def getRecommendations(currUser, dict):
  """Ria Konar: Gets recommendations for a user (currUser) based on the users in dict and the user's prefrences
    Returns a list of recommended artists"""
  if len(dict.keys()) == 1:
    # Extra credit -- fixing the Get Recommendations Bug
    print("Error: There are no additional users to recommend preferences.")
  else:
    recommendations = []
    bestUser = findBestUser(currUser, dict)
    bestUserList = dict[bestUser]
    for artist in bestUserList:
      if artist not in dict[currUser]:
        recommendations.append(artist)
        print(artist)
    if recommendations == []:
      print("No recommendations available at this time")


def findBestUser(currUser, dict):
  # helper function
  """Ria Konar: Find the user whose tastes are closest to the current user. Returns the best user's name (a string)"""
  bestUser = None
  bestScore = -1
  for user in dict:
    score = numMatches(dict[currUser], dict[user])
    if currUser != user and score != len(dict[user]):
      if score > bestScore:
        bestScore = score
        bestUser = user

  return bestUser


def numMatches(list1, list2):
  # helper function
  """Ria Konar: Returns the number of items in list1 that are also in list2"""
  if len(list1) > len(list2):
    bigList = list1
    smallList = list2
  else:
    bigList = list2
    smallList = list1

  matches = 0
  for x in bigList:
    if x in smallList:
      matches += 1

  return matches


# most popular artist
def mostPopularArtist(dic):
  '''Molly DiCampli: Print the artists that are liked by the most users.
The top 3 artists should be printed, one per line, starting with the most popular'''
  popular = {}
  max = 1
  for user, artists in dic.items():
    #if user[-1] != '$':  #if not private
    for i in artists:
      if i in popular:
        popular[i] += 1
        if popular[i] > max:
          max = popular[i]
      else:
        popular[i] = 1
  if popular == {}:
    print("Sorry, no artists found.")
  else:
    popular = sorted(popular.items(), key=lambda x: x[1])
    for num in range(-1,-4,-1):
        try:
            print(list(popular[num])[0])
        except:
            continue

# how popular is the most popular artist
def howPopular(dic):
  '''Molly DiCampli: Prints the number of likes the most popular artist received.'''
  popular = {}
  max = 1
  for user, artist in dic.items():
    if user[-1] != '$':  #if not private
      for i in artist:
        if i in popular:
          popular[i] += 1
          if popular[i] > max:
            max = popular[i]
        else:
          popular[i] = 1
  if popular == {}:
    print("Sorry, no artists found.")
  else:
    print(max)


# which user likes the most artists
def whichUser(dic):
  '''Molly DiCampli: Prints the full name(s) of the user(s) who
like(s) the most artists.'''
  mostArtists = []
  max = 0
  nameMax = ""
  for user, artists in dic.items():
    if user[-1] != '$':  #if not private
      if len(artists) > max:
        max = len(artists)
        nameMax = user  #only printing one name as instructions allow so
  if max == 0:
    print("Sorry, no user found.")
  else:
    print(nameMax)


def deletePreferences(user, dic):
    ''' Daniel Detore: user is the current users name, dic is the dictionary of users 
    and their preferences. shows the users their artists and allows them to remove one. '''
    j = 0
    for i in dic[user]:
        print(j,": " + i)
        j += 1
    print("Enter a number to remove its associated preference.")
    choice = int(input())
    currentArtists = dic[user]
    currentArtists.pop(choice)
    dic[user] = currentArtists


def showPreferences(user, dict):
  # Extra credit
  """Ria Konar: Prints the artist preferences of a user (user)"""
  for artist in dict[user]:
    print(artist)


startupSurvey()
