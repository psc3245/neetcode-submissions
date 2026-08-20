public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int color) {
        HashSet<(int, int)> seen = new HashSet<(int, int)>();

        dfs(image, sr, sc, seen, color, image[sr][sc]);

        return image;
    }
    public void dfs(int[][] image, int row, int col, HashSet<(int, int)> seen, int color, int orig) {
        seen.Add((row, col));
        if (row + 1 < image.Length && !seen.Contains((row + 1, col))) {
            if (orig == image[row+1][col]) {
                dfs(image, row + 1, col, seen, color, orig);
            }
        }
        if (row - 1 > -1  && !seen.Contains((row - 1, col))) {
            if (orig == image[row - 1][col]) {
                dfs(image, row - 1, col, seen, color, orig);
            }
        }
        if (col + 1 < image[0].Length  && !seen.Contains((row, col + 1))) {
            if (orig == image[row][col + 1]) {
                dfs(image, row, col + 1, seen, color, orig);
            }
        }
        if (col - 1 > -1  && !seen.Contains((row, col - 1))) {
            if (orig == image[row][col - 1]) {
                dfs(image, row, col - 1, seen, color, orig);
            }
        }
        image[row][col] = color;
    }
}