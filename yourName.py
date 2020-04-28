spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3: # When spam == 3; the code goes back up to loop and starts at spam == 4
        continue
    print('Spam is ' + str(spam))