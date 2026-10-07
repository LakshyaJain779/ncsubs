class Solution:

    def encode(self, strs: List[str]) -> str:
        s = str()
        for string in strs:
            s = s + "dnojfno3rgb" + string
        return s
    def decode(self, s: str) -> List[str]:
        return s.strip().split("dnojfno3rgb")[1:]
