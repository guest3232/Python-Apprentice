"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']


# Create a story using the words in the list
story = [words[0],words[2],words[7],words[9],words[7],words[13],words[6],words[7],words[12],words[5],words[7],words[1],words[11],words[16],words[7],words[3],words[14],words[18],]
story_a=[words[19].title(),words[15],words[10],words[8],words[4],words[10],words[17],words[6],words[8],words[18],]
words[0].title()

# Display the story to the user
print(' '.join(story))
print(' '.join(story_a))