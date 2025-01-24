import java.util.*;

public class water_java_BFS{

    static class State {
        int x, y;

        State(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static String waterJug(int m, int n, int d) {
        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new State(0, 0));
        visited.add("0,0");

        while (!queue.isEmpty()) {
            State state = queue.poll();
            int x = state.x;
            int y = state.y;
            System.out.println(x+"     "+y);
            if (x == d || y == d) {
                return "Found jug x=" + x + " and jug y=" + y;
            }

           
            List<State> nextStates = Arrays.asList(
                    new State(m, y),    
                    new State(x, n),    
                    new State(0, y),    
                    new State(x, 0),    
                    new State(x - Math.min(x, n - y), y + Math.min(x, n - y)), 
                    new State(x + Math.min(y, m - x), y - Math.min(y, m - x))  
            );

            for (State nextState : nextStates) {
                String stateStr = nextState.x + "," + nextState.y;
                if (!visited.contains(stateStr)) {
                    visited.add(stateStr);
                    queue.add(nextState);
                }
            }
        }

        return "No solution found";
    }

    public static void main(String[] args) {
        System.out.println(waterJug(5, 4, 2)); 
    }
}
