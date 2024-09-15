# and 
# 1 and 1 => 1
# 1 and 0 => 0
# 0 and 1 => 0
# 0 and 0 => 0

# or
# 1 or 1 => 1
# 1 or 0 => 1
# 0 or 1 => 1
# 0 or 0 => 0

# not 
# not 1 => 0
# not 0 => 1

written_test = "Pass"
driving_test = "Fail"

# Get Driving License when both tests pass
get_driving_license = written_test == 'Pass' and driving_test == 'Pass'
print(get_driving_license)

# Get Driving License if one of the test pass
get_driving_license = written_test == 'Pass' or driving_test == 'Pass'
print(get_driving_license)