package rushhour.afit.edu;
import java.util.*;

public class MySearch implements Search {
	
	public int node_count;
	public Board currentBoard;
	public Move path;
	
	public LinkedList<Pair<String,Integer>> open = new LinkedList<Pair<String,Integer>>();
	public LinkedList<Pair<String,Integer>> visited = new LinkedList<Pair<String,Integer>>();
	
	public HashMap<String,Board> boardmap = new HashMap<String,Board>();

	public MySearch(Board board) {
		// TODO Auto-generated constructor stub
		currentBoard = board;
		open.add(Pair.of(toString(board),board.cost));
		boardmap.put(toString(board),board);
		node_count = 0;
	}

	
	  /**
     * The findMoves method will be where the search code actually goes. It is 
     * expecting a return of the move list to the goal. The Board objects keep
     * track of the moves which got you to the goal so all you need to do is once
     * the goal is found return the move_list for the goal Board.
     * 
     * @return
     */
	@Override
	public Move findMoves() {
		
		
		open.remove((Pair.of(toString(currentBoard),currentBoard.cost)));
		visited.add(Pair.of(toString(currentBoard),currentBoard.cost));
		
		Move nextMove = currentBoard.genMoves();
		
		while(nextMove != null)//add all children to open list
		{
			currentBoard.makeMove(nextMove);
			
			if(currentBoard.cost == 0)
			{
				return currentBoard.move_list;
			}
			
			if(!visited.contains(Pair.of(toString(currentBoard),currentBoard.cost)))
			{
				open.add(Pair.of(toString(currentBoard),currentBoard.cost));
				node_count++;
				boardmap.put(toString(currentBoard),currentBoard);
			}
			
			currentBoard.reverseMove(nextMove);
			nextMove = nextMove.next;
		}
		
		if(open.size() < 1 )
		{
			return null;
		}
		
		Pair<String,Integer> iterBoard = open.getFirst();
		Pair<String,Integer> nextBoard = open.getFirst();
		//find element in open with lowest cost, iterate again over that
		for(int i = 0; i < open.size(); i++)
		{
			iterBoard = open.get(i);
			if(iterBoard.second < nextBoard.second)
			{
				nextBoard = iterBoard;
			}
		}
		
		//search on new board
		currentBoard = boardmap.get(nextBoard.first);
		
		if(currentBoard == null)
		{
			return null;
		}
		
		findMoves();
		
		return null;
		//return move list
	}
	
	 /**
     * Inside your search you should also keep an incrementor around which keeps
     * track of the number of nodes expanded. This method just returns that count.
     * 
     * @return
     */
	@Override
	public long nodeCount() {
		// TODO Auto-generated method stub
		return node_count;
		//return count of nodes (aka moves) made
	}
	
	/*
	  * creates string representation of board for the visited list
	  *
	  * @return String resultant String representation of the board
	  */
	 public String toString(Board b) {
	   String outString = new String();

	    for ( int i = 0; i < Board.BOARD_SIZE+1; i++ )
	      for ( int j = 0; j < Board.BOARD_SIZE; j++ )  outString = outString.concat(String.valueOf(b.theBoard[i][j]));
	    return outString;
	   }

}
