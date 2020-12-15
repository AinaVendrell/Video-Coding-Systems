import inquirer
from transform import transform
from mosaic import mosaic
from streaming import streaming


menu = [
    inquirer.List('menu',
                  message='Choose an exercise',
                  choices=[
                      '1) Mosaic',
                      '2) Streaming',
                  ]
                  ),
]

size = [
    inquirer.List('size',
                  message='Choose a size',
                  choices=[
                      '720p',
                      '480p',
                      '360x240',
                      '160x120',
                  ]
                  ),
]

exercise = inquirer.prompt(menu)['menu']


if '1)' in exercise:
    size = inquirer.prompt(size)['size']
    output_files = transform(size)
    mosaic(output_files, size)

elif '2)' in exercise:
    streaming()
