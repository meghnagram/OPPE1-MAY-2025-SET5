piece_map = {'K': 'King', 'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight'}
piece_values = {"Pawn": 1, "Bishop": 2, "Knight": 3, "Rook": 4, "Queen": 5, "King": 6}


def parse_moves(game: str) -> list:
    """Returns a list with alternate white and black moves."""
    
    
    moves = game.split()
    del moves[-1]
    del moves[::3]
    return moves
    

def get_n_moves(game: str) -> int:
    """Returns the total number of moves played in the game."""
    
    return len(parse_moves(game))

def count_piece_moves(moves: list) -> dict:
    """Returns a dictionary with piece names and the number of moves made by that piece.
    
    During castling a move is counted for both king and rook.
    """
    
    
    counts = {p: 0 for p in list(piece_map.values())+["Pawn"]}
    for move in moves:
        if move.startswith('O'):
            counts['King'] += 1
            counts['Rook'] += 1
        else:
            piece = piece_map.get(move[0], 'Pawn')
            counts[piece] += 1
    return counts
    

def most_used_piece(game: str, player: str) -> str:
    """Returns the name of the piece that was moved the most for a specified player."""
    
    
    moves = parse_moves(game)
    player_moves = moves[::2] if player == 'white' else moves[1::2]
    counts = count_piece_moves(player_moves)
    return max(counts, key=lambda x: (counts.get(x), piece_values.get(x)))
    

def remaining_pieces(game: str, player: str) -> int:
    """Returns the remaining pieces for a player."""
    
    
    moves = parse_moves(game)
    player_moves = moves[::2] if player == 'black' else moves[1::2]
    return 16 - sum(1 for move in player_moves if 'x' in move)
    

def n_checks(game: str, player: str) -> int:
    """Returns the number of times a player put the opponent in check."""
    
    
    moves = parse_moves(game)
    player_moves = moves[::2] if player == 'white' else moves[1::2]
    return sum(1 for move in player_moves if move.endswith('+'))
    
# #Another Method:

# piece_map = {'K': 'King', 'Q': 'Queen', 'R': 'Rook', 'B': 'Bishop', 'N': 'Knight'}
# piece_values = {"Pawn": 1, "Bishop": 2, "Knight": 3, "Rook": 4, "Queen": 5, "King": 6}


# def parse_moves(game: str) -> list:
#     """Returns a list with alternate white and black moves."""
#     l=[]
#     m=[]
#     l=game.split()
#     for i in range(len(l)):
#         if i%3==0:
#             continue
#         else:
#             m.append(l[i])
#     m=m[0:-1:]
#     return(m)
    

# def get_n_moves(game: str) -> int:
#     """Returns the total number of moves played in the game."""
#     l=[]
#     m=[]
#     l=game.split()
#     for i in range(len(l)):
#         if i%3==0:
#             continue
#         else:
#             m.append(l[i])
#     m=m[0:-1:]
#     return(len(m))
    

# def count_piece_moves(moves: list) -> dict:
#     """Returns a dictionary with piece names and the number of moves made by that piece.
    
#     During castling a move is counted for both king and rook.
#     """
#     d={}
#     d['Bishop']=0
#     d['King']=0
#     d['Knight']=0
#     d['Pawn']=0
#     d['Queen']=0
#     d['Rook']=0

#     for i in moves:
#         c=0
#         for j in i:
#             if j in ('K','Q', 'R', 'B', 'N'):
#                 c=1
#                 if j in ('K'):
#                     d['King'] +=1
#                 if j in ('Q'):
#                     d['Queen'] +=1
#                 if j in ('R'):
#                     d['Rook'] +=1
#                 if j in ('B'):
#                     d['Bishop'] +=1
#                 if j in ('N'):
#                     d['Knight'] +=1
#         if i=='O-O':
#             d['King'] +=1
#             d['Rook'] +=1
#             c=1 
        
#         if c==0:
#             d['Pawn'] +=1
        
#     return(d)
 

# def most_used_piece(game: str, player: str) -> str:
#     """Returns the name of the piece that was moved the most for a specified player."""
#     l=[]
#     m=[]
#     l=game.split()
#     for i in range(len(l)):
#         if i%3==0:
#             continue
#         else:
#             m.append(l[i])
#     m=m[0:-1:]
#     #w=m[0::2]
#     #b=m[1::2]
#     if player=="white":
#         sublist=m[0::2]
#     if player=="black":
#         sublist=m[1::2]

#     d={}
#     d['Bishop']=0
#     d['King']=0
#     d['Knight']=0
#     d['Pawn']=0
#     d['Queen']=0
#     d['Rook']=0

#     for i in sublist:
#         c=0
#         for j in i:
#             if j in ('K','Q', 'R', 'B', 'N'):
#                 c=1
#                 if j in ('K'):
#                     d['King'] +=1
#                 if j in ('Q'):
#                     d['Queen'] +=1
#                 if j in ('R'):
#                     d['Rook'] +=1
#                 if j in ('B'):
#                     d['Bishop'] +=1
#                 if j in ('N'):
#                     d['Knight'] +=1
#         if i=='O-O':
#             d['King'] +=1
#             d['Rook'] +=1
#             c=1 
        
#         if c==0:
#             d['Pawn'] +=1
        
#     max=0
#     s=[]

#     for key in d:
#         if d[key]>max:
#             max=d[key]
#     for key in d:
#         if d[key] ==max:
#             s.append(key)
        
#     winner=s[0]
#     for i in s:
#         if piece_values[i]>piece_values[winner]:
#             winner=i
#     return(winner)
    

# def remaining_pieces(game: str, player: str) -> int:
#     """Returns the remaining pieces for a player."""
#     l=[]
#     m=[]
#     l=game.split()
#     for i in range(len(l)):
#         if i%3==0:
#             continue
#         else:
#             m.append(l[i])
#     m=m[0:-1:]
#     #w=m[0::2]
#     #b=m[1::2]
#     if player=="white":
#         sublist=m[1::2]
#     if player=="black":
#         sublist=m[0::2]

#     c=0
#     for i in sublist:
#         for j in i:
#             if j=='x':
#                 c +=1
    
#     return(16-c)
    

# def n_checks(game: str, player: str) -> int:
#     """Returns the number of times a player put the opponent in check."""
#     l=[]
#     m=[]
#     l=game.split()
#     for i in range(len(l)):
#         if i%3==0:
#             continue
#         else:
#             m.append(l[i])
#     m=m[0:-1:]
#     #w=m[0::2]
#     #b=m[1::2]
#     if player=="white":
#         sublist=m[0::2]
#     if player=="black":
#         sublist=m[1::2]

#     c=0
#     for i in sublist:
#         for j in i:
#             if j=='+':
#                 c +=1
    
#     return(c)

# Chess Game Analysis
# You are given a record of chess moves as a string in Standard Algebraic Notation (SAN). Implement the following functions to analyze the game:

# parse_moves(game:str) -> list
# Parses the game string to list of alternate black and white moves.
# get_n_moves(game: str) -> int:
# Returns the total number of moves played in the game (one move is considered as each turn).
# count_piece_moves(moves: list) -> dict:
# Returns a dictionary with each piece name ('King', 'Queen', 'Rook', 'Bishop', 'Knight', 'Pawn') as keys and the number of times that piece is moved in the game as values. Castling is counted as a move for both the king and the rook involved.
# most_used_piece(game: str, player: str) -> str:
# Returns the name of the piece that was moved the most for a specified player ("white" or "black"). Break ties with the piece with most value. Piece values are {"Pawn": 1, "Bishop": 2, "Knight": 3, "Rook": 4, "Queen": 5, "King": 6}
# remaining_pieces(game: str, player: str) -> int:
# Returns the remaining number of pieces that a player has on the board. A piece capture is denoted by an 'x' in the moves. White captures black pieces, and vice-versa.
# n_checks(game: str, player: str) -> int:
# Returns the number of times the player has put the opponent in check. A check is denoted by a '+' at the end of the move.
# Note: Assume that the input game string is well-formed and valid according to the rules of chess. The player will always be either "white" or "black".

# Examples

# Given a chess game as a string:

# >>> game = "1. d4 d5 2. c4 Nf6 3. cxd5 Nxd5 4. Nf3 Be6 5. e4 Nb6 6. Nc3 f5 7. Ng5 Qd7 8. Nb5 c6 9. Nxe6 Qxe6 10. Nc7+ Kd8 11. Nxe6+ Ke8 12. Nc7+ Kd8 13. Bf4 N8d7 14. d5 e6 15. dxe6 Bb4+ 16. Ke2 Rc8 17. exd7 Nxd7 18. Ne6+ Ke7 19. Nxg7 Rcg8 20. Bd6+ Bxd6 21. Nxf5+ Ke6 22. Qxd6+ Kf7 23. Qxd7+ Kf8 24. Qe7# 1-0"
# >>> parse_moves(game)
# ['d4', 'd5', 'c4', 'Nf6', 'cxd5', 'Nxd5', 'Nf3', 'Be6', 'e4', 'Nb6', 'Nc3', 'f5', 'Ng5', 'Qd7', 'Nb5', 'c6', 'Nxe6', 'Qxe6', 'Nc7+', 'Kd8', 'Nxe6+', 'Ke8', 'Nc7+', 'Kd8', 'Bf4', 'N8d7', 'd5', 'e6', 'dxe6', 'Bb4+', 'Ke2', 'Rc8', 'exd7', 'Nxd7', 'Ne6+', 'Ke7', 'Nxg7', 'Rcg8', 'Bd6+', 'Bxd6', 'Nxf5+', 'Ke6', 'Qxd6+', 'Kf7', 'Qxd7+', 'Kf8', 'Qe7#']
# >>> get_n_moves(game)
# 47
# >>> count_piece_moves(game)
# {'Pawn': 6, 'Knight': 3, 'Bishop': 2, 'Rook': 1, 'King': 1, 'Queen': 0}
# >>> most_used_piece(game, "black")
# "Knight"
# >>> remaining_pieces(game, "white")
# >>> n_checks(game, "white")
# Chess Notation Details
# Pieces are represented by their initials:
# K - King
# Q - Queen
# R - Rook
# B - Bishop
# N - Knight
# Pawn (no initial, just represented by move)
# Castling is represented with:
# O-O (kingside castling)
# O-O-O (queenside castling)
# A move in which a player captures a piece of the opponent is denoted with a x in the move.
# A move in which a player puts the opponent in check is denoted with a + in the end of the move.
# A move in which a player check mates is denoted by # at the end of the move.
# The end of game string will have the result of the game as "1-0", "0-1" or "1/2-1/2".



