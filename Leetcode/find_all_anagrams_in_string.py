def find_all_anagrams(s:str, p:str) -> List[int]:

	if len(p) > len(s):
		return []


	p_count = {}
	s_count = {}

	for char in p:
		p_count[char] = p_count.get(char, 0) + 1


	result = []
	left = 0

	for right in range(len(s)):

		incoming_char = s[right]


		s_count[incoming_char] = s_count.get(incoming_char, 0) + 1

		if (right - left + 1) > len(p):

			outgoing_char = s[left]


			s_count[outgoing_char] -= 1

			if s_count[outgoing_char] == 0:
				del s_count[outgoing_char]

			left += 1

		if s_count == p_count:
			result.append(left)


	return result
