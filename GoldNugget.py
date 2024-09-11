from os import path, mkdir, listdir, getcwd
from cv2 import imread, GaussianBlur, imwrite

print('\n')
#dir_path = path.dirname(path.realpath(__file__))
dir_path = getcwd()
input_dir = path.join(dir_path,'input')
output_dir = path.join(dir_path,'output')
if path.exists(output_dir):
    check_dir = True
else :
    check_dir = False
if check_dir == False :
    mkdir(output_dir)
if path.exists(input_dir):
    check_dir = True
else :
    check_dir = False
if check_dir == False :
    mkdir(input_dir)
print(dir_path)
print('\n',input_dir)
print('\n',output_dir)
print('\n','filename :','\n')
for filename in listdir(input_dir):
    print(filename,'\n')
print('\n','process :','\n')
for filename in listdir(input_dir):
    f = path.join(input_dir,filename)
    extension = path.splitext(f)
    if path.isfile(f):
        if '.png' in extension[1]:
            print(f,'\n')
            layer_X_X = imread(f)
            layer_X_X_blur = GaussianBlur(layer_X_X,(301,301),0)
            imwrite(path.join(output_dir,filename),layer_X_X_blur)
input("Press enter to exit;")