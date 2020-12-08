import inquirer
from resize import resize
from transcode import transcode
from info import getData
from rename import rename


menu = [
    inquirer.List('menu',
                  message='Choose an exercise',
                  choices=[
                      '1) Get data from BBB video',
                      '2) Rename video',
                      '3) Resize input',
                      '4) Transcode input into an output with another codec'
                  ]
                  ),
]

exercise = inquirer.prompt(menu)['menu']


if '1)' in exercise:
    getData()

elif '2)' in exercise:
    print('Enter the path of the file you want to rename:')
    input_file = str(input())
    print('\nEnter the new name:')
    new_name = str(input())
    rename(input_file, new_name)

elif '3)' in exercise:
    print('Enter the path of the input you want to resize:')
    input_file = str(input())
    print('\nDefine the width and height as (360x240) or the resolution as (720p):')
    while 1:
        size = str(input())
        if 'p' in size or 'x' in size:
            print('\nSize: ', size)
            resize(size, input_file)
            break
        else:
            print('Invalid option, choose another size')

elif '4)' in exercise:
    print('Video codec MPEG2, audio codec ACC')
    transcode()
