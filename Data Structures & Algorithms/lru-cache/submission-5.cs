public class LRUCache {

    OrderedDictionary<int, int> cache;
    int capacity;

    public LRUCache(int capacity) {
        this.cache = new OrderedDictionary<int, int>();
        this.capacity = capacity;
    }
    
    public int Get(int key) {
        if (this.cache.TryGetValue(key, out int value)) {
            this.cache.Remove(key);
            this.cache.Insert(0, key, value);
            return value;
        }
        else {
            return -1;
        }
    }
    
    public void Put(int key, int value) {
        if (this.cache.ContainsKey(key)) {
            this.cache.Remove(key);
        }
        if (this.cache.Count == this.capacity) {
            this.cache.RemoveAt(this.capacity - 1);
        }
        this.cache.Insert(0, key, value);

    }
}
