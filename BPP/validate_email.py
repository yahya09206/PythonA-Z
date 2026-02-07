def validate_email(email):

	# check if email has @ sign
	if '@' not in email:
		return False

	# split email into chars
	parts = email.split('@')

	# return true if both side have content
	if len(parts[0]) > 0 and len(parts[1]) > 0:
		return True


	# otherwise return false
	return False

print(validate_email("test@example.com"))  # Should print True
print(validate_email("invalid.com"))       # Should print False
print(validate_email("@example.com"))      # Should print False