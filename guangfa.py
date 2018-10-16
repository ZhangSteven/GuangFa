# coding=utf-8
# 
# Convert files from GuangFa securities to other formats.
# 
# 1. Bloomberg upload trade file.
# 2. Geneva reconciliation file.
#


from os.path import join
import logging
logger = logging.getLogger(__name__)



def getTradeFiles(files):
	"""
	[list] txt files => [list] trade files
	"""
	return list(filter(lambda fn: 'trddata' in fn.split('\\')[-1], files))



def getTxtFiles(folder):
	"""
	[string] folder => [list] txt files in the folder
	"""
	from os import listdir
	from os.path import isfile

	logger.info('getTxtFiles(): folder {0}'.format(folder))

	def isTxtFile(file):
		"""
		[string] file name (without path) => [Bool] is it an Excel file?
		"""
		return file.split('.')[-1] == 'txt'

	return [join(folder, f) for f in listdir(folder) \
			if isfile(join(folder, f)) and isTxtFile(f)]





if __name__ == '__main__':
	from GuangFa.utility import get_current_path
	import logging.config
	logging.config.fileConfig('logging.config', disable_existing_loggers=False)

	tradeFiles = getTradeFiles(getTxtFiles(join(get_current_path(), 'samples', '20140129')))
	if len(tradeFiles) == 0:
		print('trade file not found')
	else:
		print('trade file: {0}'.format(tradeFiles[0]))


