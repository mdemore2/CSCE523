package rushhour.afit.edu;
import java.util.*;

public class MySearch implements Search {
	
	public int node_count = 0;
	public Board theBoard;
	public Move path;
	
	public LinkedList<Pair<String,Integer>> open;
	public LinkedList<Pair<String,Integer>> visited;
	
	public HashMap<String,Board> boardmap;

	public MySearch(Board board) {
		// TODO Auto-generated constructor stub
		theBoard = board;
		open.add(Pair.of(board.toString(),board.cost));
		boardmap.put(board.toString(),board);
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
		
		open.remove((Pair.of(theBoard.toString(),theBoard.cost)));
		visited.add(Pair.of(theBoard.toString(),theBoard.cost));
		
		Move nextMove = theBoard.genMoves();
		
		while(nextMove.next != null)//add all children to open list
		{
			theBoard.makeMove(nextMove);
			
			if(theBoard.cost == 0)
			{
				return theBoard.move_list;
			}
			
			if(!visited.contains(Pair.of(theBoard.toString(),theBoard.cost)))
			{
				open.add(Pair.of(theBoard.toString(),theBoard.cost));
				boardmap.put(theBoard.toString(),theBoard);
			}
			
			theBoard.reverseMove(nextMove);
			nextMove = nextMove.next;
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
		theBoard = boardmap.get(nextBoard.first);
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
		return 0;
		//return count of nodes (aka moves) made
	}
	

}
