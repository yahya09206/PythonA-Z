def group_anagrams(strs:List[str]) -> List[List[strs]]:

	groups = {}

	for words in strs:

		sorted_word = ''.join(sorted(words))

		if sorted_word not in groups:
			groups[sorted_word] = []

		groups[sorted_word].append(words)


	return list(groups.values())


