import sys
import os
import subprocess
import numpy as np
import time

RUN_SCRIPT = 'run_video.py'
RANDOM_SEED = 42
RUN_TIME = 60 # sec  was: 280
ABR_ALGO = ['RL','fastMPC', 'robustMPC', 'BOLA']
#ABR_ALGO = ['RL']
REPEAT_TIME = 1  # was 10


def main():

	np.random.seed(RANDOM_SEED)

	with open('./chrome_retry_log', 'w') as log:
		log.write('chrome retry log\n')
		log.flush()

		for rt in range(REPEAT_TIME):
			np.random.shuffle(ABR_ALGO)
			for abr_algo in ABR_ALGO:
				print(f"DEBUG: *** working on ABR Algo: {abr_algo} ***")
				while True:
					print(f"DEBUG: rt: {rt} starting script...")
					start = time.perf_counter()
					script = '/usr/bin/python3.8 ' + RUN_SCRIPT + ' ' + \
							  abr_algo + ' ' + str(RUN_TIME) + ' ' + str(rt)
					
					proc = subprocess.Popen(script,
							  stdout=subprocess.PIPE, 
							  stderr=subprocess.PIPE, 
							  shell=True)
					print(f"DEBUG: rt: {rt} waiting on script")
					(out, err) = proc.communicate()
					end = time.perf_counter()
					#print(f'DEBUG: got output in {end - start:0.4f} seconds!')
					#print('out: {}\ntype(out): {}\nstr(out): {}\nstr(out.decode(utf-8): {}'.format(out, type(out), str(out), str(out.decode('utf-8'))))
					#print('err: {}'.format(err.decode('utf-8')))
					
					if str(out.decode('utf-8')) == '\ndone\n':
						print(f'DEBUG: *** rt: {rt} finished script in {end - start:0.4f} seconds! ***')
						break
					else:
						print(f"DEBUG: rt: {rt} failed, retrying script")
						log.write(abr_algo + '_' + str(rt) + '\n')
						log.write(out.decode('utf-8') + '\n')
						log.flush()
					



if __name__ == '__main__':
	main()
