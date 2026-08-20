public class Solution {
    public int[][] IntervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> intervals = new List<int[]>();

        var firstPointer = 0;
        var secondPointer = 0;

        while (firstPointer < firstList.Length && secondPointer < secondList.Length) {
            var fStart = firstList[firstPointer][0];
            var fEnd = firstList[firstPointer][1];

            var sStart = secondList[secondPointer][0];
            var sEnd = secondList[secondPointer][1];

            var start = Math.Max(fStart, sStart);
            var end = Math.Min(fEnd, sEnd);

            if (start <= end) {
                intervals.Add([start, end]);
            }

            if (fEnd < sEnd) firstPointer ++;
            else secondPointer ++;
        }

        return intervals.ToArray();
    }
}