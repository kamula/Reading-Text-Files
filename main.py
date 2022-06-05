# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file_contents = None
    # read file contents an return them as a String
    with open(filename) as f:
        file_contents = f.read()
        f.close()
    return file_contents


def count_words():
    text = read_file_content("./story.txt")
    text_list = text.split(" ")
    # [assignment] Add your code here
    # print(text.split(' '))
    dict_count = {e:text_list.count(e) for e in set(text_list)}
    

    return dict_count

count_words()