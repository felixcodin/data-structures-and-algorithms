#Time complexity: O(m * n) || Space complexity: O(m)

from collections import defaultdict

def groupAnagrams(strs):
    res = defaultdict(list) #create hash map stores `list` key value
    for s in strs:
        count = [0] * 26 #create a list containing the number of each character
        for c in s:
            count[ord(c) - ord('a')] += 1 #count the number of letter from a to z
        res[tuple(count)].append(s) #convert `count` list into a tuple and used as a key in the dictionary `res`. Add string `s` to the list res[tuple(count)] (with the same "fingerprint")
    return list(res.values())

test_case_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(test_case_1))
test_case_2 = ["x"]
print(groupAnagrams(test_case_2))
test_case_3 = [""]
print(groupAnagrams(test_case_3))