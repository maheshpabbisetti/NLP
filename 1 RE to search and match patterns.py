import re

# Define the text we want to search
text = "The quick brown fox jumps over the lazy dog."

# Define the regular expression pattern we want to match
pattern = r"\b\w{4}\b"

# Use the re.findall function to search for matches of the pattern in the text
matches = re.findall(pattern, text)

# Print the matches
print("Matches: ", matches)

# Define a new pattern to search for words that start with the letter 'j'
pattern = r"\bj\w*\b"

# Use the re.finditer function to search for matches of the pattern in the text
matches = re.finditer(pattern, text)

# Print the start and end indices and the matched string for each match
print("Matches:")
for match in matches:
    print(f"Start: {match.start()}, End: {match.end()}, Match: {match.group()}")
