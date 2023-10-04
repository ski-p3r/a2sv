import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z]', '', s)
        return (st.lower() == st.lower()[::-1]) 