total_inches = 10**12

(total_feet, inches) = divmod(total_inches, 12)
(total_yards, feet) = divmod(total_feet, 3)
(total_miles, yards) = divmod(total_yards, 1760)
(em_dist, miles) = divmod(total_miles, 238855)

fmt = "One trillion inches is the same as going to the moon and back %d times, plus an extra %d miles, %d yards, %d feet, and %d inches."
print(fmt % (em_dist, miles, yards, feet, inches))
