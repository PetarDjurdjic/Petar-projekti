def k_universal_circular_string(k):
    # Generate the binary alphabet of length k
    alphabet = [format(i, '0' + str(k) + 'b') for i in range(2**k)]

    # Initialize the circular string with the first string in the alphabet
    circular_string = alphabet[0]

    # Helper function to find the next character to add to the circular string
    def find_next_char(current_suffix):
        for char in alphabet:
            next_suffix = current_suffix[1:] + char[-1]
            if next_suffix not in circular_string:
                return char[-1]
        return None  # Return None if no character is found

    # Build the circular string by adding characters one by one
    while len(circular_string) < 2**k:
        next_char = find_next_char(circular_string[-k + 1:])
        if next_char is not None:
            circular_string += next_char
        else:
            break  # Break the loop if no character is found

    return circular_string

# Example usage for k = 3
k_value = 3
result = k_universal_circular_string(k_value)
print(result)
