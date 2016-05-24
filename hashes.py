from passlib.hash import sha256_crypt

hash_file = open("hashes_rounds=5000.txt", "w")


for i in range (1, 50001):
	hash_file.write(sha256_crypt.encrypt(str(i), salt="0123456789012345", rounds=5000)) #mijenjanje broja rundi i soli
	if (i < 50000):
		hash_file.write("\n")
