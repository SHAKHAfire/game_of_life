import os
import copy
from settings import (ROWS, COLUMNS, DEAD_FIELD, 
                      ALIVE_FIELD, SURVIVE, BIRTH,
                      AUTOPLAY, FPS, FIGURE)
from time import sleep
from random import randrange as rr
#NOTE:coordinates system>>> matrix[y][x]

class Cell:
    
    def __init__(self, x:int , y:int ,alive=False):
        
        self.alive = alive
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return ALIVE_FIELD if self.alive else DEAD_FIELD
    
    def neighbors(self) -> list[tuple]:
        neighbor_list = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < COLUMNS and 0 <= ny < ROWS:
                    neighbor_list.append((nx, ny))
        return neighbor_list
    
    def alive_in_next(self) -> bool:
        neighbors_sum = sum(1 for nx, ny in self.neighbors() if matrix[ny][nx].alive)
        #Survive
        if self.alive:
            if neighbors_sum in SURVIVE:
                return True
            return False
        
        #birth
        if not self.alive: 
            if neighbors_sum in BIRTH:
                return True
            return False   
                   
        
matrix=[[Cell(x,y) for x in range(COLUMNS)]for y in range(ROWS)]
        

def display():
    row_length = COLUMNS * len(DEAD_FIELD)
    print(' ' + '_' * row_length)
    for row in matrix:
        print('|' + ''.join(map(str, row)) + '|')
    print(' ' + '‾' * row_length)


def update_matrix():
    new_mat = copy.deepcopy(matrix)
    for y in range(ROWS):
        for x in range(COLUMNS):
            new_mat[y][x].alive = matrix[y][x].alive_in_next()
    matrix[:] = new_mat


#temporary
            
def draw(fig:str):
    for y,_ in enumerate(fig.split('\n')):
        for x,char in enumerate(_):
            if char==' ':
                continue
            matrix[y][x].alive=True
             

def randomize():
    for i in range(400):
        matrix[rr(ROWS)][rr(COLUMNS)].alive = True

def main():
    draw(FIGURE)
    # randomize()
    
    gen=0
    while True:
        os.system('cls')
        display()
        print(f"{gen=}         ctrl+c to exit")
        gen+=1
        update_matrix()
        
        if not AUTOPLAY:
            input()
        else:
            sleep(1/FPS)

main()