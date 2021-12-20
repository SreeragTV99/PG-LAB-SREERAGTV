import statistics

# Calculate average values
print("Mean : ",statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print("Mean : ",statistics.mean([1, 3, 5, 7, 9, 11]))
print("Mean : ",statistics.mean([-11, 5.5, -3.4, 7.1, -9, 22]))

print("===============================")

# Calculate middle values
print("Median : ",statistics.median([1, 3, 5, 7, 9, 11, 13]))
print("Median : ",statistics.median([1, 3, 5, 7, 9, 11]))
print("Median : ",statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))


print("===============================")

# Calculate the mode
print("Mode :",statistics.mode([1, 3, 3, 3, 5, 7, 9, 11]))
print("Mode :",statistics.mode([1, 1, 3, -5, 7, -9, 11]))
print("Mode :",statistics.mode(['red', 'green', 'blue', 'red']))

print("===============================")

# Calculate the variance from a sample of data
print("Varience :",([1, 3, 5, 7, 9, 11]))
print("Varience :",statistics.variance([2, 2.5, 1.25, 3.1, 1.75, 2.8]))
print("Varience :",statistics.variance([-11, 5.5, -3.4, 7.1]))
print("Varience :",statistics.variance([1, 30, 50, 100]))

print("===============================")

# Calculate harmonic mean
print("Hermonic mean",statistics.harmonic_mean([40, 60, 80]))
print("Hermonic mean",statistics.harmonic_mean([10, 30, 50, 70, 90]))

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


