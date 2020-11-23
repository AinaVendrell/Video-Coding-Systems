import inquirer
from cut import cut
from histogram import histogram
from resize import resize
from mono import mono


menu = [
    inquirer.List('menu',
                  message='Choose an exercice',
                  choices=[
                      '1) Cut 10 seconds of the BBB video',
                      '2) Extract the YUV histogram of the 10 seconds BBB video',
                      '3) Resize the 10 seconds BBB video',
                      '4) Change the audio into mono and apply a different audio codec'
                  ]
                  ),
]

exercice = inquirer.prompt(menu)['menu']

if '1)' in exercice:
    print(
        'Define the time the trimmed video will start as mm:ss knowing that the maximun is 10:25')
    while 1:
        time = str(input())
        a = time.split(':')
        if int(a[0]) < 11 and int(a[1]) < 61:
            print('\nTime: ', time)
            cut(time)
            break
        else:
            print('Invalid option, choose another time')

elif '2)' in exercice:
    histogram()

elif '3)' in exercice:
    print('Define the width and height as (360x240) or the resolution as (720p)')
    while 1:
        size = str(input())
        if 'p' in size or 'x' in size:
            print('\nSize: ', size)
            resize(size)
            break
        else:
            print('Invalid option, choose another size')

elif '4)' in exercice:
    print('Which codec do you want to use?')
    codec = str(input())
    mono(codec)
