public class Solution {
    public int[][] KClosest(int[][] points, int k) {
        PriorityQueue<(int, int), double> q = new PriorityQueue<(int, int), double>();

        foreach (int[] point in points) {
            var x = point[0];
            var y = point[1];
            double dist = Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2));
            q.Enqueue((x, y), dist);
        }

        var ret = new int[k][];

        for (int i = 0; i < k; i++) {
            var deq = q.Dequeue();
            ret[i] = [deq.Item1, deq.Item2];
        }

        return ret;
    }
}
