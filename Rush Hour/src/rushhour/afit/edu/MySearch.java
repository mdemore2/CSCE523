package rushhour.afit.edu;

public class MySearch implements Search {

	public MySearch(Board board) {
		// TODO Auto-generated constructor stub
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
		// TODO Auto-generated method stub
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
