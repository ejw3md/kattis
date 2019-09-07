#include <iostream>
#include <vector>

using namespace std;

void printGrid(const vector<vector<char>> grid);
void placeApples(vector<vector<char>>& grid, int c);

int main()
{
	int rows, cols;
	cin>>rows>>cols;
	vector<vector<char>> grid (rows);
	
	
	
	for(int i=0; i<rows; i++)
	{
		grid[i] = vector<char>(cols);
		for(int j=0; j<cols; j++)
		{
			char temp;
			cin>>temp;
			grid[i][j] = temp;
		}
	}
	for(int i=0; i<cols; i++)
	{
		placeApples(grid, i);
	}
	printGrid(grid);
}

void placeApples(vector<vector<char>>& grid, int c)
{
	int lowestPlace = grid.size()-1;
	int curItr = grid.size()-1;
	while( curItr>= 0 )
	{
		while( lowestPlace >= 0 && grid[lowestPlace][c] != '.' )
		{
			lowestPlace-=1;	
		}
		if( curItr < lowestPlace && grid[curItr][c] == 'a')
		{
			grid[lowestPlace][c] = 'a';
			grid[curItr][c] = '.';
			lowestPlace-=1;
		}
		else if(grid[curItr][c] == '#')
		{
			lowestPlace = curItr-1;	
		}
		curItr--;
	}
	
}

void printGrid(const vector<vector<char>> grid)
{
	for(int i=0; i<grid.size(); i++)
	{
		for(int j=0; j<grid[0].size(); j++)
		{
			cout<<grid[i][j];	
		}
		cout<<endl;
	}
	
}