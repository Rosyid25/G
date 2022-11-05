import random 
import sys
import time
def mengetik(s):
   for c in s +  '\n':
	sys.stdout.write(c)
        sys.stdout.flush()

	time.sleep(random.random( ) * 0.3)

mengetik('jangan lupa subscribe chanel Youtube Mou Yt... \n')
mengetik('Dan Jangan Lupa Follow Tiktok Mou_Story... \nselamat menonton\nterimakasih.')
