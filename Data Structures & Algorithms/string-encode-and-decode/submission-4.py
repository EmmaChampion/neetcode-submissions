class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "///empty///"
        encoded_str = ""
        for word in strs:
            add_to = f"/\\/\\{word}"
            encoded_str = encoded_str + add_to
        encoded_str = encoded_str[4:]
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "///empty///":
            return []
        pattern = r"/\\/\\"
        decoded_str = re.split(pattern, s)
        return decoded_str

















