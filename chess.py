import pygame,sys
class piece(object):
	"""arg:type(str),color(1,-1),pos(x,y),moves[(.,.)]"""
	global board
	moves=[]
	def __init__(self,type,color,pos):
		self.type=type
		self.color=color
		self.pos=pos
	def gen_moves(self):
		if self.type=='K':
			self.moves=king_moves(self.color,self.pos)

		if self.type=='Q':
			self.moves=queen_moves(self.color,self.pos)

		if self.type=='b':
			self.moves=bishop_moves(self.color,self.pos)

		if self.type=='kn':
			self.moves=knight_moves(self.color,self.pos)

		if self.type=='r':
			self.moves=rook_moves(self.color,self.pos)

		if self.type=='p':
			self.moves=pawn_moves(self.color,self.pos)
		
	def move(self,pos):
		board[self.pos]=0
		self.pos=pos
		board[self.pos]=self.color
def king_moves(color,pos):
	global board,w_dzone,b_dzone
	moves=[]
	x=pos[0]
	y=pos[1]
	i=x-1
	while i<x+2:
		j=y-1
		while j<y+2:
			if i>=0 and i<8 and j>=0 and j<8:
				if i!=x or j!=y:
					if board[(i,j)]!=color:
						moves.append((i,j))
			j+=1
		i+=1
	if color==1:
		moves=list(set(moves)-set(w_dzone))
	if color==-1:
		moves=list(set(moves)-set(b_dzone))
	return  moves
def queen_moves(color,pos):
	global board
	moves=[]
	moves=bishop_moves(color,pos)+rook_moves(color,pos)
	return  moves
def bishop_moves(color,pos,botleft=1,topleft=1,botright=1,topright=1):
	global board
	moves=[]
	x=pos[0]
	y=pos[1]
	if botleft==1:
		i=1
		while i<8-x and i<8-y:				#bottom of left diagonal
			if board[(x+i,y+i)]==color:
				break
			elif board[(x+i,y+i)]==color*-1:
				moves.append((x+i,y+i))
				break
			else:
				moves.append((x+i,y+i))
			i+=1

	if topleft==1:
		i=1
		while i<=x and i<=y:				#top of left diagonal
			if board[(x-i,y-i)]==color:
				break
			elif board[(x-i,y-i)]==color*-1:
				moves.append((x-i,y-i))
				break
			else:
				moves.append((x-i,y-i))
			i+=1

	if botright==1:
		i=1
		while i<8-x and i<=y:				#top of right diagonal
			if board[(x+i,y-i)]==color:
				break
			elif board[(x+i,y-i)]==color*-1:
				moves.append((x+i,y-i))
				break
			else:
				moves.append((x+i,y-i))
			i+=1

	if topright==1:
		i=1
		while i<=x and i<8-y:				#bottom right diagonal
			if board[(x-i,y+i)]==color:
				break
			elif board[(x-i,y+i)]==color*-1:
				moves.append((x-i,y+i))
				break
			else:
				moves.append((x-i,y+i))
			i+=1

	return  moves
def knight_moves(color,pos):
	global board
	moves=[]
	x=pos[0]
	y=pos[1]

	if x+1<8 and y-2>=0:
		if board[(x+1,y-2)]!=color:
			moves.append((x+1,y-2))
	if x-1>=0 and y-2>=0:
		if board[(x-1,y-2)]!=color:
			moves.append((x-1,y-2))
	if x+1<8 and y+2<8:
		if board[(x+1,y+2)]!=color:
			moves.append((x+1,y+2))
	if x-1>=0 and y+2<8:
		if board[(x-1,y+2)]!=color:
			moves.append((x-1,y+2))
	if x+2<8 and y-1>=0:
		if board[(x+2,y-1)]!=color:
			moves.append((x+2,y-1))
	if x-2>=0 and y-1>=0:
		if board[(x-2,y-1)]!=color:
			moves.append((x-2,y-1))
	if x+2<8 and y+1<8:
		if board[(x+2,y+1)]!=color:
			moves.append((x+2,y+1))
	if x-2>=0 and y+1<8:
		if board[(x-2,y+1)]!=color:
			moves.append((x-2,y+1))
	
	return  moves
def rook_moves(color,pos,left=1,right=1,up=1,down=1):
	global board
	moves=[]
	x=pos[0]
	y=pos[1]
	if right==1:
		i=1
		while i<8-x:					#right
			if board[(x+i,y)]==color:
				break
			elif board[(x+i,y)]==color*-1:
				moves.append((x+i,y))
				break
			else:
				moves.append((x+i,y))
			i+=1
	if left==1:
		i=1
		while i<=x:						#left
			if board[(x-i,y)]==color:
				break
			elif board[(x-i,y)]==color*-1:
				moves.append((x-i,y))
				break
			else:
				moves.append((x-i,y))
			i+=1
	if down==1:
		i=1
		while i<8-y:					#down
			if board[(x,y+i)]==color:
				break
			elif board[(x,y+i)]==color*-1:
				moves.append((x,y+i))
				break
			else:
				moves.append((x,y+i))
			i+=1
	if up==1:
		i=1
		while i<=y:						#up
			if board[(x,y-i)]==color:
				break
			elif board[(x,y-i)]==color*-1:
				moves.append((x,y-i))
				break
			else:
				moves.append((x,y-i))
			i+=1
	return  moves
def pawn_moves(color,pos):
	global board
	moves=[]
	x=pos[0]
	y=pos[1]
	if color==1:
		if y==6:
			if board[(x,5)]==0:
				moves.append((x,5))
				if board[(x,4)]==0:
					moves.append((x,4))
		else:
			if board[(x,y-1)]==0:
				moves.append((x,y-1))
		if x!=0:
			if board[(x-1,y-1)]==-1:
				moves.append((x-1,y-1))
		if x!=7:
			if board[(x+1,y-1)]==-1:
				moves.append((x+1,y-1))
	if color==-1:
		if y==1:
			if board[(x,2)]==0:
				moves.append((x,2))
				if board[(x,3)]==0:
					moves.append((x,3))
		else:
			if board[(x,y+1)]==0:
				moves.append((x,y+1))
		if x!=0:
			if board[(x-1,y+1)]==1:
				moves.append((x-1,y+1))
		if x!=7:
			if board[(x+1,y+1)]==1:
				moves.append((x+1,y+1))
	return moves

def initWhite():
	white=[]
	white.append(piece('K',1,(4,7)))
	white.append(piece('Q',1,(3,7)))
	white.append(piece('r',1,(0,7)))
	white.append(piece('kn',1,(1,7)))
	white.append(piece('b',1,(2,7)))	
	white.append(piece('b',1,(5,7)))
	white.append(piece('kn',1,(6,7)))
	white.append(piece('r',1,(7,7)))
	
	for i in range(8):
		white.append(piece('p',1,(i,6)))

	return white


def initBlack():
	black=[]
	black.append(piece('K',-1,(4,0)))
	black.append(piece('Q',-1,(3,0)))
	black.append(piece('r',-1,(0,0)))
	black.append(piece('kn',-1,(1,0)))
	black.append(piece('b',-1,(2,0)))
	black.append(piece('b',-1,(5,0)))
	black.append(piece('kn',-1,(6,0)))
	black.append(piece('r',-1,(7,0)))
	
	for i in range(8):
		black.append(piece('p',-1,(i,1)))

	return black
def bishop_crtd_moves(color,white,black,pos):
	global board,w_dzone,b_dzone
	leftdiag=1
	rightdiag=1
	config=0
	if color==1:
		if pos[0]<7 and pos[1]<7:
			if board[(pos[0]+1,pos[1]+1)]!=1:
				config=board[(pos[0]+1,pos[1]+1)]
				board[(pos[0]+1,pos[1]+1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					leftdiag=0
				board[(pos[0]+1,pos[1]+1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		if pos[0]>0 and pos[1]>0:
			if board[(pos[0]-1,pos[1]-1)]!=1:
				config=board[(pos[0]-1,pos[1]-1)]
				board[(pos[0]-1,pos[1]-1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					leftdiag=0
				board[(pos[0]-1,pos[1]-1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		if pos[0]>0 and pos[1]<7:
			if board[(pos[0]-1,pos[1]+1)]!=1:
				config=board[(pos[0]-1,pos[1]+1)]
				board[(pos[0]-1,pos[1]+1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					rightdiag=0
				board[(pos[0]-1,pos[1]+1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		if pos[0]<7 and pos[1]>0:
			if board[(pos[0]+1,pos[1]-1)]!=1:
				config=board[(pos[0]+1,pos[1]-1)]
				board[(pos[0]+1,pos[1]-1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					rightdiag=0
				board[(pos[0]+1,pos[1]-1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		return bishop_moves(1,pos,leftdiag,leftdiag,rightdiag,rightdiag)
	if color==-1:
		if pos[0]<7 and pos[1]<7:
			if board[(pos[0]+1,pos[1]+1)]!=-1:
				config=board[(pos[0]+1,pos[1]+1)]
				board[(pos[0]+1,pos[1]+1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					leftdiag=0
				board[(pos[0]+1,pos[1]+1)]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[0]>0 and pos[1]>0:
			if board[(pos[0]-1,pos[1]-1)]!=-1:
				config=board[(pos[0]-1,pos[1]-1)]
				board[(pos[0]-1,pos[1]-1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					leftdiag=0
				board[(pos[0]-1,pos[1]-1)]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[0]>0 and pos[1]<7:
			if board[(pos[0]-1,pos[1]+1)]!=-1:
				config=board[(pos[0]-1,pos[1]+1)]
				board[(pos[0]-1,pos[1]+1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					rightdiag=0
				board[(pos[0]-1,pos[1]+1)]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[0]<7 and pos[1]>0:
			if board[(pos[0]+1,pos[1]-1)]!=-1:
				config=board[(pos[0]+1,pos[1]-1)]
				board[(pos[0]+1,pos[1]-1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					rightdiag=0
				board[(pos[0]+1,pos[1]-1)]=config
				uupdateMoves_w(white)
				updatedangerzone_b(white)
		return bishop_moves(-1,pos,leftdiag,leftdiag,rightdiag,rightdiag)

def rook_crtd_moves(color,white,black,pos):
	global board,w_dzone,b_dzone
	hori=1
	vert=1
	config=0
	if color==1:
		if pos[0]<7:
			if board[(pos[0]+1,pos[1])]!=1:
				config=board[(pos[0]+1,pos[1])]
				board[(pos[0]+1,pos[1])]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					hori=0
				board[(pos[0]+1,pos[1])]=config
				updateMoves_b(black)
				updatedangerzone_w(black)

		if pos[0]>0:
			if board[(pos[0]-1,pos[1])]!=1:
				config=board[(pos[0]-1,pos[1])]
				board[(pos[0]-1,pos[1])]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					hori=0
				board[(pos[0]-1,pos[1])]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		if pos[1]<7:
			if board[(pos[0],pos[1]+1)]!=1:
				config=board[(pos[0],pos[1]+1)]
				board[(pos[0],pos[1]+1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					vert=0
				board[(pos[0],pos[1]+1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		if pos[1]>0:
			if board[(pos[0],pos[1]-1)]!=1:
				config=board[(pos[0],pos[1]-1)]
				board[(pos[0],pos[1]-1)]=1
				updateMoves_b(black)
				updatedangerzone_w(black)
				if white[0].pos in w_dzone:
					vert=0
				board[(pos[0],pos[1]-1)]=config
				updateMoves_b(black)
				updatedangerzone_w(black)
		return rook_moves(1,pos,hori,hori,vert,vert)


	if color==-1:
		if pos[0]<7:
			if board[(pos[0]+1,pos[1])]!=-1:
				config=board[(pos[0]+1,pos[1])]
				board[(pos[0]+1,pos[1])]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					hori=0
				board[(pos[0]+1,pos[1])]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[0]>0:
			if board[(pos[0]-1,pos[1])]!=-1:
				config=board[(pos[0]-1,pos[1])]
				board[(pos[0]-1,pos[1])]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					hori=0
				board[(pos[0]-1,pos[1])]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[1]<7:
			if board[(pos[0],pos[1]+1)]!=-1:
				config=board[(pos[0],pos[1]+1)]
				board[(pos[0],pos[1]+1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					vert=0
				board[(pos[0],pos[1]+1)]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		if pos[1]>0:
			if board[(pos[0],pos[1]-1)]!=-1:
				config=board[(pos[0],pos[1]-1)]
				board[(pos[0],pos[1]-1)]=-1
				updateMoves_w(white)
				updatedangerzone_b(white)
				if black[0].pos in b_dzone:
					vert=0
				board[(pos[0],pos[1]-1)]=config
				updateMoves_w(white)
				updatedangerzone_b(white)
		return rook_moves(-1,pos,hori,hori,vert,vert)
def correct_Whitemoves(white,black,check=0):

	global board,w_dzone,pinned_coins_w,white_castle
	if check==0:
		for coin in white:
			board[coin.pos]=0
			updateMoves_b(black)
			updatedangerzone_w(black)
			if white[0].pos in w_dzone:
				if coin.type=='kn':
					coin.moves=[]
				if coin.type=='r':
					coin.moves=rook_crtd_moves(1,white,black,coin.pos)
				if coin.type=='b':
					coin.moves=bishop_crtd_moves(1,white,black,coin.pos)
				if coin.type=='Q':
					coin.moves=rook_crtd_moves(1,white,black,coin.pos)
					if coin.moves==[]:
						coin.moves=bishop_crtd_moves(1,white,black,coin.pos)
				if coin.type=='p':
					if board[(coin.pos[0],coin.pos[1]-1)]==0:
						board[(coin.pos[0],coin.pos[1]-1)]=1
						updateMoves_b(black)
						updatedangerzone_w(black)
						board[(coin.pos[0],coin.pos[1]-1)]=0
						if white[0].pos in w_dzone:
							coin.moves=[]
						if coin.pos[0]>0:
							if board[(coin.pos[0]-1,coin.pos[1]-1)]==-1:
								board[(coin.pos[0]-1,coin.pos[1]-1)]=1
								for j in range(len(black)):
									if black[j].type=='b' or black[j].type=='Q':
										if black[j].pos==(coin.pos[0]-1,coin.pos[1]-1):
											opp_coin=black[j]
								updateMoves_b(black)
								updatedangerzone_w(black)
								if white[0].pos not in set(w_dzone)-set(opp_coin.moves):
									coin.moves.append((coin.pos[0]-1,coin.pos[1]-1))
								board[(coin.pos[0]-1,coin.pos[1]-1)]=-1
								updateMoves_b(black)
								updatedangerzone_w(black)
						if coin.pos[0]<7:
							if board[(coin.pos[0]+1,coin.pos[1]-1)]==-1:
								board[(coin.pos[0]+1,coin.pos[1]-1)]=1
								for j in range(len(black)):
									if black[j].type=='b' or black[j].type=='Q':
										if black[j].pos==(coin.pos[0]+1,coin.pos[1]-1):
											opp_coin=black[j]
								updateMoves_b(black)
								updatedangerzone_w(black)
								if white[0].pos not in set(w_dzone)-set(opp_coin.moves):
									coin.moves.append((coin.pos[0]+1,coin.pos[1]-1))
								board[(coin.pos[0]+1,coin.pos[1]-1)]=-1
								updateMoves_b(black)
								updatedangerzone_w(black)
				pinned_coins_w.append(coin)
			board[coin.pos]=1
			updateMoves_b(black)
			updatedangerzone_w(black)
		if white_castle[0]==1:
			if board[(1,7)]==0 and board[(2,7)]==0 and board[(3,7)]==0:
				if ((2,7) not in w_dzone) and ((3,7) not in w_dzone):
					white[0].moves.append((2,7))
		if white_castle[1]==1:
			if board[(5,7)]==0 and board[(6,7)]==0:
				if ((5,7) not in w_dzone) and ((6,7) not in w_dzone):
					white[0].moves.append((6,7))
	else:
		for k in range(1,len(white)):
			if white[k] in pinned_coins_w:
				white[k].moves=[]

	for pos in white[0].moves:
		if board[pos]==-1:
			for coin in black:
				if coin.type=='b' or coin.type=='Q':
					if coin.pos in bishop_moves(1,pos):
						white[0].moves.remove(pos)
						break
				if coin.type=='r' or coin.type=='Q':
					if coin.pos in rook_moves(1,pos):
						white[0].moves.remove(pos)
						break
				if coin.type=='kn':
					if coin.pos in knight_moves(1,pos):
						white[0].moves.remove(pos)
						break
				if coin.type=='p':
					if coin.pos==(pos[0]-1,pos[1]-1) or coin.pos==(pos[0]+1,pos[1]-1):
						white[0].moves.remove(pos)
						break
def correct_Blackmoves(black,white,check=0):

	global board,b_dzone,pinned_coins_b
	if check==0:
		for coin in black:
			board[coin.pos]=0
			updateMoves_w(white)
			updatedangerzone_b(white)
			if black[0].pos in b_dzone:
				if coin.type=='kn':
					coin.moves=[]
				if coin.type=='r':
					coin.moves=rook_crtd_moves(-1,white,black,coin.pos)
				if coin.type=='b':
					coin.moves=bishop_crtd_moves(-1,white,black,coin.pos)
				if coin.type=='Q':
					coin.moves=rook_crtd_moves(-1,white,black,coin.pos)
					if coin.moves==[]:
						coin.moves=bishop_crtd_moves(-1,white,black,coin.pos)
				if coin.type=='p':
					if board[(coin.pos[0],coin.pos[1]+1)]==0:
						board[(coin.pos[0],coin.pos[1]+1)]=1
						updateMoves_w(white)
						updatedangerzone_b(white)
						if black[0].pos in b_dzone:
							coin.moves=[]
						board[(coin.pos[0],coin.pos[1]+1)]=0
						if coin.pos[0]>0:
							if board[(coin.pos[0]-1,coin.pos[1]+1)]==1:
								board[(coin.pos[0]-1,coin.pos[1]+1)]=-1
								for j in range(len(white)):
									if white[j].type=='b' or white[j].type=='Q':
										if white[j].pos==(coin.pos[0]-1,coin.pos[1]+1):
											opp_coin=white[j]
								updateMoves_w(white)
								updatedangerzone_b(white)
								if black[0].pos not in set(b_dzone)-set(opp_coin.moves):
									coin.moves.append((coin.pos[0]-1,coin.pos[1]+1))
								board[(coin.pos[0]-1,coin.pos[1]+1)]=1
						if coin.pos[0]<7:
							if board[(coin.pos[0]+1,coin.pos[1]+1)]==1:
								board[(coin.pos[0]+1,coin.pos[1]+1)]=-1
								for j in range(len(white)):
									if white[j].type=='b' or white[j].type=='Q':
										if white[j].pos==(coin.pos[0]+1,coin.pos[1]+1):
											opp_coin=white[j]
								updateMoves_w(white)
								updatedangerzone_b(white)
								if black[0].pos not in set(b_dzone)-set(opp_coin.moves):
									coin.moves.append((coin.pos[0]+1,coin.pos[1]+1))
								board[(coin.pos[0]+1,coin.pos[1]+1)]=1
				pinned_coins_b.append(coin)
			board[coin.pos]=-1
			updateMoves_w(white)
			updatedangerzone_b(white)
		if black_castle[0]==1:
			if board[(1,0)]==0 and board[(2,0)]==0 and board[(3,0)]==0:
				if ((2,0) not in b_dzone) and ((3,0) not in b_dzone):
					black[0].moves.append((2,0))
		if black_castle[1]==1:
			if board[(5,0)]==0 and board[(6,0)]==0:
				if ((5,0) not in b_dzone) and ((6,0) not in b_dzone):
					black[0].moves.append((6,0))
	else:
		for k in range(1,len(black)):
			if black[k] in pinned_coins_b:
				black[k].moves=[]
	for pos in black[0].moves:
			if board[pos]==1:
				for coin in white:
					if coin.type=='b' or coin.type=='Q':
						if coin.pos in bishop_moves(-1,pos):
							black[0].moves.remove(pos)
							break
					if coin.type=='r' or coin.type=='Q':
						if coin.pos in rook_moves(-1,pos):
							black[0].moves.remove(pos)
							break
					if coin.type=='kn':
						if coin.pos in knight_moves(-1,pos):
							black[0].moves.remove(pos)
							break
					if coin.type=='p':
						if coin.pos==(pos[0]-1,pos[1]+1) or coin.pos==(pos[0]+1,pos[1]+1):
							black[0].moves.remove(pos)
							break
def check_path(color,white,black):

	path_b=[]
	path_r=[]
	path_k=[]
	if color==1:
		check_path=bishop_moves(1,white[0].pos,1,0,0,0)
		for coin in black:
			if coin.pos in check_path:
				if coin.type=='b' or coin.type=='Q':
					path_b=check_path
					break
		if path_b==[]:
			check_path=bishop_moves(1,white[0].pos,0,1,0,0)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='b' or coin.type=='Q':
						path_b=check_path
						break
		if path_b==[]:
			check_path=bishop_moves(1,white[0].pos,0,0,1,0)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='b' or coin.type=='Q':
						path_b=check_path
						break
		if path_b==[]:
			check_path=bishop_moves(1,white[0].pos,0,0,0,1)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='b' or coin.type=='Q':
						path_b=check_path
						break
		check_path=rook_moves(1,white[0].pos,1,0,0,0)
		for coin in black:
			if coin.pos in check_path:
				if coin.type=='r' or coin.type=='Q':
					path_r=check_path
					break
		if path_r==[]:
			check_path=rook_moves(1,white[0].pos,0,1,0,0)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='r' or coin.type=='Q':
						path_r=check_path
						break
		if path_r==[]:
			check_path=rook_moves(1,white[0].pos,0,0,1,0)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='r' or coin.type=='Q':
						path_r=check_path
						break
		if path_r==[]:
			check_path=rook_moves(1,white[0].pos,0,0,0,1)
			for coin in black:
				if coin.pos in check_path:
					if coin.type=='r' or coin.type=='Q':
						path_r =check_path
						break
		check_path=knight_moves(1,white[0].pos)
		for coin in black:
			if coin.pos in check_path:
				if coin.type=='kn':
					path_k=check_path
					break

	if color==-1:
			check_path=bishop_moves(-1,black[0].pos,1,0,0,0)
			for coin in white:
				if coin.pos in check_path:
					if coin.type=='b' or coin.type=='Q':
						path_b=check_path
						break
			if path_b==[]:
				check_path=bishop_moves(-1,black[0].pos,0,1,0,0)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='b' or coin.type=='Q':
							path_b=check_path
							break
			if path_b==[]:
				check_path=bishop_moves(-1,black[0].pos,0,0,1,0)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='b' or coin.type=='Q':
							path_b=check_path
							break
			if path_b==[]:
				check_path=bishop_moves(-1,black[0].pos,0,0,0,1)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='b' or coin.type=='Q':
							path_b=check_path
							break
			check_path=rook_moves(-1,black[0].pos,1,0,0,0)
			for coin in white:
				if coin.pos in check_path:
					if coin.type=='r' or coin.type=='Q':
						path_r=check_path
						break
			if path_r==[]:
				check_path=rook_moves(-1,black[0].pos,0,1,0,0)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='r' or coin.type=='Q':
							path_r=check_path
							break
			if path_r==[]:
				check_path=rook_moves(-1,black[0].pos,0,0,1,0)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='r' or coin.type=='Q':
							path_r=check_path
							break
			if path_r==[]:
				check_path=rook_moves(-1,black[0].pos,0,0,0,1)
				for coin in white:
					if coin.pos in check_path:
						if coin.type=='r' or coin.type=='Q':
							path_r =check_path
							break
			check_path=knight_moves(-1,black[0].pos)
			for coin in white:
				if coin.pos in check_path:
					if coin.type=='kn':
						path_k=check_path
						break
	return path_b,path_r,path_k
def checkmoves(color,white,black):
	global w_dzone,b_dzone
	path=[]
	if color==1:
		path_b,path_r,path_k=check_path(1,white,black)
		if (path_b!=[] and path_r!=[]) or (path_k!=[] and path_r!=[]) or (path_b!=[] and path_k!=[]):
			for coin in white:
				if coin.type!='K':
					coin.moves=[]
			if path_k==[]:
				x=white[0].pos[0]
				y=white[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in white[0].moves:
						white[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in white[0].moves:
						white[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in white[0].moves:
						white[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in white[0].moves:
						white[0].moves.remove((x-1,y+1))
				if (x+1,y)==path_r[0]:
					if (x-1,y) in white[0].moves:
						white[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in white[0].moves:
						white[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in white[0].moves:
						white[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in white[0].moves:
						white[0].moves.remove((x,y+1))
			elif path_b==[]:
				x=white[0].pos[0]
				y=white[0].pos[1]
				if (x+1,y)==path_r[0]:
					if (x-1,y) in white[0].moves:
						white[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in white[0].moves:
						white[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in white[0].moves:
						white[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in white[0].moves:
						white[0].moves.remove((x,y+1))
			else:
				x=white[0].pos[0]
				y=white[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in white[0].moves:
						white[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in white[0].moves:
						white[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in white[0].moves:
						white[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in white[0].moves:
						white[0].moves.remove((x-1,y+1))
					white[0].moves.remove((x-1,y+1))
		else:
			if path_k!=[]:
				path=path_k
			elif path_b!=[]:
				x=white[0].pos[0]
				y=white[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in white[0].moves:
						white[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in white[0].moves:
						white[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in white[0].moves:
						white[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in white[0].moves:
						white[0].moves.remove((x-1,y+1))
				path=path_b
			elif path_r!=[]:
				x=white[0].pos[0]
				y=white[0].pos[1]
				if (x+1,y)==path_r[0]:
					if (x-1,y) in white[0].moves:
						white[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in white[0].moves:
						white[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in white[0].moves:
						white[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in white[0].moves:
						white[0].moves.remove((x,y+1))
				path=path_r
			for coin in white:
				if coin.type!='K':	
					moves=coin.moves
					coin.moves=[]
					for pos in moves:
						if pos in path:
							coin.moves.append(pos)
	if color==-1:
		path_b,path_r,path_k=check_path(-1,white,black)
		if (path_b!=[] and path_r!=[]) or (path_k!=[] and path_r!=[]) or (path_b!=[] and path_k!=[]):
			for coin in black:
				if coin.type!='K':
					coin.moves=[]
			if path_k==[]:
				x=black[0].pos[0]
				y=black[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in black[0].moves:
						black[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in black[0].moves:
						black[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in black[0].moves:
						black[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in black[0].moves:
						black[0].moves.remove((x-1,y+1))
				if (x+1,y)==path_r[0]:
					if (x-1,y) in black[0].moves:
						black[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in black[0].moves:
						black[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in black[0].moves:
						black[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in black[0].moves:
						black[0].moves.remove((x,y+1))
			elif path_b==[]:
				x=black[0].pos[0]
				y=black[0].pos[1]
				if (x+1,y)==path_r[0]:
					if (x-1,y) in black[0].moves:
						black[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in black[0].moves:
						black[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in black[0].moves:
						black[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in black[0].moves:
						black[0].moves.remove((x,y+1))
			else:
				x=black[0].pos[0]
				y=black[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in black[0].moves:
						black[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in black[0].moves:
						black[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in black[0].moves:
						black[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in black[0].moves:
						black[0].moves.remove((x-1,y+1))
					black[0].moves.remove((x-1,y+1))
		else:
			if path_k!=[]:
				path=path_k
			elif path_b!=[]:
				x=black[0].pos[0]
				y=black[0].pos[1]
				if (x+1,y+1)==path_b[0]:
					if (x-1,y-1) in black[0].moves:
						black[0].moves.remove((x-1,y-1))
				if (x-1,y-1)==path_b[0]:
					if (x+1,y+1) in black[0].moves:
						black[0].moves.remove((x+1,y+1))
				if (x-1,y+1)==path_b[0]:
					if (x+1,y-1) in black[0].moves:
						black[0].moves.remove((x+1,y-1))
				if (x+1,y-1)==path_b[0]:
					if (x-1,y+1) in black[0].moves:
						black[0].moves.remove((x-1,y+1))
				path=path_b
			elif path_r!=[]:
				x=black[0].pos[0]
				y=black[0].pos[1]
				if (x+1,y)==path_r[0]:
					if (x-1,y) in black[0].moves:
						black[0].moves.remove((x-1,y))
				if (x-1,y)==path_r[0]:
					if (x+1,y) in black[0].moves:
						black[0].moves.remove((x+1,y))
				if (x,y+1)==path_r[0]:
					if (x,y-1) in black[0].moves:
						black[0].moves.remove((x,y-1))
				if (x,y-1)==path_r[0]:
					if (x,y+1) in black[0].moves:
						black[0].moves.remove((x,y+1))
				path=path_r
			for coin in black:
				if coin.type=='K':
					for pos in coin.moves:
						old_pos=coin.pos
						coin.move(pos)
						updatedangerzone_b(white)
						if coin.pos in b_dzone:
							coin.moves.remove(pos)
						coin.move(old_pos)
				else:
					moves=coin.moves
					coin.moves=[]
					for pos in moves:
						if pos in path:
							coin.moves.append(pos)

def updateMoves_w(white):
	
	for coin in white:
		coin.gen_moves()

def updateMoves_b(black):
	for coin in black:
		coin.gen_moves()

def updatedangerzone_w(black):
	global w_dzone,board
	w_dzone=[]
	for coin in black:
		if coin.type!='p':
			w_dzone+=coin.moves
		else:
			x=coin.pos[0]
			y=coin.pos[1]
			if x>0:
				if board[(x-1,y+1)]!=-1:
					w_dzone.append((x-1,y+1))
			if x<7:
				if board[(x+1,y+1)]!=-1:
					w_dzone.append((x+1,y+1))
	w_dzone=list(set(w_dzone))
def updatedangerzone_b(white):
	global b_dzone,board
	b_dzone=[]
	for coin in white:
		if coin.type!='p':
			b_dzone+=coin.moves
		else:
			x=coin.pos[0]
			y=coin.pos[1]
			if x>0:
				if board[(x-1,y-1)]!=1:
					b_dzone.append((x-1,y-1))
			if x<7:
				if board[(x+1,y-1)]!=1:
					b_dzone.append((x+1,y-1))
	b_dzone=list(set(b_dzone))
def initBoard():
	global board
	board={}
	for y in range(8):
		for x in range(8):
			if y<=1:
				board[(x,y)]=-1
			elif y>=6:
				board[(x,y)]=1
			else :
				board[(x,y)]=0

def findpos(loc):
	global Boardsize,a,b,sq_size
	x=(loc[0]-a)//sq_size
	y=(loc[1]-b)//sq_size
	return (x,y)

def drawBoard(win):
	global Boardsize,sq_size,a,b
	pygame.draw.rect(win,(85,30,25),(a-4,b-4,Boardsize+8,4))
	pygame.draw.rect(win,(85,30,25),(a-4,b+Boardsize,Boardsize+8,4))
	pygame.draw.rect(win,(85,30,25),(a-4,b,4,Boardsize))
	pygame.draw.rect(win,(85,30,25),(a+Boardsize,b,4,Boardsize))

	pygame.draw.rect(win,(137,76,35),(a,b,sq_size,sq_size))
	pass
	x=a
	y=b
	for i in range(8):
		x=a
		for j in range(8):
			if (i+j)%2==0:
				pygame.draw.rect(win,(137,76,35),(x,y,sq_size,sq_size))
			else:
				pygame.draw.rect(win,(209,185,128),(x,y,sq_size,sq_size))
			x+=sq_size
		y+=sq_size

def displayPieces(win,white,black):

	for coin in white:
		if coin.type=='K':
			image=pygame.image.load('images/wking.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='Q':
			image=pygame.image.load('images/wqueen.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='b':
			image=pygame.image.load('images/wbishop.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='kn':
			image=pygame.image.load('images/wknight.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='r':
			image=pygame.image.load('images/wrook.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='p':
			image=pygame.image.load('images/wpawn.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))

	for coin in black:
		if coin.type=='K':
			image=pygame.image.load('images/bking.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='Q':
			image=pygame.image.load('images/bqueen.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='b':
			image=pygame.image.load('images/bbishop.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='kn':
			image=pygame.image.load('images/bknight.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='r':
			image=pygame.image.load('images/brook.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
		if coin.type=='p':
			image=pygame.image.load('images/bpawn.png')
			win.blit(image,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
def displayTitle(win,title):
	global Boardsize,sq_size,a,b
	color=(89,170,61)
	if title in ("CHECK!-White's Turn","CHECK!-Black's Turn","GAME OVER"):
		color=(228,74,66)
	pygame.draw.rect(win,(85,30,25),(a-6,4,Boardsize+12,50))
	pygame.draw.rect(win,(126,86,62),(a,10,Boardsize,40))
	font=pygame.font.Font('freesansbold.ttf', 32)
	text=font.render(title,True,color,(126,86,62))
	textRect=text.get_rect()
	textRect.center=(a+Boardsize//2,30)
	win.blit(text,textRect)

def displayWindow(win,white,black,title,select=0,coin=piece('#',0,(-1,-1))):
	global Boardsize,sq_size,a,b
	background=pygame.image.load('images/background.jpg')
	win.blit(background,(0,0))
	displayTitle(win,title)
	drawBoard(win)
	if select==1:
		greenframe=pygame.image.load('images/select.png')
		win.blit(greenframe,(a+coin.pos[0]*sq_size,b+coin.pos[1]*sq_size))
	displayPieces(win,white,black)
	if select==1:
		show_moves(win,coin)
def show_moves(win,piece):
	global Boardsize,sq_size
	for pos in piece.moves[:]:
		centre=(a+pos[0]*sq_size+sq_size//2,b+pos[1]*sq_size+sq_size//2)
		pygame.draw.circle(win,(52,113,52),centre,sq_size//4+2)
		pygame.draw.circle(win,(108,204,65),centre,sq_size//4)

def message_box(win,cat):
			#cat=1,-1,0,2,-2,3 checkmate whitewins/blackwins,stalemate,white promotion,black promotion,draw
	global sq_size
	pygame.draw.rect(win,(85,30,25),(a+sq_size*2-10,b-4+(sq_size*5)//2,4*sq_size+20,2*sq_size+8))
	if cat==2 or cat==-2:
		pygame.draw.rect(win,(126,86,62),(a+sq_size*2-6,b+(sq_size*5)//2,4*sq_size+12,sq_size-4))

		font=pygame.font.Font('freesansbold.ttf', 32)
		text=font.render("Promote To...",True,(89,170,61),(126,86,62))
		textRect=text.get_rect()
		textRect.center=(a+Boardsize//2,b+(sq_size*3)-2)
		win.blit(text,textRect)

		pygame.draw.rect(win,(126,86,62),(a+sq_size*2-6,b+(sq_size*7)//2,sq_size,sq_size))
		pygame.draw.rect(win,(126,86,62),(a+sq_size*3-2,b+(sq_size*7)//2,sq_size,sq_size))
		pygame.draw.rect(win,(126,86,62),(a+sq_size*4+2,b+(sq_size*7)//2,sq_size,sq_size))
		pygame.draw.rect(win,(126,86,62),(a+sq_size*5+6,b+(sq_size*7)//2,sq_size,sq_size))

		if cat==2:
			img=pygame.image.load('wqueen.png')
			win.blit(img,(a+sq_size*2-6,b+(sq_size*7)//2))
			img=pygame.image.load('wrook.png')
			win.blit(img,(a+sq_size*3-2,b+(sq_size*7)//2))
			img=pygame.image.load('wbishop.png')
			win.blit(img,(a+sq_size*4+2,b+(sq_size*7)//2))
			img=pygame.image.load('wknight.png')
			win.blit(img,(a+sq_size*5+6,b+(sq_size*7)//2))
		else:
			img=pygame.image.load('bqueen.png')
			win.blit(img,(a+sq_size*2-6,b+(sq_size*7)//2))
			img=pygame.image.load('brook.png')
			win.blit(img,(a+sq_size*3-2,b+(sq_size*7)//2))
			img=pygame.image.load('bbishop.png')
			win.blit(img,(a+sq_size*4+2,b+(sq_size*7)//2))
			img=pygame.image.load('bknight.png')
			win.blit(img,(a+sq_size*5+6,b+(sq_size*7)//2))
	if cat in (-1,0,1):
		pygame.draw.rect(win,(126,86,62),(a+sq_size*2-6,b+(sq_size*5)//2,4*sq_size+12,2*sq_size))

		font=pygame.font.Font('freesansbold.ttf', 40)
		if cat==0:
			text=font.render("STALEMATE!!",True,(228,74,66),(126,86,62))
		else:
			text=font.render("CHECKMATE!!",True,(228,74,66),(126,86,62))
		textRect=text.get_rect()
		textRect.center=(a+Boardsize//2,b+(sq_size*3)-2)
		win.blit(text,textRect)

		font=pygame.font.Font('freesansbold.ttf', 32)
		if cat==1:
			text=font.render("White Wins",True,(89,170,61),(126,86,62))
		elif cat==-1:
			text=font.render("Black Wins",True,(89,170,61),(126,86,62))
		else:
			text=font.render("Draw",True,(89,170,61),(126,86,62))
		textRect=text.get_rect()
		textRect.center=(a+Boardsize//2,b+(sq_size*4)-2)
		win.blit(text,textRect)
	elif cat==3:
		pygame.draw.rect(win,(126,86,62),(a+sq_size*2-6,b+(sq_size*5)//2,4*sq_size+12,2*sq_size))
		font=pygame.font.Font('freesansbold.ttf',40)
		text=font.render("Draw!!",True,(89,170,61),(126,86,62))
		textRect=text.get_rect()
		textRect.center=(a+Boardsize//2,b+(sq_size*7)//2-2)
		win.blit(text,textRect)	
def main():
	pygame.init()
	global board,Boardsize,sq_size,a,b,w_dzone,b_dzone,pinned_coins_w,pinned_coins_b,white_castle,black_castle
	Boardsize=640
	sq_size=80
	a=20
	b=60
	win=pygame.display.set_mode((Boardsize+2*a,Boardsize+b+a))
	pygame.display.set_caption('CHESS')
	white=initWhite()
	black=initBlack()
	w_dzone=[]
	b_dzone=[]
	white_castle=[1,1]		#queen side,king side
	black_castle=[1,1]
	initBoard()
	updateMoves_w(white)
	updateMoves_b(black)
	turn=1
	select=0
	check=0
	run=1
	en_passant_index=[]
	while True:
		if run==1:
			if turn==1:
				if white[0].pos in w_dzone[:]:
					check=1
				else:
					check=0

				if check==0:
					pinned_coins_w=[]
					correct_Whitemoves(white,black)
				else:
					correct_Whitemoves(white,black,1)
					checkmoves(1,white,black)
				mate=1
				for coin in white:
					if len(coin.moves)>0:
						mate=0
						break
			else:
				if black[0].pos in b_dzone[:]:
					check=-1
				else:
					check=0
				if check==0:
					pinned_coins_b=[]
					correct_Blackmoves(black,white)
				else:
					correct_Blackmoves(black,white,1)
					checkmoves(-1,white,black)
				mate=1
				for coin in black:
					if len(coin.moves)>0:
						mate=0
			if len(white)==1 and len(black)==1:
				mate=-1
			run=0
		if select==0:
			for event in pygame.event.get():   
				if event.type==pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN :
					(x,y)=event.pos
					if x>a and x<Boardsize+a and y>b and y<Boardsize+b:
						(i,j)=findpos((x,y))
						if board[(i,j)]==turn:
							if turn==1:
								for k in range(len(white)):
									if white[k].pos==(i,j):
										selected_index=k
										avail_moves=white[k].moves
										select=1
										break
							else:
								for k in range(len(black)):
									if black[k].pos==(i,j):
										selected_index=k
										avail_moves=black[k].moves
										select=1
										break

		if select==1:
			for key in pygame.event.get():
				if key.type==pygame.QUIT:
					pygame.quit()
					sys.exit()
				if key.type==pygame.MOUSEBUTTONDOWN:
					(m,n)=key.pos
					if m>a and m<Boardsize+a and n>b and n<Boardsize+b:
						(i,j)=findpos((m,n))
						if (i,j) in avail_moves[:]:
							if turn==1:
								if white[selected_index].type=='p':
									if white[selected_index].pos[1]==6 and j==4:
										if i<7:
											if board[(i+1,j)]==-1:
												for t in range(len(black)):
													if (black[t].pos==(i+1,j) or black[t].pos==(i-1,j)) and black[t].type=='p':
														en_passant_index.append(t)
										if i>0:
											if board[(i-1,j)]==-1:
												for t in range(len(black)):
													if (black[t].pos==(i+1,j) or black[t].pos==(i-1,j)) and black[t].type=='p':
														en_passant_index.append(t)
									if white[selected_index].pos[1]==3 and ((i,j)==(white[selected_index].pos[0]+1,2) or (i,j)==(white[selected_index].pos[0]-1,2)):
										if board[(i,j)]==0:
											for w in range(len(black)):
												if black[w].pos==(i,j+1):
													board[(i,j+1)]=0
													black.pop(w)
													break
								for k in range(len(black)):
									if black[k].pos==(i,j):
										board[(i,j)]=0
										black.pop(k)
										break
								white[selected_index].move((i,j))
								if selected_index==0:
									if white_castle[1]==1:
										if (i,j)==(6,7):
											for k in (range(1,len(white))):
												if white[k].pos==(7,7):
													white[k].move((5,7))
									if white_castle[0]==1:
										if (i,j)==(2,7):
											for k in (range(1,len(white))):
												if white[k].pos==(0,7):
													white[k].move((3,7))
										
									white_castle=[0,0]
								elif white[selected_index].type=='r':
									if white[selected_index].pos==(7,7):
										white_castle[1]=0
									elif white[selected_index].pos==(0,7):
										white_castle[0]=0
								elif white[selected_index].type=='p':
									if j==0:
										flag=True
										while flag:
											for event in pygame.event.get():
												if event==pygame.QUIT:
													pygame.quit()
													sys.exit()
												elif event.type==pygame.MOUSEBUTTONDOWN:
													(x,y)=event.pos
													if y>b+(sq_size*7)//2 and y<b+(sq_size*9)//2:
														if x>a+sq_size*2-6 and x<a+sq_size*3-6:
															white[selected_index].type='Q'
															flag=False
															break
														elif x>a+sq_size*3-2 and x<a+sq_size*4-2:
															white[selected_index].type='r'
															flag=False
															break
														elif x>a+sq_size*4+2 and x<a+sq_size*5+2:
															white[selected_index].type='b'
															flag=False
															break
														elif x>a+sq_size*5+6 and x<a+sq_size*6+6:
															white[selected_index].type='kn'
															flag=False
															break
											displayWindow(win,white,black,'Select Piece')
											message_box(win,2)
											pygame.display.update()
								updateMoves_w(white)
								updatedangerzone_b(white)
								updateMoves_b(black)
								updatedangerzone_w(black)
								pinned_coins_w=[]
								correct_Whitemoves(white,black)
								if en_passant_index!=[]:
									for q in en_passant_index:
										black[q].moves.append((i,j+1))
									en_passant_index=[]
							else:
								if black[selected_index].type=='p':
									if black[selected_index].pos[1]==1 and j==3:
										if i>7:
											if board[(i+1,j)]==1:
												for t in range(len(white)):
													if (white[t].pos==(i+1,j) or white[t].pos==(i-1,j))and white[t].type=='p':
														en_passant_index.append(t)
										if i<0:
											if board[(i-1,j)]==1:
												for t in range(len(white)):
													if (white[t].pos==(i+1,j) or white[t].pos==(i-1,j))and white[t].type=='p':
														en_passant_index.append(t)
									if black[selected_index].pos[1]==4 and ((i,j)==(black[selected_index].pos[0]+1,5) or (i,j)==(black[selected_index].pos[0]-1,5)):
										if board[(i,j)]==0:
											for w in range(len(white)):
												if white[w].pos==(i,j-1):
													board[(i,j-1)]=0
													white.pop(w)
													break
								for k in  range(len(white)):
									if white[k].pos==(i,j):
										board[(i,j)]=0
										white.pop(k)
										break
								black[selected_index].move((i,j))
								if selected_index==0:
									if black_castle[1]==1:
										if (i,j)==(6,0):
											for k in (range(1,len(black))):
												if black[k].pos==(7,0):
													black[k].move((5,0))

									if black_castle[0]==1:
										if (i,j)==(2,0):
											for k in (range(1,len(black))):
												if black[k].pos==(0,0):
													black[k].move((3,0))
									black_castle=[0,0]
								elif black[selected_index].type=='r':
									if black[selected_index].pos==(7,0):
										black_castle[1]=0
									elif black[selected_index].pos==(0,0):
										black_castle[0]=0

								elif black[selected_index].type=='p':
									if j==7:
										flag=True
										while flag:
											for event in pygame.event.get():
												if event==pygame.QUIT:
													pygame.quit()
													sys.exit()
												elif event.type==pygame.MOUSEBUTTONDOWN:
													(x,y)=event.pos
													if y>b+(sq_size*7)//2 and y<b+(sq_size*9)//2:
														if x>a+sq_size*2-6 and x<a+sq_size*3-6:
															black[selected_index].type='Q'
															flag=False
															break
														elif x>a+sq_size*3-2 and x<a+sq_size*4-2:
															black[selected_index].type='r'
															flag=False
															break
														elif x>a+sq_size*4+2 and x<a+sq_size*5+2:
															black[selected_index].type='b'
															flag=False
															break
														elif x>a+sq_size*5+6 and x<a+sq_size*6+6:
															black[selected_index].type='kn'
															flag=False
															break
											displayWindow(win,white,black,'Select Piece')
											message_box(win,-2)
											pygame.display.update()
								updateMoves_b(black)
								updatedangerzone_w(black)
								updateMoves_w(white)
								updatedangerzone_b(white)
								pinned_coins_b=[]
								correct_Blackmoves(black,white)
								if en_passant_index!=[]:
									for q in en_passant_index:
										white[q].moves.append((i,j-1))
									en_passant_index=[]
							run=1
							turn=-1*turn
					select=0

		if turn==1:
			if select==1:
				if check==1:
					displayWindow(win,white,black,"CHECK!-White's Turn",1,white[selected_index])
				else:
					displayWindow(win,white,black,"White's Turn",1,white[selected_index])
			else:
				if check==1:
					displayWindow(win,white,black,"CHECK!-White's Turn")
				else:
					displayWindow(win,white,black,"White's Turn")
		else:
			if select==1:	
				if check==-1:
					displayWindow(win,white,black,"CHECK!-Black's Turn",1,black[selected_index])
				else:
					displayWindow(win,white,black,"Black's Turn",1,black[selected_index])
			else:
				if check==-1:
					displayWindow(win,white,black,"CHECK!-Black's Turn")
				else:
					displayWindow(win,white,black,"Black's Turn")
		if mate!=0:
			if mate==1:
				if check==1:
					cat=-1
				elif check==-1:
					cat=1
				else:
					cat=0
			else:
				cat=3
			while True:
				for press in pygame.event.get():
					if press.type==pygame.QUIT or press.type==pygame.MOUSEBUTTONDOWN:
						pygame.quit()
						sys.exit()
				displayWindow(win,white,black,'GAME OVER')
				message_box(win,cat)
				pygame.display.update()
		pygame.display.update()

main()