import java.util.Scanner;

public class missionaries {

    static int missionariesLeft = 3, cannibalsLeft = 3;
    static int missionariesRight = 0, cannibalsRight = 0;
    static boolean boatOnLeft = true;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (missionariesLeft > 0 || cannibalsLeft > 0) {
            System.out.println("\nCurrent state:");
            printState();

            if (missionariesLeft == 0 && cannibalsLeft == 0) {
                System.out.println("All Missionaries and Cannibals have crossed the river!");
                break;
            }

            System.out.println("\nEnter the number of missionaries and cannibals to move (format: M C):");
            int m = scanner.nextInt();
            int c = scanner.nextInt();

            if (isValidMove(m, c)) {
                makeMove(m, c);
            } else {
                System.out.println("Invalid move. Please try again.");
            }
        }

        scanner.close();
    }

    // Print the current state of the game
    private static void printState() {
        System.out.println("Left Bank: " + missionariesLeft + " Missionaries, " + cannibalsLeft + " Cannibals");
        System.out.println("Right Bank: " + missionariesRight + " Missionaries, " + cannibalsRight + " Cannibals");
        System.out.println("Boat is on the " + (boatOnLeft ? "Left" : "Right") + " Bank");
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
            if (missionariesLeft - m < cannibalsLeft - c && missionariesLeft - m > 0) return false; // Invalid state after move
        }
        // If the boat is on the right bank, check if the move doesn't leave more cannibals than missionaries.
        else {
            if (m > missionariesRight || c > cannibalsRight) return false; // Can't move more than available
            if (missionariesRight - m < cannibalsRight - c && missionariesRight - m > 0) return false; // Invalid state after move
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
}
