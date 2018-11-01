import queue as queue

#define class for nodes that will be used to construct the tree
class treeNode:
	def __init__(self, state_list):
		self.state = state_list
		#appended children will be stored in a list with mantained order
		self.children = []	
		self.queenCount = 0
	def appendChild(self, node):
		self.children.append(node)

#global solutions array		
solutions = []

#function recurses in a dfs pattern in order to find all possible solutions for N
def placeQueens(root, N, col):
	#if col exceeds the number of possible columns, return
	if col == N:
		return
	#for each row on the NxN board
	for i in range(0, N):
		#check if the placement is safe before confirming
		var = isSafe(root.state, col, i)
		if var:
			#if the placement is safe store the row number in the list at index i
			root.state[col] = i
			#add the child to the tree
			newNode = treeNode(list(root.state))
			root.appendChild(newNode)
			root.queenCount = root.queenCount + 1
			if(root.queenCount == N):
				solutions.append(tuple(root.state))
			#move to the next column
			placeQueens(root, N, col+1)
			#if no possible slot is found subtract one from the row and the queen count
			root.state[col] = -1
			root.queenCount = root.queenCount -1 
	return
	


def isSafe(current_state, tryCol, tryRow):
	queens = (row for row in current_state if row != -1)
	for row in queens:
		col = current_state.index(row)
		#check row
		if(row == tryRow):
			return False
		#check diagonal
		elif((tryRow + tryCol) == (row + col) or (tryRow - tryCol) == (row - col)):
			return False
	return True


#initialize the initial tuple with all -1's
def initializeList(start, N):
	for i in range(N):
		start.append(-1)
	return start

def main():
	N = 8
	start = []
	start = initializeList(start, N)
	rootNode = treeNode(start)
	placeQueens(rootNode, N, 0)
	count = 0
	if(not solutions):
		print("There are no valid solutions")
		return
	[(x,) for x in solutions]
	for each in solutions:
		count = count + 1
		print(each,"\n")
	print(count)

	sample_solution = (0,6,4,7,1,3,5,2)
	if sample_solution in solutions:
		print("Yay that is correct")
	else:
		print("UH-OH you done messed up")
	

if __name__ == "__main__":
	main()


	
	
