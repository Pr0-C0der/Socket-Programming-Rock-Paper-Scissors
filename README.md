# Socket-Programming-Rock-Paper-Scissors
This repository contains a simple implementation of the classic game "Rock-Paper-Scissors" using socket programming in Python. The game allows two players to connect to a server and play against each other by making their choices of rock, paper, or scissors.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)

## Introduction
Socket programming is a way of communication between two computers using sockets, which are the endpoints for sending and receiving data across a network. This repository demonstrates how socket programming can be used to create a simple multiplayer game like Rock-Paper-Scissors.

The game consists of a server that handles connections from two players and manages the game logic. Each player connects to the server and sends their choice of rock, paper, or scissors. The server then determines the winner based on the choices and sends the result to both players. The players can continue playing multiple rounds until they decide to quit.

## Requirements

To run the game, you need to have the following requirements installed:

- Python 3.x

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/Pr0-C0der/Socket-Programming-Rock-Paper-Scissors.git
   
2. Change into the project directory:
   ```bash
   cd Socket-Programming-Rock-Paper-Scissors
3. Start the server by running the server.py
   ``` bash
   python server.py
4. The players need to run the client.py for both players:
   ```bash
   python client.py
   
5. Both Players should click anywhere on the screen to start the game
6. Enjoy the Game 

## Acknowledgements
Thank you Tech With Tim for awesome python tutorials. [Check his channel here](https://www.youtube.com/@TechWithTim)
