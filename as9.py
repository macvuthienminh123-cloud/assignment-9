def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count

def find_keyword_lines(filename, keyword):
    result = []
    with open(filename, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                result.append(i)
    return result

def average_score(filename):
    total = 0
    count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            name, score = line.strip().split(',')
            total += int(score)
            count += 1
    
    if count == 0:
        return 0
    return total / count

def caesar_cipher_file(input_file, shift, direction):
    if direction == "left":
        shift = -shift
    
    result = ""
    
    with open(input_file, 'r') as file:
        text = file.read()
        
        for c in text:
            if c.isupper():
                new_char = chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
                result += new_char
            elif c.islower():
                new_char = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                result += new_char
            else:
                result += c
    
    with open("cipher_output.txt", 'w') as file:
        file.write(result)