def ransom_note(ransomNote:str, magazine:str) -> bool:

	if len(ransomNote) > len(magazine):
		return False


	magazine_counts = {}


	for char in magazine:
		magazine_counts[char] = magazine_counts.get(char, 0) + 1

	
	for char in ransomNote:
		if char not in magazine_counts or magazine_counts[char] == 0:
			return False
		else:
			magazine_counts[char] = magazine_counts.get(char, 0) - 1


	return True