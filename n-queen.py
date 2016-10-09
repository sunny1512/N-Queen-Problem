import json
def isSafe(row,col,pos):
	for i in range(0,len(pos)):
		if(pos[i][0]==row  or abs(pos[i][0]-row)==abs(pos[i][1]-col)):
			return False
	return True		
def solve(col,pos):
	global flag
	for i in range(0,n):
		if isSafe(i,col,pos):
			matrix[i][col]=1
			a=[]
			a.append(i)
			a.append(col)
			pos.append(a)
			if col==n-1:
				flag=1
				return 0
			if flag==0:
				solve(col+1,pos)
				if flag==0:
					pos.pop()	
					matrix[i][col]=0
	return 0

statement ="Problem statement :: Given a n*n matrix place n queens such that no two queen clashes each other...\n"
print statement
n=int(raw_input("Enter the dimension of chessboard "))
matrix=[]
for i in range (0,n):
	p=[]
	for j in range(0,n):
		p.append(0);
	matrix.append(p);
pos=[]
flag=0
print "Solution :: \n"
with open('start.json') as data_file:    
    data = json.load(data_file)
x=int(data["startpoint"]["y_coordinate"])    
solve(x,pos)
for i in range (0,n):
	for j in range(0,n):
		print (matrix[i][j]),		
	print "\n"	
