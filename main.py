import matplotlib.pyplot as plt

def read_text_file(file_path):
    """
    Reads a text file and returns its content as a string.
    
    :param file_path: Path to the text file.
    :return: Content of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: The file '{file_path}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"
    
# create a function to convert the text to lowercase and remove punctuation.
def process_text(text):
    """
    Processes the text by converting it to lowercase and removing punctuation.
    
    :param text: Input text as a string.
    :return: List of words from the processed text.
    """
    import string
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize the text into words
    words = text.split()
    return words

# Count the frequency of each unique word in words
def count_word_frequencies(words):
    """
    Counts the frequency of each unique word in a list of words.
    
    :param words: List of words.
    :return: Dictionary with words as keys and their frequencies as values.
    """
    word_frequencies = {}
    for word in words:
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    return word_frequencies

# create a function to plot out the top n words on a graph with matplotlib
def plot_top_n_words(word_frequencies, n=10):
    """
    Plots the top n words by frequency using matplotlib.
    
    :param word_frequencies: Dictionary with words as keys and their frequencies as values.
    :param n: Number of top words to display.
    """

    # Sort the word frequencies by frequency
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

    # Get the top n words and their frequencies
    top_n_words = sorted_words[:n]
    words, frequencies = zip(*top_n_words)

    # Create a bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(words, frequencies, color='skyblue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {n} Words by Frequency')
    plt.xticks(rotation=45)
    plt.show()

# Main function to read a file, process the text, count word frequencies, and plot the top words
def main(file_path, top_n=10):
    """
    Main function to read a file, process the text, count word frequencies, and plot the top words.
    
    :param file_path: Path to the text file.
    :param top_n: Number of top words to display in the plot.
    """
    # Read the text file
    content = read_text_file(file_path)
    
    if "Error" in content:
        print(content)
        return
    
    # Process the text
    words = process_text(content)
    
    # Count word frequencies
    word_frequencies = count_word_frequencies(words)
    
    # Plot the top n words
    plot_top_n_words(word_frequencies, top_n)

# Execute the main method if this file is run as a script
if __name__ == "__main__":
    import sys
    
    # Check if the file path is provided as a command line argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <file_path> [top_n]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    top_n = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    
    # Call the main function with the provided file path and top_n
    main(file_path, top_n)