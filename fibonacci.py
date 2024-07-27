sequence = [0, 1]

#add to the tail of array the sum of two previous numbers
for i in sequence:
    if len(sequence) <= 15:  #cut off loop at 15 numbers
        seqSum = i + sequence[len(sequence)-1]  #add current number and last index of current iteration
        sequence.append(seqSum)
    else:
        break

print(sequence)