class Solution:
    def frequencySort(self, s: str) -> str:
        a = Counter(s)
        stri = ""
        # sortA = sorted(a.elements())
        for ele,freq in a.most_common():
            stri += ele*freq
        return stri
        # return sortA