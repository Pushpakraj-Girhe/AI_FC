// missionaries_canni_Ai
import java.util.HashSet;
import java.util.Set;

public class missionaries_canni_Ai {

    static int missionariesLeft = 3, cannibalsLeft = 3;
    static int missionariesRight = 0, cannibalsRight = 0;
    static boolean boatOnLeft = true;

    static Set<String> visitedStates = new HashSet<>();

    public static void main(String[] args) {
        // Attempt to solve the problem
        if (!solve()) {
            System.out.println("No solution found.");
        }
    }

    // Try to solve the problem with DFS (backtracking)
    private static boolean solve() {
        // Print the current state of the game
        printState();

        // If all missionaries and cannibals have crossed the river, return true (solved)
        if (missionariesLeft == 0 && cannibalsLeft == 0) {
            System.out.println("All Missionaries and Cannibals have crossed the river!");
            return true;
        }

        // Explore all possible moves
        int[][] moves = {
            {1, 1},  // Move 1 missionary and 1 cannibal
            {2, 0},  // Move 2 missionaries
            {0, 2},  // Move 2 cannibals
            {1, 0},  // Move 1 missionary
            {0, 1}   // Move 1 cannibal
        };

        // Try all possible moves in a recursive DFS fashion
        for (int[] move : moves) {
            int m = move[0];
            int c = move[1];

            // Try making the move if it's valid and hasn't been visited
            if (isValidMove(m, c)) {
                makeMove(m, c);
                String currentState = getState();

                // Avoid revisiting the same state
                if (visitedStates.contains(currentState)) {
                    undoMove(m, c);
                    continue;  // Skip this move as it leads to a previously visited state
                }

                visitedStates.add(currentState);

                // Recursively try to solve from the new state
                if (solve()) {
                    return true;  // If the recursive call returns true, we've solved the puzzle
                }

                // Backtrack: undo the move if it didn't lead to a solution
                undoMove(m, c);
                visitedStates.remove(currentState);
            }
        }

        // No valid moves found, return false to indicate failure
        return false;
    }

    // Print the current state of the game
    private static void printState() {
        System.out.println("Left Bank: " + missionariesLeft + " Missionaries, " + cannibalsLeft + " Cannibals");
        System.out.println("Right Bank: " + missionariesRight + " Missionaries, " + cannibalsRight + " Cannibals");
        System.out.println("Boat is on the " + (boatOnLeft ? "Left" : "Right") + " Bank");
    }

    // Get the current state as a string (to check if we've visited it before)
    private static String getState() {
        return missionariesLeft + "," + cannibalsLeft + "," + missionariesRight + "," + cannibalsRight + "," + boatOnLeft;
    }

    // Check if the move is valid
    private static boolean isValidMove(int m, int c) {
        // The boat can only carry 1 or 2 people, either missionaries or cannibals or a combination.
        if (m + c > 2 || m < 0 || c < 0 || (m == 0 && c == 0)) {
            return false;
        }

        // If the boat is on the left bank, check if the move doesn't leave more cannibals than missionaries.
        if (boatOnLeft) {
            if (m > missionariesLeft || c > cannibalsLeft) return false; // Can't move more than available
            if ((missionariesLeft - m < cannibalsLeft - c && missionariesLeft - m > 0) || (missionariesLeft - m < 0) || (cannibalsLeft - c < 0)) {
                return false; // Invalid state after move (not enough missionaries/cannibals or leaves more cannibals than missionaries)
            }
        }
        // If the boat is on the right bank, check if the move doesn't leave more cannibals than missionaries.
        else {
            if (m > missionariesRight || c > cannibalsRight) return false; // Can't move more than available
            if ((missionariesRight - m < cannibalsRight - c && missionariesRight - m > 0) || (missionariesRight - m < 0) || (cannibalsRight - c < 0)) {
                return false; // Invalid state after move
            }
        }

        return true;
    }

    // Perform the move
    private static void makeMove(int m, int c) {
        if (boatOnLeft) {
            missionariesLeft -= m;
            cannibalsLeft -= c;
            missionariesRight += m;
            cannibalsRight += c;
        } else {
            missionariesRight -= m;
            cannibalsRight -= c;
            missionariesLeft += m;
            cannibalsLeft += c;
        }

        boatOnLeft = !boatOnLeft; // Toggle the boat's position
    }

    // Undo the move (used for backtracking)
    private static void undoMove(int m, int c) {
        if (boatOnLeft) {
            missionariesRight -= m;
            cannibalsRight -= c;
            missionariesLeft += m;
            cannibalsLeft += c;
        } else {
            missionariesLeft -= m;
            cannibalsLeft -= c;
            missionariesRight += m;
            cannibalsRight += c;
        }

        boatOnLeft = !boatOnLeft; // Toggle the boat's position
    }
}
