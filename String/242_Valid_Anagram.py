class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for sym in s:
            if sym in map:
                map[sym] += 1
                continue
            map[sym] = 1
        for sym in t:
            if sym in map:
                map[sym] -= 1
                continue
            return False
        if set(map.values()) == {0}:
            return True
        return False




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for sym in s:
            if sym in map:
                map[sym] += 1
                continue
            map[sym] = 1
        for sym in t:
            if sym in map:
                map[sym] -= 1
                continue
            return False
        for sym in map:
            if map[sym] == 0:
                continue
            return False
        return True
