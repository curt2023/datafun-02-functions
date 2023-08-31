import statistics

data_a = [10,11,14,20,20,20,22,24,28,31]
data_b = [2,9,13,14,20,20,24,26,32,40]

mean_data_a = statistics.mean(data_a)
median_data_a = statistics.median(data_a)
mode_data_a = statistics.mode(data_a)

mean_data_b = statistics.mean(data_b)
median_data_b = statistics.median(data_b)
mode_data_b = statistics.mode(data_b)


print ("data_a mean =", mean_data_a)
print ("data_a median =", median_data_a)
print ("data_a mode =", mode_data_a)

print ("data_b mean =", mean_data_b)
print ("data_b median =", median_data_b)
print ("data_b mode =", mode_data_b)