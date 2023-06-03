import socket
from _thread import *
import pickle
from game import Game

# port represents the TCP port number to accept connections on from clients
server = "192.168.1.7"
port = 5559

#AF_INET refers to the address family the socket can communicate with.
# SOCK_STREAM means connection-oriented TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#It might happen that the port is not free for some reason, hence we could get error while binding
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

#s.listen() basically listens for connections. We pass 2 as argument as we only want atmost 2 connections 
s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}  #storing games
idCount = 0 #storing the count


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            #Checking if the gameId exists in games
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    #When the conncection is lost we delete the particular game as there are no players
    #We decreace the count and close the connection
    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    #Accepting the connection from client and storing the information
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0
    gameId = (idCount - 1)//2  #We divide by 2 since two players play the game
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 1


    start_new_thread(threaded_client, (conn, p, gameId))