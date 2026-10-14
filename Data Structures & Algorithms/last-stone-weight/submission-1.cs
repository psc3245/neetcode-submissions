public class Solution {
    public int LastStoneWeight(int[] stones) {
        PriorityQueue<int, int> p = new PriorityQueue<int, int>();
        foreach (var s in stones) {
            p.Enqueue(s, -s);
        }

        while (p.Count > 1) {
            var l = p.Dequeue();
            var r = p.Dequeue();
            if (l != r) {
                p.Enqueue(Math.Abs(l - r), -Math.Abs(l - r));
            }
        }

        return p.Count == 0 ? 0 : p.Dequeue();

    }
}
