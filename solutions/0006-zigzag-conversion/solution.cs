public class Solution {
    public string Convert(string s, int numRows) {
        int loopLength =  numRows * 2 - 2;

        var rows = new string[numRows];
        for (int i = 0; i < numRows; i++) {
            string row = "";

            int j = i;
            bool directionDown = true;
            while (j < s.Length) {
                row += s[j];

                int increment = 0;
                if (directionDown) {
                    increment = loopLength - (i * 2);
                    if (increment <= 0) {
                        increment = i * 2;
                    }
                } else {
                    increment = i * 2;
                    if (increment <= 0) {
                        increment = loopLength - (i * 2);
                    }
                }

                if (increment <= 0) {
                    increment = 1;
                }

                j += increment;

                directionDown = !directionDown;
            }

            rows[i] = row;
        }

        string result = "";
        foreach (string row in rows) {
            result += row;
        }

        return result;
    }
}
