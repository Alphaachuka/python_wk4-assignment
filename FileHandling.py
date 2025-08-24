# interactive file read and write

#step 1: Ask user for input and output file names
input_file = input("Enter the name of the file to read from (e.g., input.txt): ")
output_file = input("Enter the name of the file to write to (e.g., output.txt): ") 

#step 2: Read from the input file

try:
    with open(input_file, 'r') as infile:
        content = infile.read()
except FileNotFoundError:
    print("❌File not found. Please check the file name and try again.")
    exit()
except IOError:
    print("❌An error occurred while reading the file.")
    exit()
    
# step 3: Ask user how they want to modify text

print("\nChoose a modification option:")
print("1. Convert to UPPERCASE")
print("2. Convert to lowercase")
print("3. Replace a word")
print("4. Add line numbers")
print("5. Add extra sentences")

choice = input("Enter your choice (1-5): ")

if choice == '1':
    modified_content = content.upper() 
elif choice == '2':
    modified_content = content.lower()
elif choice == '3':
    word_to_replace = input("Enter the word to replace: ")
    replacement_word = input("Enter the replacement word: ")
    modified_content = content.replace(word_to_replace, replacement_word)
elif choice == '4':
    lines = content.splitlines()
    modified_content = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(lines))
elif choice == '5':
    print("Enter sentences to add (type 'DONE' when finished):" )
    extra_sentences = []
    while True:
        sentence = input(">")
        if sentence.upper() == 'DONE':
            break
        extra_sentences.append(sentence)
    modified_content = content + '\n' + '\n'.join(extra_sentences)
else:
    print("❌Invalid choice. No modifications made.")
    exit()
    
# step 4: Write to the output file

with open(output_file, 'w') as outfile:
    outfile.write(modified_content)
print(f"✅Modified content written to {output_file}")