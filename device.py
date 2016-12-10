#This is where the protocol will play out, we will call all relevant functions here and simulate Alice/Bob communication and attacker interception in this script

import math
import random
import hashlib

def device_protocol():

	def __init__(self):
		self.p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
		self.g = 2
		#device chooses the exponents
		self.a = 1
		self.b = 1
		print "--------------------------------------------------"
		print "Public large prime p ",p, " and generator ",g, " generated."
		print "--------------------------------------------------"
		self.H = hashlib.sha256()
		print "Using Hash algorithm SHA256..."
		print "--------------------------------------------------"	
		self.prg = random.SystemRandom()
		self.t = prg.randrange(2)
		self.W = 3 # or 1 or something.. we can test different values
		self.Y = 1 #public key
		
	def get_new_keys():
		t = prg.randrange(2); #this is 0.. ?
		z = pow(g,((c1-W*t)%(p-1)),p)*pow(Y,((-a*c1-b)%(p-1)),p);
		H.update(b'ttt');
		c2 = H.hexdigest(); #get hash from int to int
		m2 = pow(g, int(c2, 16),p);
		print "--------------------------------------------------"
		print "Sending message 2: m2 is :", m2
		print "--------------------------------------------------"
		return c1, m1, t, z, c2, m2

	
	def get_generator():
		return 2

	def get_alice_exp():
		return a

	def get_bob_exp():
		return b

	def encrypt(self, usage_number):
		if usage_number == 1:
				self.c1 = prg.randrange(p-1)+1
				m = pow(g, c1, p) #m1
		else:
				m = 1
				self.z = pow(g,c1-W*t,p)*pow(Y,-a*c1-b, p)
				#self.H.update("stuff")
				#self.c2 = H.hexdigest();
				#^placeholder until H is fixed
				#m = pow(g, int(c2, 16), p)
		return m

