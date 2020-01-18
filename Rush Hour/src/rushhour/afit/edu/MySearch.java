package rushhour.afit.edu;
import java.util.*;

public class MySearch implements Search {
	
	public int node_count = 0;
	public Board theBoard;
	public Move path;
	
	public LinkedList<String> open;
	public LinkedList<String> visited;

	public MySearch(Board board) {
		// TODO Auto-generated constructor stub
		theBoard = board;
		open.add(board.toString());
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
		
		open.remove();
		visited.add(theBoard.toString());
		Move nextMove = theBoard.genMoves();
		
		while(nextMove.next != null)//add all children to open list
		{
			theBoard.makeMove(nextMove);
			
			if(theBoard.goalHeur == 0)
			{
				return theBoard.move_list;
			}
			
			if(!visited.contains(theBoard.toString()))
			{
				open.add(theBoard.toString());
			}
			
			theBoard.reverseMove(nextMove);
			nextMove = nextMove.next;
		}
		
		//find element in open with lowest cost, iterate again over that
		
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
		return 0;
		//return count of nodes (aka moves) made
	}

}
