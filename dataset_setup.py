import os
from shutil import move, rmtree
from random import shuffle

path = "Tensorflow/workspace/images"
dirs = os.listdir(path)
train_dir = os.path.join(path, 'train')
test_dir = os.path.join(path, 'test')
os.mkdir(train_dir)
os.mkdir(test_dir)

for files in dirs:
    filepath = os.path.join(path, files)
    jpg = []
    xml = []
    for file in os.listdir(filepath):
        if file.endswith('jpg'):
            jpg.append(file)
        if file.endswith('xml'):
            xml.append(file)

    jpg, xml = sorted(jpg), sorted(xml)
    for i in range(len(jpg)):
        if jpg[i][:-3] != xml[i][:-3]:
            print(files)

    SPLIT = 0.9
    SIZE = len(jpg)
    split_range = int(SPLIT*SIZE)
    shuffle(jpg)
    training_set = jpg[:split_range]
    test_set = jpg[split_range:]
    for training_file in training_set:
        move(os.path.join(filepath, training_file),
             os.path.join(train_dir, training_file))
        move(os.path.join(filepath, training_file[:-3]+'xml'),
             os.path.join(train_dir, training_file[:-3]+'xml'))

    for test_file in test_set:
        move(os.path.join(filepath, test_file),
             os.path.join(test_dir, test_file))
        move(os.path.join(
            filepath, test_file[:-3]+'xml'), os.path.join(test_dir, test_file[:-3]+'xml'))

    rmtree(filepath)
