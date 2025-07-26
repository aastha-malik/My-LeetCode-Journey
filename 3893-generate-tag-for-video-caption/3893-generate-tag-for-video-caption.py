class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip()
        arr = caption.split(" ")
        for i in range(1, len(arr)):
            arr[i] = arr[i].capitalize()
            
        arr[0] = arr[0].lower()
        s = "".join(arr)
        res = "#" + s[:99]
        return res

        