class Solution:
    def build_frequency_dict(self, s):
        """
        Returns a dictionary with character frequencies of the string.
        """
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        return freq

    def isAnagram(self, s: str, t: str) -> bool:
        return self.build_frequency_dict(s) == self.build_frequency_dict(t)



        