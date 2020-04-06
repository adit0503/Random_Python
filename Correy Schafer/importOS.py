import os
for datetime import datetime

print(os.getcwd()) #/home/spc/Desktop/random_python/Correy Schafer

os.chdir("/home/spc/Desktop/")
print(os.getcwd()) #/home/spc/Desktop/

os.listdir()
# ['flask_dev',
#  'Resume_Flask-Heroku',
#  'webpage_dev',
#  'Data_visualization',
#  'Resume_Netlify',
#  'virtual_env',
#  'random_python',
#  'leetcode-ctci',
#  'Deploy-ML',
#  'NLP']

os.mkdir('abc.txt')
os.listdir()
# ['flask_dev',
#  'Resume_Flask-Heroku',
#  'webpage_dev',
#  'Data_visualization',
#  'Resume_Netlify',
#  'virtual_env',
#  'abc.txt',
#  'random_python',
#  'leetcode-ctci',
#  'Deploy-ML',
#  'NLP']
os.stat('abc.txt')
# os.stat_result(st_mode=16893, st_ino=28313131, st_dev=66306, st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime=1586177566, st_mtime=1586177566, st_ctime=1586177566)
os.rename('abc.txt','cba.txt')
os.listdir()
# ['flask_dev',
#  'Resume_Flask-Heroku',
#  'webpage_dev',
#  'Data_visualization',
#  'Resume_Netlify',
#  'virtual_env',
#  'random_python',
#  'leetcode-ctci',
#  'cba.txt',
#  'Deploy-ML',
#  'NLP']
os.stat('cba.txt')
# os.stat_result(st_mode=16893, st_ino=28313131, st_dev=66306, st_nlink=2, st_uid=1000, st_gid=1000, st_size=4096, st_atime=1586177740, st_mtime=1586177566, st_ctime=1586177740)

os.rmdir('abc')
