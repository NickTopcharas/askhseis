import random

def towervsqueen(whitetower_position,blackqueen_position):
    #Εντοπίζει αν ο πύργος τρώει την βασίλισσα
    player1=0
    for i in range(9):
        if (i,y1) == blackqueen_position:
            player1 = player1 + 1
            #κάθετος έλεγχος
        elif (x1,i) == blackqueen_position:
            player1 = player1 + 1
            #οριζόντιος έλεγχος
    return(player1)  

def officervsqueen(officer_position,blackqueen_position):
    # εντοπιζει αν ο αξιωματικος τρωει τη βασιλισσα με περιπτώσεις
    #1η περίπτωση διαγωνίου από πάνω αριστερά προς τα κάτω δεξιά
    player11=0
    if x1>=y1:
        #έλεγχος διαγωνίου μέχρι την μεσαία (κύρια) διαγώνιο
        k1= x1-y1+1
        #βρίσκει ποια είναι η πρώτη γραμμή της διαγωνίου
        for i in range(0,9-k1):
            if (k1+1,i+1)==(x3,y3):
                player11=player11+1
    #έλεγχος διαγωνίου από την κύρια διαγώνιο και μετά            
    else:
        k2=y1-x1+1
        for i in range(0,9-k2):
            if (i+1,k2+i)==(x2,y2):
                player11=player11+1
    #2η περίπτωση διαγωνίου από αριστερά κάτω προς τα δεξιά πάνω            
    if player11==0:
        if x1+y1<=9:
            l1=x1+y1-1
            for i in range(0,l1):
                if (l1-i,i+1)==(x3,y3):
                    player11=player11+1
        else:
            l2=x1+y1-8
            for i in range(0,9-l2):
                if (8-i)==(x3,y3):
                    player11=player11+1
    return(player11)


def queenvswhitetower(blackqueen_position,whitetower_position):
    #Εντοπίζει αν η βασιλισσα τρωει τον πύργο καθετα η οριζόντια
    player2=0
    player22=0
    if (x3,y3)!=(x1,y1):
        for i in range(9):
            if (i,y3) == whitetower_position:
                 player2 = player2 + 1
            elif (x3,i) == whitetower_position:
                 player2 = player2 + 1
            #εντοπιζει αν η βασιλισσα τρωει τον πυργο διαγωνια
        if x3>=y3:
            k1= x3-y3+1
            for i in range(0,9-k1):
                if (k1+1,i+1)==(x1,y1):
                        player22 = player2 + 1
        else:
            k2=y3-x3+1
            for i in range(0,9-k2):
                if (i+1,k2+i)==(x1,y1):
                 player22=player22+1
        if player22==0:
            if x3+y3<=9:
                 l1=x3+y3-1
                 for i in range(0,l1):
                     if (l1-i,i+1)==(x1,y1):
                         player22=player22+1
            else:
                 l2=x3+y3-8
                 for i in range(0,9-l2):
                     if (8-i)==(x1,y1):
                         player22=player22+1
    else:
        player2=1
        player22=0                
    return(player2+player22)
                        

                    
def queenvsofficer(blackqueen_position,officer_position):
    #Εντοπίζει αν η βασιλισσα τρωει τον αξιωματικο καθετα η οριζόντια
    player2=0
    player22=0
    if (x3,y3)!=(x2,y2):
         for i in range(9):
             if (i,y3) == officer_position:
                 player2 = player2 + 1
             elif (x3,i) == officer_position:
                 player2 = player2 + 1
            #εντοπιζει αν η βασιλισσα τρωει τον αξιωματικο διαγωνια
         if x3>=y3:
             k1= x3-y3+1
             for i in range(0,9-k1):
                 if (k1+1,i+1)==(x2,y2):
                        player22 = player2 + 1
         else:
             k2=y3-x3+1
             for i in range(0,9-k2):
                 if (i+1,k2+i)==(x2,y2):
                     player22=player22+1
         if player22==0:
                if x3+y3<=9:
                     l1=x3+y3-1
                     for i in range(0,l1):
                        if (l1-i,i+1)==(x2,y2):
                            player22=player22+1
         else:
                     l2=x3+y3-8
                     for i in range(0,9-l2):
                        if (8-i)==(x2,y2):
                            player22=player22+1
    else:
        player2=1
        player22=0                
    return(player2+player22)
    


TeamApoints=0
TeamBpoints=0
for i in range(101):
    x1 = random.randrange(1,9)
    y1 = random.randrange(1,9)
    whitetower_position = (x1,y1)

    x2 = random.randrange(1,9)
    y2 = random.randrange(1,9)
    officer_position = (x2,y2)

    x3 = random.randrange(1,9)
    y3 = random.randrange(1,9)
    blackqueen_position = (x3,y3)
    TeamApoints = TeamApoints + towervsqueen(whitetower_position,blackqueen_position) + officervsqueen(officer_position,blackqueen_position)
    TeamBpoints = TeamBpoints + queenvswhitetower(blackqueen_position,whitetower_position) + queenvsofficer(blackqueen_position,officer_position)
print("Player's 1(white) score :")
print(TeamApoints)
print("Player's 2(black) score :")
print(TeamBpoints)


    



