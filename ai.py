# this is where the files for the ai stuff will go

def __init__(self, height=5, width=5):
    
    self.height = height
    self.width = width

    self.moves_made = set()
    self.all_possible_cells = set()
    for h in range(height):
        for w in range(width):
            self.all_possible_cells.add((h,w))
    
    self.mines = set()
    self.safes = set()

    self.known = []

def dangerzone(self, cell):
    # mark a spot as a potential mine, i.e. a danger zone
    self.mines.add(cell)
    for i in self.knowledge:
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

def safetydance(self, cell):
    # mark a spot as okay to clikc, and do a lil safety dance
    self.safes.add(cell)
    for i in self.knowledge:
        if cell in self.cells:
            self.cells.remove(cell)

def add_knowledge(self, cell, count):
    # let the ai know how many mines are around a given spot
    self.moves_made.add(cell)
    self.safetydance(cell)

    new_knowledge_cells = []

    for i in range(cell[0] - 1, cell[0] + 2):
        for j in range(cell[1] - 1, cell[0] + 2):
            
            if (i, j) == cell:
                continue

            if 0 <= i < self.height and 0 <= j < self.width:
                if (i, j) not in self.moves_made and (i, j) not in self.safes:
                    new_knowledge_cells.append(i, j)
    
    if len(new_knowledge_cells) != 0:
        self.cells = set(self.cells)
        self.count = count
        self.knowledge.append(self.cells, self.count)
    
    while self.minify_knowledge() !=  self.knowledge:
        pass

    print("\n\n\n\n")
    print("------------------------------------------------------------------")

    print("\nMove: ",cell)

    print("Knowledge Base:")
    for sentence in self.knowledge:
        print(sentence)
        
    print("\nConfirmed Safe:")
    print(self.safes)

    print("\nConfirmed Mines:")
    print(self.mines)
    print("------------------------------------------------------------------")

def mark_safe_move(self):
    if len(self.safes) > 0:
        return self.safes.pop()
    else:
        return None

def make_random_move(self):
    freeSets = self.all_possible_cells - self.moves_made - self.mines
    if len(freeSets) > 0:
        return random.choice(tuple(freeSets))
    else:
        return None

def minify_knowledge(self):
    knowledge_todo = self.knowledge.copy()

    for i in knowledge_todo:
        if self.count == 0:
            known_safes = self.cells
        if len(self.cells) == self.count:
            known_mines = self.cells
    
        if known_safes:
            self.safes.update(known_safes)
            self.knowledge.remove(i)
        if known_mines:
            self.knowledge.remove(i)
            for j in known_mines.union(self.mines):
                self.mark_mine(mine)

def getFlags(self):
    return self.mines