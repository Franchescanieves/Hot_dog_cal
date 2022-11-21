# Write a program that calculates the number of packages
# of hot dogs and the number of packages of hot dog buns needed for a cookout,
# with the minimum amount of leftovers.
# The program should ask the user for the number of people
# attending the cookout and the number of hot dogs each person will be given.
# Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.
# The program should display the following details:
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over

import math

# Declare hot dogs and buns
hotdog_packets = 10
bun_packets = 8

# Get the number of guest and how many hot dogs per quest.
number_of_guest = int(input('Enter the number of attending the cookout?' ))
hotdog_per_guest = int(input('Enter the number of hot dogs per guest:' ))

# Total number of hot dogs for the event
total = number_of_guest * hotdog_per_guest
print("Total number of hot dogs needed:", total)

# Number of hotdog packages required
hd_needed = total / hotdog_packets
print("Hotdog packets needed for this event:", math.ceil(hd_needed))

# Number of bun packages required
bun_needed = total / bun_packets
print("Bags of buns needed:", math.ceil(bun_needed))

# Calculate material used
hd_used = math.ceil(hd_needed) * hotdog_packets
print('Total number of hotdogs:', hd_used)
bun_used = math.ceil(bun_needed) * bun_packets
print('Total number of buns:', bun_used)

# Remaining hotdogs and buns
remaining_hotdogs = hd_used - total
print("Remaining hotdogs:", math.ceil(remaining_hotdogs))
remaining_buns = bun_used - total
print("Remaning buns:", math.ceil(remaining_buns))






















