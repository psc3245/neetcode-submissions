public class KthLargest {

    private PriorityQueue<int, int> priq;
    int max_size;

    public KthLargest(int k, int[] nums) {
        priq = new PriorityQueue<int, int>();
        foreach (int n in nums) {
            priq.Enqueue(n, n);
            while (priq.Count > k) {
                priq.Dequeue();
            }
        }
        this.max_size = k;
    }
    
    public int Add(int val) {
        priq.Enqueue(val, val);
        while (priq.Count > max_size) {
            priq.Dequeue();
        }
        return priq.Peek();
    }
}
