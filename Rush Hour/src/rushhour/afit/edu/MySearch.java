package rushhour.afit.edu;
import java.util.*;

public class MySearch implements Search {
	
	public int node_count;
	public Board currentBoard;
	public Move path;
	

	public PriorityQueue<Board> open = new PriorityQueue<Board>(new Board_Comparator());
	public HashMap<String,Board> visited = new HashMap<String,Board>();
	public HashMap<String,Board> openHash = new HashMap<String,Board>();
	
	
	class Board_Comparator implements Comparator<Board>{
		public int compare(Board b1, Board b2)
		{
			if(b1.cost > b2.cost)
			{
				return 1;
			}
			else if(b1.cost < b2.cost)
			{
				return -1;
			}
			else
			{
				return 0;
			}
		}
	}

	public MySearch(Board board) {
		currentBoard = board;
		open.add(board);
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
		
		Board nextBoard = currentBoard;
		
		while(!open.isEmpty())
		{
			
			nextBoard = new Board(open.poll());
			visited.put(toString(nextBoard),nextBoard);
			

			
			Move nextMove = nextBoard.genMoves();
			node_count++;
			
			while(nextMove != null)//add all children to open list
			{
				Board childBoard = new Board(nextBoard);
				childBoard.makeMove(nextMove);
				
				if(childBoard.cost == 0)
				{
					return childBoard.move_list;
				}
				
				if(!visited.containsKey(toString(childBoard)) && !openHash.containsKey(toString(childBoard)))
				{
					childBoard.setNodeCount(node_count);
					open.add(childBoard);
					openHash.put(toString(childBoard), childBoard);
					
				}
				
				nextMove = nextMove.next;
			}
			
				
		}
		
		return null;
		
	}
	
	 /**
     * Inside your search you should also keep an incrementor around which keeps
     * track of the number of nodes expanded. This method just returns that count.
     * 
     * @return
     */
	@Override
	public long nodeCount() {
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
