import os

input_file = os.path.join('paragraph_1.txt')

output_file = os.path.join('results.txt')

with open(input_file, 'r') as file:

    # Store all of the content of the file inside a variable called `lines`
    lines = file.read()

    list_of_words = lines.split(" ")
    num_of_words = len(list_of_words)

    #get total number of characters in the paragraph
    letter_count = 0
    for word in list_of_words:
        letter_count = letter_count + len(word)
    avg_letter_count = letter_count/len(list_of_words)

    list_of_sentences = lines.split(".")
    num_of_sentences = len(list_of_sentences) - 1

    #split make the last list a blank item in the list so need to remove it.
    list_of_sentences.pop(num_of_sentences)
    
    #get total words per sentence
    words_per_sentence = 0
    for sentence in list_of_sentences:
        temp = sentence.split(" ")
        words_per_sentence = words_per_sentence + (len(temp))
    avg_words_per_sentence = words_per_sentence/len(list_of_sentences)

    print("Paragraph Analysis")
    print("-----------------")
    print("Approximate Word Count: " + str(num_of_words))
    print("Approximate Sentence Count: " + str(num_of_sentences))
    print("Average Letter Count: " + str('{0:.2f}'.format(avg_letter_count)))
    print("Average Sentence Length: " + str('{0:.2f}'.format(avg_words_per_sentence)))