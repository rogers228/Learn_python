import logging

if True: # log
	logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y/%m/%d %H:%M',
                    handlers = [logging.FileHandler('my.log', 'w', 'utf-8'),])
	console = logging.StreamHandler()
	console.setLevel(logging.INFO) # 等級
	formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s') #格式
	console.setFormatter(formatter)
	logging.getLogger('').addHandler(console)

def main():
	# root 輸出
	logging.debug('天高地遠')
	logging.info('天龍地虎')
	logging.warning('天發殺機')
	logging.error('地動天搖')

if __name__ == '__main__':
    main()