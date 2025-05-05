# A quick python file to convert Josh Fitz's Typst notes to Anki flashcards
# Should I be revising instead of writing this? Yes.


input_file = "in.txt"

# If argument is passed, use that as input file
import sys
import os
if len(sys.argv) > 1:
    # Check if the argument is a file
    if not os.path.isfile(sys.argv[1]):
        print(f"Error: {sys.argv[1]} is not a file")
        print("Usage: python typstToAnki.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    print(f"Using {input_file} as input file")

output_file = "out.txt"

# Clear output file
with open(output_file, "w") as f:
    f.write("")


with open(input_file, "r") as f:
    lines = f.readlines()
    # Change to one massive string
    text = "".join(lines)
    
    splitted = text.split("#pagebreak()")

    print(f'Split into {len(splitted)}')
    
    for i in range(int(len(splitted)/2)):
        question = splitted[i*2]
        answer = splitted[i*2 + 1]
        
        if("*" not in question):
            print(f"Missing * in question {i} ({question})")
        if("*"  in answer):      
            print(f"* in answer {i} ({answer})")      
            
        
        
        # Remove bold from question
        question = question.replace("*", "")
        answer = answer.replace("*", "")
        # Remove last new line from question
        question = question.rstrip("\n")
        # Remove last new line from answer
        answer = answer.rstrip("\n")

        # Remove starting new line from question
        question = question.lstrip("\n")
        # Remove starting new line from answer
        answer = answer.lstrip("\n")
        
        # Remove semicolon from question
        question = question.replace(";", "")
        # Remove semicolon from answer
        answer = answer.replace(";", "")
        
        
        # Remove any quotation marks
        question = question.replace('"', "'")
        answer = answer.replace('"', "'")
        
        with open(output_file, "a") as f:
            f.write(f'"{question}";"{answer}"\n')
           
print(f'Wrote {len(splitted)/2} cards to {output_file}')