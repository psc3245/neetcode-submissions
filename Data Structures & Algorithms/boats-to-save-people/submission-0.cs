public class Solution {
    public int NumRescueBoats(int[] people, int limit) {

        int l = 0;
        int r = people.Length - 1;

        Array.Sort(people);

        int boats = 0;

        while (l < r) {
            if (people[l] + people[r] <= limit) {
                l ++;
                r --;
            }
            else {
                r --;
            }
            boats ++;
        }

        return l == r ? boats + 1 : boats;
    }
}