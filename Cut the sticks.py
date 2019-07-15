def cut_stick(length):
    result = []
    while length:
        result.append(len(length))
        m = min(length)

        new_length = []

        for i in range (len(length)):
            length[i] -= m

            if length[i] != 0:
                new_length.append(length[i])

        length = new_length

    return result            

    
