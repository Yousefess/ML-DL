import shutil
import os

os.makedirs('/content/working/data')

os.makedirs('/content/working/data/train')
os.makedirs('/content/working/data/val')
os.makedirs('/content/working/data/test')

os.makedirs('/content/working/data/train/cats')
os.makedirs('/content/working/data/train/dogs')

os.makedirs('/content/working/data/val/cats')
os.makedirs('/content/working/data/val/dogs')

os.makedirs('/content/working/data/test/cats')
os.makedirs('/content/working/data/test/dogs')

os.makedirs('/content/working/model')


def move(source, dest, half=""):
  source_file_lst = os.listdir(source)

  if half == "left":
    source_file_lst = source_file_lst[:len(source_file_lst)//2]
  elif half == "right":
    source_file_lst = source_file_lst[len(source_file_lst)//2:]

  for f in source_file_lst:
    shutil.copy(source + f, dest)

  print(str(len(source_file_lst)) + " files copied from " + source + "to " + dest)


move('/content/data/training_set/training_set/dogs/',
     '/content/working/data/train/dogs')
move('/content/data/training_set/training_set/cats/',
     '/content/working/data/train/cats')

move('/content/data/test_set/test_set/dogs/',
     '/content/working/data/test/dogs', half='left')
move('/content/data/test_set/test_set/cats/',
     '/content/working/data/test/cats', half='left')

move('/content/data/test_set/test_set/dogs/',
     '/content/working/data/val/dogs', half='right')
move('/content/data/test_set/test_set/cats/',
     '/content/working/data/val/cats', half='right')
