def find_all_anagrams(s:str, p:str) -> List[int]:

	if len(p) > len(s):
		return []