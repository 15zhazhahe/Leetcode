// Time:  O(n)
// Space: O(1)
class Solution {
public:
    bool judgeCircle(string moves) {
        int len = moves.length();
        int x = 0, y = 0;
        for(int i=0;i<len;i++)
        {
            if(moves[i]=='U')
                y++;
            else if(moves[i]=='D')
                y--;
            else if(moves[i]=='L')
                x--;
            else
                x++;
        }
        if(x==y && x==0)
            return true;
        else
            return false;
    }
};