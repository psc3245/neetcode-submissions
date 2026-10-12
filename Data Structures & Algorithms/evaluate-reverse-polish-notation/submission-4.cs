public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> s = new Stack<int>();
        foreach (var t in tokens) {
            if (t == "+") {
                var r = s.Pop();
                var l = s.Pop();
                s.Push(l + r);
            }
            else if (t == "-") {
                var r = s.Pop();
                var l = s.Pop();
                s.Push(l - r);
            }
            else if (t == "*") {
                var r = s.Pop();
                var l = s.Pop();
                s.Push(l * r);
            }
            else if (t == "/") {
                var r = s.Pop();
                var l = s.Pop();
                s.Push(l / r);
            }
            else {
                s.Push(int.Parse(t));
            }
        }
        return s.Pop();
    }
}
