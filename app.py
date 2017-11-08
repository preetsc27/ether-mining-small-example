# for milli seconds
import time

# for current date and time
from time import gmtime, strftime

# for encryption
import hashlib

# current date and time
data = strftime("%Y-%m-%d %H:%M:%S", gmtime())

# function to solve a bloack chain simple contract example
def solvePuzzle(blockdata, difficultyPrefix):
	nonce = "NOT-Found"
	start = time.time()
	end = start

	# for loop to find a solution
	for tryNonce in range(100000000):

		# converting to string and concating
		# both the vars to make a combination
		y = str(blockdata) + str(tryNonce)

		# changing the encoding to utf-8 so that it can be digested
		encoded_y = y.encode('utf-8')

		# now making the hex
		sha = hashlib.sha256(encoded_y).hexdigest()

		# now cheking if we found the combination
		if sha.startswith(difficultyPrefix):
			end = time.time()
			nonce = tryNonce
			print(sha)
			break

	#checking the time taken
	time_taken = end - start
	print(end, start)
	if time_taken == 0:
		print("Difficulty=", difficultyPrefix, " Nonce not found!!!")
	else:
		print("Difficulty=", difficultyPrefix," Time(ms)=", time_taken, " Nonce=", nonce,  " Hash=", sha)
solvePuzzle(data, "0")
solvePuzzle(data, "00")
solvePuzzle(data, "000")
solvePuzzle(data, "0000")
solvePuzzle(data, "000000")

