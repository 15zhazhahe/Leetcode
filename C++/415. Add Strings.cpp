class Solution {
public:
    string addStrings(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int len = max(a.length(),b.length()), cnt = 0;
        string ans = "";
        for(int i=0;i<len;i++)
        {
            int tmp = i<a.length()?a[i]-'0':0;
            tmp += i<b.length()?b[i]-'0':0;
            tmp += cnt;
            ans += (char)(tmp%10+'0');
            cnt = tmp/10;
        }
        if(cnt) ans += '0'+cnt;
        reverse(ans.begin(), ans.end());
        return ans;
    }
};