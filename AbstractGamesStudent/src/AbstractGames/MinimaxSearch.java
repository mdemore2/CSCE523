package AbstractGames;


import AbstractGames.LinesOfAction.LOABoard;
import AbstractGames.LinesOfAction.LOAMove;

public class MinimaxSearch<BOARD extends Board, MOVE extends Move> implements Search<BOARD,MOVE>  {
  BOARD board;
  int totalNodesSearched;
  int totalLeafNodes;

  static final int PLAYER_WHITE = 0;
  static final int PLAYER_BLACK = 1;

  //int Max = 0, Min = 0;
  //double alpha = Double.NEGATIVE_INFINITY, beta = Double.POSITIVE_INFINITY;

  @Override
  public MOVE findBestMove(BOARD board, int depth) {
    MOVE best_move = null;
    int runningNodeTotal = 0;
    long startTime = System.currentTimeMillis();
    long elapsedTime = 0;
    long currentPeriod;
    long previousPeriod = 0;
    int i = 1;

    /*this.board = board;
    alpha = Double.NEGATIVE_INFINITY;
    beta = Double.POSITIVE_INFINITY;

    this.Max = board.getCurrentPlayer();
    if(Max == PLAYER_BLACK)
    {
      Min = PLAYER_WHITE;
    }
    else
    {
      Min = PLAYER_BLACK;
    }*/

    // Including the iterative deepening for consistency.
    while ( i <= depth ) {
      totalNodesSearched = totalLeafNodes = 0;

      best_move = Minimax(i); // Min-Max alpha beta with transposition tables

      elapsedTime = System.currentTimeMillis()-startTime;
      currentPeriod = elapsedTime-previousPeriod;
      double rate = 0.0;
      if ( i > 3 && previousPeriod > 50 )
        rate = (currentPeriod - previousPeriod)/previousPeriod;
      previousPeriod = elapsedTime;

      runningNodeTotal += totalNodesSearched;
      System.out.println("Depth: " + i +" Time: " + elapsedTime/1000.0 + " " + currentPeriod/1000.0 + " Nodes Searched: " +
          totalNodesSearched + " Leaf Nodes: " + totalLeafNodes + " Rate: " + rate);

      // increment indexes;
      i = i + 2;
    }

    System.out.println("Nodes per Second = " + runningNodeTotal/(elapsedTime/1000.0));
    if (best_move == null ) {
      throw new Error ("No Move Available - Search Error!");
    }
    return best_move;
  }

  /**
   * TODO Write Minimax here!
   *
   * @param depth Depth to search to
   * @return best move found at this node
   */
  private MOVE Minimax(int depth) {

    if(depth == 0)
    {
      return null;//return the move to get to this board?
    }

    MOVE child = (MOVE) this.board.generateMoves();
    MOVE bestMove = child;
    this.board.makeMove(child);
    double best = this.board.heuristicEvaluation();
    this.board.reverseMove(child);

    double eval = 0;

    while(child != null)
    {
      eval = recursiveMinimaxAB(this.board,depth,true,Double.NEGATIVE_INFINITY,Double.POSITIVE_INFINITY);
      if(eval > best)
      {
        best = eval;
        bestMove = child;
      }

      child = (MOVE) child.next;
    }

    return bestMove;
  }


  private double recursiveMinimaxAB(Board board, int depth, boolean maxPlayer, double alpha, double beta)
  {
    if(depth == 0)
    {
      return board.heuristicEvaluation();
    }

    double maxEval = Double.NEGATIVE_INFINITY, minEval = Double.POSITIVE_INFINITY;
    double eval = 0;
    MOVE child = (MOVE) board.generateMoves();

    if(maxPlayer)
    {
      while(child != null)
      {
        board.makeMove(child);
        eval = recursiveMinimaxAB(board,depth-1,false, alpha, beta);
        board.reverseMove(child);
        maxEval = Math.max(maxEval,eval);
        alpha = Math.max(alpha,eval);
        if(beta <= alpha)
        {
          break;
        }
        child = (MOVE) child.next;
      }
      return maxEval;

    }
    else
    {
      while(child != null)
      {
        board.makeMove(child);
        eval = recursiveMinimaxAB(board,depth-1,true, alpha, beta);
        board.reverseMove(child);
        minEval = Math.min(minEval,eval);
        beta = Math.min(beta,eval);
        if(beta <= alpha)
        {
          break;
        }
        child = (MOVE) child.next;
      }
      return minEval;
    }

  }
}
