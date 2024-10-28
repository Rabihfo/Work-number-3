def generate_recaman_sequence(n):
    # Initialize the sequence and a set to keep track of the elements
    sequence = [0]
    seen = {0}
    
    # Generate the sequence up to the nth element
    for k in range(1, n):
        prev = sequence[-1]
        candidate = prev - k
        
        # Check if candidate is valid
        if candidate > 0 and candidate not in seen:
            sequence.append(candidate)
            seen.add(candidate)
        else:
            # If candidate is invalid, add k instead
            candidate = prev + k
            sequence.append(candidate)
            seen.add(candidate)
    
    return sequence

if __name__ == "__main__":
    # Input: Length of the Recamán sequence
    sequence_length = int(input().strip())
    
    # Output: Generated Recamán sequence (formatted as required by the autograder)
    recaman_sequence = generate_recaman_sequence(sequence_length)
    print(recaman_sequence)
