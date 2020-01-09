from tkinter import *
from tkinter import messagebox
from operator import le, ge, sub, add
import copy

class App():
    
    def __init__(self):
        self.board = [
            ['BR1','BH1','BB1','BQ1','BK1','BB2','BH2','BR2'],
            ['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8'],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'],
            ['WR1','WH1','WB1','WQ1','WK1','WB2','WH2','WR2'],
            ]
        self.black_pieces = ['BR1','BH1','BB1','BQ1','BK1','BB2','BH2','BR2',
                             'BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8']
        self.white_pieces = ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8',
                             'WR1','WH1','WB1','WQ1','WK1','WB2','WH2','WR2']
        self.highlighted_piece = None
        self.adversary = 'Black'
        self.current_turn = 'White'
        self.stopper = False
        self.white_castle = [False, False, False]
        self.black_castle = [False, False, False]
        self.window = Tk()
        self.window.title('Chess')
        self.canvas = Canvas(self.window, bg='white', height=800, width=800)
        self.canvas.pack()
        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=self.about_menu)
        self.filemenu.add_command(label="New Game", command=self.new_game)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.window.destroy)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.window.config(menu=self.menubar)
        self.create_canvas()
        self.create_pieces()
        self.window.mainloop()

    def about_menu(self):
        messagebox.showinfo("About", "Made By Jason Alencewicz")
        return

    def new_game(self):
        self.board = [
            ['BR1','BH1','BB1','BQ1','BK1','BB2','BH2','BR2'],
            ['BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8'],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8'],
            ['WR1','WH1','WB1','WQ1','WK1','WB2','WH2','WR2'],
            ]
        self.black_pieces = ['BR1','BH1','BB1','BQ1','BK1','BB2','BH2','BR2',
                             'BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8']
        self.white_pieces = ['WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8',
                             'WR1','WH1','WB1','WQ1','WK1','WB2','WH2','WR2']
        self.highlighted_piece = None
        self.adversary = 'Black'
        self.current_turn = 'White'
        self.white_castle = [False, False, False]
        self.black_castle = [False, False, False]
        self.stopper = False
        self.canvas.delete("all")
        self.create_canvas()
        self.create_pieces()
        return
    
    def create_canvas(self):
        location = [0,-100,0,0]
        for x in range(len(self.board)):

            if x % 2 == 0:
                color ='white'
            else:
                color = 'sienna4'
                
            location[0] = 0
            location[1]+= 100
            location[2] = 100
            location[3]+= 100
            for y in range(len(self.board)):
                tag_id = 'r'+str(x)+'c'+str(y)
                self.canvas.create_rectangle(location[0], location[1], location[2], location[3],outline="black", fill=color, tag=tag_id)
                self.canvas.tag_bind(tag_id, '<1>', self.on_click_square)
                location[0]+=100
                location[2]+=100
                if color == 'sienna4':
                    color = 'white'
                elif color == 'white':
                    color = 'sienna4'
        return

    def create_pieces(self):
        location = [0,-100]
        for x in range(len(self.board)):
            location[0] = 0
            location[1]+= 100
            for y in range(len(self.board)):
                piece = self.board[x][y]
                if piece == 0:
                    pass
                elif 'WP' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="P",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BP' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="P",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'WR' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="R",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BR' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="R",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'WB' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="B",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BB' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="B",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'WH' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="H",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BH' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="H",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'WQ' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="Q",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BQ' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="Q",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'WK' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="K",font=("Purisa", 28),fill='darkgray', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                elif 'BK' in piece:
                    tag_id = self.board[x][y]
                    self.canvas.create_text(location[0]+50, location[1]+50, text="K",font=("Purisa", 28),fill='black', tag=tag_id)
                    self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
                location[0] += 100
        return 

    def on_click_square(self, event):
        square =self.canvas.find_closest(event.x, event.y)
        new_square = self.canvas.itemcget(square, "tag").replace(' current','')
        new_row = int(new_square[1])
        new_col = int(new_square[3])
        if self.highlighted_piece == None:
            return
        elif self.canvas.itemcget(square, "outline") == 'red':
            msg = messagebox.askyesno('Castle',"Would you like to castle with this rook?")
            if msg == True:
                self.perform_castle(square)
            else:
                self.deselect()
            return
        elif self.canvas.itemcget(square, "outline") == 'orange':
            old_square = self.get_current_square(self.highlighted_piece)
            if self.check_if_viable_move(old_square, new_square) == False:
                return self.deselect()
            if self.board[new_row][new_col] != 0 and self.adversary[0] == str(self.board[new_row][new_col])[0]:
                self.remove_piece(new_square)
            self.move_piece(old_square, new_square, self.highlighted_piece)
        else:
            self.deselect()
        return
    
    def check_castle(self, square):
        if self.current_turn == 'Black' and self.black_castle[0] == False:
            if self.black_castle[1] == False and self.highlighted_piece == 'BR1':
                self.canvas.itemconfig(square, outline='red')  
            elif self.black_castle[2] == False and self.highlighted_piece == 'BR2':
                self.canvas.itemconfig(square, outline='red')  
        if self.current_turn == 'White' and self.white_castle[0] == False:
            if self.white_castle[1] == False and self.highlighted_piece == 'WR1':
                self.canvas.itemconfig(square, outline='red')  
            elif self.white_castle[2] == False and self.highlighted_piece == 'WR2':
                self.canvas.itemconfig(square, outline='red')  
        return
    
    def perform_castle(self, square):
        piece = self.highlighted_piece
        king_piece = str(self.current_turn[0])+'K1'
        if self.highlighted_piece == "WR1":
            old_rook_square = 'r7c0'
            new_rook_square = 'r7c3'
            old_king_square = 'r7c4'
            new_king_square = 'r7c2'
        elif self.highlighted_piece == "WR2":
            old_rook_square = 'r7c7'
            new_rook_square = 'r7c5'
            old_king_square = 'r7c4'
            new_king_square = 'r7c6'
        elif self.highlighted_piece == "BR1":
            old_rook_square = 'r0c0'
            new_rook_square = 'r0c3'
            old_king_square = 'r0c4'
            new_king_square = 'r0c2'
        elif self.highlighted_piece == "BR2":
            old_rook_square = 'r0c7'
            new_rook_square = 'r0c5'
            old_king_square = 'r0c4'
            new_king_square = 'r0c6'

        if self.check_if_viable_move(old_rook_square, new_rook_square, old_king_square, new_king_square, king_piece) == True:
            self.move_piece(old_rook_square, new_rook_square, piece)
            self.move_piece(old_king_square, new_king_square, king_piece)
            self.get_piece_type(piece, new_rook_square, 1)
            self.adjust_castle(king_piece)
            self.deselect()
            self.switch_turn()
        else:
            self.deselect()
        return

    def adjust_castle(self, piece):
        if piece == 'BK1':
            self.black_castle[0] = True
        elif piece == 'BR1':
            self.black_castle[1] = True
        elif piece == 'BR2':
            self.black_castle[2] = True
        elif piece == 'WK1':
            self.white_castle[0] = True
        elif piece == 'WR1':
            self.white_castle[1] = True
        elif piece == 'WR2':
            self.white_castle[2] = True
        return
    
    def on_click_piece(self, event):
        self.deselect()
        item = self.canvas.find_closest(event.x, event.y)
        piece = self.canvas.itemcget(item, "tag").replace(' current','')
        if piece[0] == self.current_turn[0]:
            self.canvas.itemconfig(item, fill='yellow')
            self.highlighted_piece = piece
            current_square = self.get_current_square(piece)
            self.get_piece_type(piece, current_square, 0)
        return

    def check_if_viable_move(self, old_square, new_square, *args, **kwargs):
        old_board = copy.deepcopy(self.board)

        #additional args are for when castling
        if args:
            old_square2 = args[0]
            new_square2 = args[1]
            piece = args[2]
            self.board[int(old_square2[1])][int(old_square2[3])] = 0
            self.board[int(new_square2[1])][int(new_square2[3])] = piece

        self.board[int(old_square[1])][int(old_square[3])] = 0
        self.board[int(new_square[1])][int(new_square[3])] = self.highlighted_piece
        for x, v1 in enumerate(self.board):
            for y, v2 in enumerate(v1):
                if v2 == 0:
                    continue
                elif self.adversary[0] == v2[0]:
                    square = 'r'+str(x)+'c'+str(y)
                    self.get_piece_type(v2, square, 2)
                    if self.stopper == True:
                        messagebox.showinfo('Oops!', "Can't move into check!")
                        self.stopper = False
                        self.board = copy.deepcopy(old_board)
                        return False
        self.board = copy.deepcopy(old_board)
        return True

    def announce_check(self):
        if self.adversary[0] == 'B':
            messagebox.showinfo('Check!', 'Black player is in check!')
        elif self.adversary[0] == 'W':
            messagebox.showinfo('Check!', 'White player is in check!')
        return

    def remove_piece(self, square):
        piece = self.board[int(square[1])][int(square[3])]
        self.canvas.delete(piece)
        if piece[0] == 'B':
            self.black_pieces.remove(piece)
        elif piece[0] == 'W':
            self.white_pieces.remove(piece)
        return

    def get_piece_type(self, piece, current_square, switch):
        if piece[1] == 'P':
            self.get_pawn_moves(piece, current_square, switch)
        elif piece[1] == 'R':
            self.get_rook_moves(piece, current_square, switch)
        elif piece[1] == 'H':
            self.get_horse_moves(piece, current_square, switch)
        elif piece[1] == 'B':
            self.get_bishop_moves(piece, current_square, switch)
        elif piece[1] == 'Q':
            self.get_queen_moves(piece, current_square, switch)
        elif piece[1] == 'K':
            self.get_king_moves(piece, current_square, switch)
        return

    def get_pawn_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])
        square1 = None
        square2 = None
        square3 = None
        square4 = None

        if 'W' in piece:
            if self.board[row-1][col] == 0:
                square1 = 'r'+str(row-1)+'c'+str(col)
            if row == 6 and self.board[row-2][col] == 0:
                square2 = 'r'+str(row-2)+'c'+str(col)
            if col != 7 and self.adversary[0] == str(self.board[row-1][col+1])[0] or switch == 2:
                square3 = 'r'+str(row-1)+'c'+str(col+1)
            if col != 0 and self.adversary[0] == str(self.board[row-1][col-1])[0] or switch == 2:
                square4 = 'r'+str(row-1)+'c'+str(col-1)

        elif 'B' in piece:
            if self.board[row+1][col] == 0:
                square1 = 'r'+str(row+1)+'c'+str(col)
            if row == 1 and self.board[row+2][col] == 0:
               square2 = 'r'+str(row+2)+'c'+str(col)
            if col != 7 and self.adversary[0] == str(self.board[row+1][col+1])[0] or switch == 2:
                square3 = 'r'+str(row+1)+'c'+str(col+1)
            if col != 0 and self.adversary[0] == str(self.board[row+1][col-1])[0] or switch == 2:
                square4 = 'r'+str(row+1)+'c'+str(col-1)

        if switch == 1 or switch == 2:
            for square in [square3, square4]:
                self.check_for_king(square, switch)
        else:
            self.highlight_squares(square1, square2, square3, square4)
        return
        
    def get_horse_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])

        square1 = 'r'+str(row+2)+'c'+str(col+1)
        square2 = 'r'+str(row+2)+'c'+str(col-1)
        square3 = 'r'+str(row-2)+'c'+str(col+1)
        square4 = 'r'+str(row-2)+'c'+str(col-1)
        square5 = 'r'+str(row+1)+'c'+str(col+2)
        square6 = 'r'+str(row+1)+'c'+str(col-2)
        square7 = 'r'+str(row-1)+'c'+str(col+2)
        square8 = 'r'+str(row-1)+'c'+str(col-2)

        if switch == 1 or switch == 2:
            for square in [square1, square2, square3, square4, square5, square6, square7, square8]:
                self.check_for_king(square, switch)
        else:
            self.highlight_squares(square1, square2, square3, square4, square5, square6, square7, square8)
        
        return 

    def get_rook_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])
        left = col-1
        up = row-1
        right = col+1
        down = row+1
        
        self.horizontal(left, ge, 0, sub, row, switch)
        self.horizontal(right, le, 7, add, row, switch)
        self.vertical(up, ge, 0, sub, col, switch)
        self.vertical(down, le, 7, add, col, switch)
        return

    def get_bishop_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])

        upleftrow = row -1
        upleftcol = col -1

        uprightrow = row -1
        uprightcol = col +1

        downleftrow = row + 1
        downleftcol = col - 1

        downrightrow = row+1
        downrightcol = col +1

        self.diagonal(upleftcol, ge, 0, upleftrow, ge, 0, sub, sub, switch)
        self.diagonal(uprightcol, le, 7, uprightrow, ge, 0, sub, add, switch)
        self.diagonal(downleftcol, ge, 0, downleftrow, le, 7, add, sub, switch)
        self.diagonal(downrightcol, le, 7, downrightrow, le, 7, add, add, switch)
        return

    def get_queen_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])

        left = col-1
        up = row-1
        right = col+1
        down = row+1

        upleftrow = row-1
        upleftcol = col-1

        uprightrow = row-1
        uprightcol = col+1

        downleftrow = row+1
        downleftcol = col-1

        downrightrow = row+1
        downrightcol = col+1

        self.horizontal(left, ge, 0, sub, row, switch)
        self.horizontal(right, le, 7, add, row, switch)
        self.vertical(up, ge, 0, sub, col, switch)
        self.vertical(down, le, 7, add, col, switch)
        self.diagonal(upleftcol, ge, 0, upleftrow, ge, 0, sub, sub, switch)
        self.diagonal(uprightcol, le, 7, uprightrow, ge, 0, sub, add, switch)
        self.diagonal(downleftcol, ge, 0, downleftrow, le, 7, add, sub, switch)
        self.diagonal(downrightcol, le, 7, downrightrow, le, 7, add, add, switch)
        return

    def horizontal(self, direction, sign1, num1, sign2, row, switch):
        while sign1(direction, num1):
            square =  'r'+str(row)+'c'+str(direction)
            if  (switch == 0 or switch == 1) and self.board[row][direction] == 0:
                self.highlight_squares(square)
                direction = sign2(direction, 1)
            elif switch == 0 and self.adversary[0] == str(self.board[row][direction])[0]:
                self.highlight_squares(square)
            elif switch == 0 and self.highlighted_piece[1] == 'R' and (square == 'r7c4' or square == 'r0c4'):
                self.check_castle(square)
                break
            elif switch == 1 and self.adversary[0]+'K' in str(self.board[row][direction]):
                self.announce_check()
                return
            elif switch == 2:
                if self.current_turn[0]+'K' in str(self.board[row][direction]):
                    self.stopper = True
                return    
            else:
                break
        return
              
    def diagonal(self, col, sign1, num1, row, sign2, num2, sign3, sign4, switch):
        while sign1(col, num1) and sign2(row, num2):
            square =  'r'+str(row)+'c'+str(col)
            if (switch == 0 or switch == 1) and self.board[row][col] == 0:
                self.highlight_squares(square)
                row = sign3(row, 1)
                col = sign4(col, 1)
            elif switch == 0 and self.adversary[0] == str(self.board[row][col])[0]:
                self.highlight_squares(square)
                return
            elif switch == 1 and self.adversary[0]+'K' in str(self.board[row][col]):
                self.announce_check()
                return
            elif switch == 2:
                if self.current_turn[0]+'K' in str(self.board[row][col]):
                    self.stopper = True
                return
            else:
                break
        return

    def vertical(self, direction, sign1, num1, sign2, col, switch):
        while sign1(direction, num1):
            
            square =  'r'+str(direction)+'c'+str(col)
            if  (switch == 0 or switch == 1) and self.board[direction][col] == 0:
                self.highlight_squares(square)
                direction = sign2(direction, 1)
            elif switch == 0 and self.adversary[0] == str(self.board[direction][col])[0]:
                self.highlight_squares(square)
                return
            elif switch == 1 and self.adversary[0]+'K' in str(self.board[direction][col]):
                self.announce_check()
                return                                                                
            elif switch == 2:
                if self.current_turn[0]+'K' in str(self.board[direction][col]):
                    self.stopper = True
                return
            else:
                break
        return
        
    def get_king_moves(self, piece, current_square, switch):
        row = int(current_square[1])
        col = int(current_square[3])

        square1 = 'r'+str(row+1)+'c'+str(col-1)
        square2 = 'r'+str(row+1)+'c'+str(col)
        square3 = 'r'+str(row+1)+'c'+str(col+1)
        square4 = 'r'+str(row)+'c'+str(col-1)
        square5 = 'r'+str(row)+'c'+str(col+1)
        square6 = 'r'+str(row-1)+'c'+str(col-1)
        square7 = 'r'+str(row-1)+'c'+str(col)
        square8 = 'r'+str(row-1)+'c'+str(col+1)

        if switch == 1 or switch == 2:
            for square in [square1, square2, square3, square4, square5, square6, square7, square8]:
                self.check_for_king(square, switch)
        else:
            self.highlight_squares(square1, square2, square3, square4, square5, square6, square7, square8)
        return 

    def check_for_king(self, square, switch):
        if square == None:
            return
        elif '8' in square or '9' in square or '-' in square:
            return
        elif self.board[int(square[1])][int(square[3])] == 0:
            return
        elif switch == 1 and self.adversary[0]+'K' in self.board[int(square[1])][int(square[3])]:
            self.announce_check()
        elif switch == 2 and self.current_turn[0]+'K' in self.board[int(square[1])][int(square[3])]:
            self.stopper = True
        return

    def move_piece(self, old_square, new_square, piece):
        old_loc = self.adjust_location(self.canvas.bbox(old_square))
        new_loc = self.adjust_location(self.canvas.bbox(new_square))
        self.canvas.move(piece,(new_loc[0]-old_loc[0]),new_loc[3]-old_loc[3])
        self.board[int(old_square[1])][int(old_square[3])] = 0
        self.board[int(new_square[1])][int(new_square[3])] = piece

        if 'WP' in piece and int(new_square[1]) == 0:
            self.check_promotion(new_square, 'queen')
        elif 'BP' in piece and int(new_square[1]) == 7:
            self.check_promotion(new_square, 'queen')

        if piece[1] == 'R' or piece[1] == 'K':
            self.adjust_castle(piece)

        self.get_piece_type(piece, new_square, 1)
        self.deselect()
        self.switch_turn()
        return
        
    def check_promotion(self, new_square, new_piece):
        msg = "Would you like to become a {}?".format(new_piece)
        question = messagebox.askyesno("You're being promoted!", msg)
        if question == True:
            self.promote_pawn(new_square, new_piece)
            return
        else:
            if new_piece == 'queen':
                return self.check_promotion(new_square, 'horse')
            elif new_piece == 'horse':
                return self.check_promotion(new_square, 'rook')
            elif new_piece == 'rook':
                return self.check_promotion(new_square, 'bishop')
            elif new_piece == 'bishop':
                return self.check_promotion(new_square, 'queen')
        return
            
    def promote_pawn(self, new_square, new_piece):
        self.canvas.delete(self.highlighted_piece)
        loc = self.adjust_location(self.canvas.bbox(new_square))
        color = 'black' if self.highlighted_piece[0] == 'B' else 'darkgray'
        piece_type, tag_id = self.get_piece_info(new_piece)
        number = self.check_piece_number(color, piece_type)
        tag_id = tag_id+str(number)
        self.canvas.create_text(loc[0]+50, loc[1]+50, text=piece_type, font=("Purisa", 28),fill=color, tag=tag_id)
        self.canvas.tag_bind(tag_id, '<1>', self.on_click_piece)
        self.board[int(new_square[1])][int(new_square[3])] = tag_id
        self.black_pieces.append(tag_id) if color == 'black' else self.white_pieces.append(tag_id)
        self.get_piece_type(tag_id, new_square, 1)
        return

    def check_piece_number(self, color, piece_type):
        number = 0
        if color == 'black':
            for item in self.black_pieces:
                if item[1] == piece_type:
                    if int(item[2]) > number:
                        number = int(item[2])
                    else:
                        continue
        else:
            for item in self.white_pieces:
                if item[1] == piece_type:
                    if int(item[2]) > number:
                        number = int(item[2])
                    else:
                        continue
        return number+1
        
    def get_piece_info(self, new_piece):
        if new_piece == 'queen':
            tag_id = self.highlighted_piece[0] + 'Q'
            piece_type = 'Q'
        elif new_piece == 'horse':
            tag_id = self.highlighted_piece[0] + 'H'
            piece_type = 'H'
        elif new_piece == 'rook':
            tag_id = self.highlighted_piece[0] + 'R'
            piece_type = 'R'
        elif new_piece == 'bishop':
            tag_id = self.highlighted_piece[0] + 'B'
            piece_type = 'B'
        return piece_type, tag_id
    
    def adjust_location(self, loc_list):
        new_list = list(loc_list)
        new_list[0] += 1
        new_list[1] += 1
        new_list[2] -= 1
        new_list[3] -= 1
        return new_list

    def highlight_squares(self,*args, **kwargs):
        for item in args:
            if item == None:
                continue
            elif ('-' in item) or int(item[1]) > 7 or int(item[3]) > 7:
                continue
            elif self.board[int(item[1])][int(item[3])] == 0:
                self.canvas.itemconfig(item, outline='orange')
            elif self.adversary[0] == str(self.board[int(item[1])][int(item[3])])[0]:
                self.canvas.itemconfig(item, outline='orange')                 
            else:
                continue
        return
            
    def get_current_square(self, piece):
        for x, value1 in enumerate(self.board):
            for y, value2 in enumerate(value1):
                if self.board[x][y] == piece:
                    current_square = 'r'+str(x)+'c'+str(y)
                    return current_square
        return
    
    def deselect(self):
        for x in self.canvas.find_all():
            item = self.canvas.itemcget(x, "tag").replace(' current','')
            if item[0] == 'r':
                self.canvas.itemconfig(x, outline='black')
            elif item[0] == 'B':
                self.canvas.itemconfig(x, fill='black')
            elif item[0] == 'W':
                self.canvas.itemconfig(x, fill='darkgray')
        self.highlighted_piece = None
        return

    def switch_turn(self):
        if self.current_turn == 'Black':
            self.current_turn = 'White'
            self.adversary = 'Black'
        elif self.current_turn == 'White':
            self.current_turn = 'Black'
            self.adversary = 'White'
        return 

App()
