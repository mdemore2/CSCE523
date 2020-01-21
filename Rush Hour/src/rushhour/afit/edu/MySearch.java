package rushhour.afit.edu;
import java.util.*;

public class MySearch implements Search {
	
	public int node_count;
	public Move path;
	

	public PriorityQueue<Board> open = new PriorityQueue<Board>(new Board_Comparator());
	public HashMap<String,Board> visited = new HashMap<String,Board>();
	public HashMap<String,Board> openHash = new HashMap<String,Board>();
	
	
	class Board_Comparator implements Comparator<Board>{
	//comparator for open priority queue, lowest cost at head	
		
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
		open.add(board); //add starting node to open queue
		node_count = 0; //reset node count
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
		
		Board nextBoard;
		
		while(!open.isEmpty())
		{
			
			nextBoard = new Board(open.poll()); //pop lowest cost next move from open
			visited.put(toString(nextBoard),nextBoard); //add to visited list
			node_count++; //increment node count for this visited parent


			
			Move nextMove = nextBoard.genMoves(); //get transition to new states (moves from current node)
			
			while(nextMove != null)
			{
				Board childBoard = new Board(nextBoard);//make copy of board to look at child states
				childBoard.makeMove(nextMove);
				
				if(childBoard.cost == 0)
				{
					return childBoard.move_list; //if this is a goal, return moves
				}
				
				if(!visited.containsKey(toString(childBoard)) && !openHash.containsKey(toString(childBoard))) //check if board config seen already
				{
					childBoard.setNodeCount(node_count); //if not, set node count of board for cost calculation
					open.add(childBoard); //add to open queue
					openHash.put(toString(childBoard), childBoard); //track seen boards
					
				}
				
				nextMove = nextMove.next; //look at neighbor
			}
			
				
		}
		
		return null; //no path found
		
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
