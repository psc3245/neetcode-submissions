public class Solution {
    public int CalPoints(string[] operations) {
        Stack<int> stack = new Stack<int>();
        foreach (string op in operations) {
            if (int.TryParse(op, out int result)) {
                stack.Push(result);
            }
            else {
                if (op == "+") {
                    var right = stack.Pop();
                    var left = stack.Peek();
                    stack.Push(right);
                    stack.Push(left + right);
                }
                if (op == "C") {
                    stack.Pop();
                }
                if (op == "D") {
                    var left = stack.Peek();
                    stack.Push(2 * left);
                }
            }
        }
        var total = 0;
        while (stack.TryPop(out int result)) {
            total += result;
        }
        return total;
    }
}