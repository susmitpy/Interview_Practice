"""
Problem: Cash Register Software
Given the number of coins of each denomination and the value to be returned.
Decide the minimum number of coins that will be needed.
"""
# Greedy Approach

def min_coins(coins, value):
	min_num_coins = 0   
	for coin_val, num_coins in coins.items():
		if value < coin_val: 
			continue	# 0 coins will be needed of coin_val denomination
		num_coins_needed = value // coin_val  # Take only the integer quotient
		if num_coins_needed <= num_coins: # Sufficient num_coins available
			min_num_coins += num_coins_needed  
			value %= coin_val  # Remaining value 
		else:
			# Insufficient number of coins of coin_val denomination
			# Take what is there
			min_num_coins += num_coins
			value -= coin_val*num_coins # Remaining value
		if value < 1:
			break
	return min_num_coins

# 106 => 25:3, 10:3, 1:1

coins = {25:3,10:20,5:16,1:6}
print("Min Coins: ", min_coins(coins, 106))
# Returns 7 => 25:3, 10:3, 1:1
