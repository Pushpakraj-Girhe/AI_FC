import java.util.*;

public class water_java_BFS{

    static class WaterJugState {
        int x, y;

        WaterJugState(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (obj == null || getClass() != obj.getClass()) return false;
            WaterJugState that = (WaterJugState) obj;
            return x == that.x && y == that.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
    }

    public static String waterJug(int m, int n, int d) {
        // Helper DFS method
        return dfs(0, 0, m, n, d, new HashSet<>());
    }

    private static String dfs(int x, int y, int m, int n, int d, Set<WaterJugState> visited) {
        // If the target amount of water is found in either jug
        if (x == d || y == d) {
            return "Found jug x=" + x + " and jug y=" + y;
        }

        // Try all possible actions
        List<WaterJugState> nextStates = Arrays.asList(
                new WaterJugState(m, y),  // Fill jug x completely
                new WaterJugState(x, n),  // Fill jug y completely
                new WaterJugState(0, y),  // Empty jug x
                new WaterJugState(x, 0),  // Empty jug y
                new WaterJugState(x - Math.min(x, n - y), y + Math.min(x, n - y)),  // Pour from jug x to jug y
                new WaterJugState(x + Math.min(y, m - x), y - Math.min(y, m - x))   // Pour from jug y to jug x
        );

        for (WaterJugState state : nextStates) {
            if (!visited.contains(state)) {
                visited.add(state);
                String result = dfs(state.x, state.y, m, n, d, visited);
                if (result != null) {  // If a solution is found, return it
                    return result;
                }
            }
        }

        return null;  // No solution found in this branch
    }

    public static void main(String[] args) {
        System.out.println(waterJug(5, 4, 2)); // Example: 5L and 4L jug, target = 2L
    }
}
