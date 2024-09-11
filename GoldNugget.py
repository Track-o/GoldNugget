import os
import cv2

print('\n')
#dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.getcwd()
input_dir = os.path.join(dir_path,'input')
output_dir = os.path.join(dir_path,'output')
if os.path.exists(output_dir):
    check_dir = True
else :
    check_dir = False
if check_dir == False :
    os.mkdir(output_dir)
if os.path.exists(input_dir):
    check_dir = True
else :
    check_dir = False
if check_dir == False :
    os.mkdir(input_dir)
print(dir_path)
print('\n',input_dir)
print('\n',output_dir)

print('\n','filename :','\n')
for filename in os.listdir(input_dir):
    print(filename,'\n')

print('\n','process :','\n')
for filename in os.listdir(input_dir):
    f = os.path.join(input_dir,filename)
    extension = os.path.splitext(f)
    if os.path.isfile(f):
        if '.png' in extension[1]:
            print(f,'\n')
            layer_X_X = cv2.imread(f)
            layer_resize = cv2.resize(layer_X_X,(1024*8,1024*8),fx=1.0,fy=1.0)
            layer_X_X_blur = cv2.GaussianBlur(layer_resize,(301,301),0)
            cv2.imwrite(os.path.join(output_dir,filename),layer_X_X_blur)
input("Press enter to exit;")
