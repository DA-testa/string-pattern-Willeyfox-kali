# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_file = input().rstrip()
    if input_file == "I":
        pattern = input().rstrip()
        text = input().rstrip()
    else:
        with open(input_file) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    return pattern, text
    # this is the sample return, notice the rstrip function
    # ####return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    ####return [0]
    p = 31
    m = len(pattern)
    n = len(text)
    p_kv = [1] * (n + 1)
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        p_kv[i] = p_kv[i - 1] * p
        h[i] = (h[i - 1] + ord(text[i - 1]) * p_kv[i - 1])

    pattern_hash = 0
    for i in range(m):
        pattern_hash += ord(pattern[i]) * p_kv[i]
    occurrences = []
    for i in range(n - m + 1):
        text_hash = h[i + m] - h[i]
        if text_hash == pattern_hash * p_kv[i]:
            occurrences.append(i)
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

