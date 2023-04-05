import pandas as pd


def freqword(filepath):
    with open(filepath) as file:
        counts = dic()
        for line in file:
            words = line.split()
            for words in words:
                counts[word] = counts.get(word,0) + 1
        maxcount = None
        maxword = None
        for word, count in counts.item():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count

        return(f"The most frequent word is: {maxword}, and then number of times appeared is: {maxcount}")
    freqword('._iso.txt')
    print()

df = pd.DataFrame(
    {
        'a':[1,2,3],
        'b':[4,5,6],
    },
    index = ['c', 'd', 'e']
)
print(df)

"""
Week 5 Consultation Questions
Practice with reading & writing files
"""


def append_to_file(pth, line):
    """Appends the new line to the file located at pth

    Parameters
    ----------
    pth : str
        Full path of the file to write to.

    line: str
        New line to be appended to the file

    """
    # <COMPLETE THIS PART>


def replace_line_words(line, new_words):
    """
    Replace the words of `line` that are among the keys
    of the `new_words` dictionary with their corresponding values

    Parameters
    ----------
    line : str
        String to be modified

    new_words: dict
        Dictionary of the format {<old_word> : <new_word>} where
            - <old_word> is a word within `line` that should be replaced
            - <new_word> is the word that <old_word> should be replaced with within `line`

    Notes
    -----
    For example, given:
    new_words = {'hello' : 'bye}
    line = 'Hello there hello'

    This function should return
    'Bye there bye'

    Returns
    -------
    str
        A copy of `line` but with its words replaced based on `new_words`

    """
    # <COMPLETE THIS PART>


def create_modified_file(old_file_pth, new_file_pth, new_words):
    """
    Create a new file called `new_file_pth` that is the exact same as
    `old_file_pth`, but with its words replaced according to the `new_words` dictionary.
    Words not found in the `new_words` dictionary should be left unchanged.

    Parameters
    ----------
        old_file_pth: str
            Path of the original file

        new_file_pth: str
            Path of new file created containing replaced words

        new_words: dict
            Dictionary of the form {<old_word> : <new_word>}

    Notes
    -----
    The text in `old_file_pth` should be left unmodified.

    """
    # <COMPLETE THIS PART>


if __name__ == "__main__":
    # ori_file = 'lyrics.txt'
    # new_file = 'modified_lyrics.txt'
    # words_replacement = {
    #     'life': 'new_life',
    #     'no': 'new_no',
    #     'open': 'new_open',
    #     'me': 'new_me',
    # }
    #
    # create_modified_file(ori_file, new_file, words_replacement)

    pass


contents = """Volume:
column position: 1
dtype: int64
width: 14

Date:
column position: 2
dtype: datetime64
width: 11

Adj Close:
column position: 3
dtype: float64
width: 19

Close:
column position: 4
dtype: float64
width: 10

Open:
column position: 5
dtype: float64
width: 6

High:
column position: 6
dtype: float64
width: 20"""


col = contents.split('\n',)
print(col)
Col = contents.split('\n')[-29].split(':')[0]
date = contents.split('\n')[-24].split(':')[0]

adj = contents.split('\n')[-19].split(':')[0]

close = contents.split('\n')[-14].split(':')[0]

open  = contents.split('\n')[-9].split(':')[0]

high = contents.split('\n')[-4].split(':')[0]

COL = [Col,date,adj,close,open,high]

print(col)


COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']


COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}

#with open("README.txt",'r') as r:
    #x = r.read()


#def get_tics(pth):
    #with open(pth,'r') as f:
      #  x = f.read()
