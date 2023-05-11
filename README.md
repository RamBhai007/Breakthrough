# Breakthrough
The goal of this assignment is to implement an agent to play a simple 2-player zerosum game called Breakthrough
Implement agents to play the Breakthrough game, one using minimax search and 
one using alpha-beta search as well as two evaluation functions - one which is more 
Offensive. while the other which is more defensive. The evaluation functions are used to 
return a value for a position when the depth limit of the search is reached.
Minimax search is a decision-making algorithm that involves analysing the entire 
game tree to determine the best move to make, assuming that both players will play 
optimally. It is called minimax because it alternates between minimizing the score of the 
opponent and maximizing its own score. In a search tree of depth 3, the algorithm would 
evaluate all possible moves three levels deep and select the move with the highest score.
Alpha-beta search is an optimization of the minimax algorithm that reduces the 
number of nodes evaluated by pruning branches that are guaranteed to be unimportant. This 
algorithm maintains two values, alpha and beta, representing the minimum score that the 
maximizing player is assured of and the maximum score that the minimizing player is assured 
of, respectively. The algorithm prunes branches that are guaranteed to not lead to a better 
score than the current best

MiniMax Algorithm
The minimax algorithm is a decision-making algorithm used in game theory to find the 
best move to make in a game with two players, assuming that both players play optimally. The 
algorithm works by analysing the entire game tree and evaluating the scores of all possible 
moves.
The algorithm starts at the top of the game tree, representing the current state of the 
game, and recursively evaluates each node in the tree. Each node represents a possible move 
that can be made by the current player.
The algorithm alternates between two players: the maximizing player and the 
minimizing player. The maximizing player tries to maximize its score, while the minimizing 
player tries to minimize the score of the maximizing player.
At each node, the algorithm evaluates all possible moves that can be made by the current 
player and determines the score of each possible move. The score of a move is determined by 
evaluating the resulting game state after making the move. The score of a game state is a 
numerical value that represents how good the game state is for the maximizing player. For 
example, in a game of Tic Tac Toe, the score might be +1 for a winning game state, -1 for a 
losing game state, and 0 for a draw game state.
Once all possible moves have been evaluated at a node, the algorithm selects the move 
with the highest score if it is the turn of the maximizing player, or the move with the lowest 
score if it is the turn of the minimizing player. This process continues until the algorithm 
reaches a leaf node, representing the end of the game or a predetermined search depth.
At the leaf node, the algorithm returns the score of the game state. This score is 
propagated back up the tree to the parent node, where the algorithm selects the move with the 
highest score if it is the turn of the maximizing player, or the move with the lowest score if it 
is the turn of the minimizing player.
The minimax algorithm assumes that both players play optimally, so it evaluates all 
possible moves and selects the best move for the current player. However, in practice, it is often 
not feasible to evaluate all possible moves, so more efficient algorithms, such as alpha-beta 
pruning, are used to optimize the search process.
Alpha-Beta Algorithm 
The alpha-beta algorithm is a variation of the minimax algorithm, used to determine the 
best move for a player in a game with two players. It works by exploring the game tree and 
evaluating the scores of all possible moves, but it reduces the number of nodes evaluated by 
pruning branches of the game tree that are unlikely to lead to a better decision.
The algorithm uses two values, alpha and beta, to keep track of the maximum score
achievable by the maximizing player and the minimum score achievable by the minimizing 
player, respectively. It starts at the top of the game tree, representing the current state of the 
game, and evaluates each node in the tree recursively.
At each node, the algorithm evaluates all possible moves that can be made by the current 
player and determines the score of each possible move. The algorithm alternates between two 
players, maximizing and minimizing their scores, and updates the current alpha and beta values 
accordingly.
If the current node is a maximizing node, the algorithm checks if the score of the current 
node is greater than or equal to the current beta value. If it is, the algorithm prunes the branch 
and returns the current beta value, because the minimizing player will not choose this branch, 
since it leads to a worse outcome than a previously evaluated branch. Otherwise, the algorithm 
updates the alpha value to be the maximum of the current score and the current alpha value.
If the current node is a minimizing node, the algorithm checks if the score of the current 
node is less than or equal to the current alpha value. If it is, the algorithm prunes the branch 
and returns the current alpha value, because the maximizing player will not choose this branch, 
since it leads to a worse outcome than a previously evaluated branch. Otherwise, the algorithm 
updates the beta value to be the minimum of the current score and the current beta value.
Once all possible moves have been evaluated at a node, the algorithm selects the move 
with the highest score if it is the turn of the maximizing player, or the move with the lowest 
score if it is the turn of the minimizing player. This process continues until the algorithm 
reaches a leaf node, representing the end of the game or a predetermined search depth.
At the leaf node, the algorithm returns the score of the game state. This score is 
propagated back up the tree to the parent node, where the algorithm updates the alpha and beta 
values and selects the move with the highest score if it is the turn of the maximizing player, or 
the move with the lowest score if it is the turn of the minimizing player.
Overall, the alpha-beta algorithm is an efficient way to search the game tree and find 
the best move in a game with two players, by pruning branches of the game tree that are 
unlikely to lead to a better decision.






SELECT MATCHUP
 (1) Minimax (Offensive Heuristic 1) vs Alpha-beta (Offensive Heuristic 1)
  ![Screenshot 2023-04-23 165434](https://github.com/RamBhai007/Breakthrough/assets/101466286/60a8f979-33bf-4ee4-bcc7-acd9289dbbdc)

 (2) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1)
 ![Screenshot 2023-04-23 165517](https://github.com/RamBhai007/Breakthrough/assets/101466286/bc05b2a5-bb8e-4d12-9b51-5e58e1498d75)

 (3) Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1)
 ![Screenshot 2023-04-23 165542](https://github.com/RamBhai007/Breakthrough/assets/101466286/7c499dd3-9190-4bb6-92d6-daf78f60ed1b)

 (4) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Offensive Heuristic 1)
 ![Screenshot 2023-04-23 165542](https://github.com/RamBhai007/Breakthrough/assets/101466286/4ed477db-36be-4103-8600-7c784a0ae433)

 (5) Alpha-beta (Defensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 1)
 ![Screenshot 2023-04-23 165634](https://github.com/RamBhai007/Breakthrough/assets/101466286/d7280f40-f7fd-4f4c-a8c8-46c79d70479f)

 (6) Alpha-beta (Offensive Heuristic 2) vs Alpha-beta (Defensive Heuristic 2)
 ![Screenshot 2023-04-23 165910](https://github.com/RamBhai007/Breakthrough/assets/101466286/554332a4-3cc6-4b60-8b2d-b149d34f3c97)
 
 
 (7) Random AI vs Random AI
 ![Screenshot 2023-04-23 165941](https://github.com/RamBhai007/Breakthrough/assets/101466286/3d63222c-1ce0-49b1-98dd-874092ccf90b)

 
 
 
 ##Minimax (Offensive Heuristic 1) vs Alpha-beta (Offensive Heuristic 1)
 ![Screenshot 2023-04-23 165434](https://github.com/RamBhai007/Breakthrough/assets/101466286/60a8f979-33bf-4ee4-bcc7-acd9289dbbdc)

 
