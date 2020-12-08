import inquirer
from classContainer import Container

menu = [
    inquirer.List('menu',
                  message='Choose an exercise',
                  choices=[
                      '1) Create example Container',
                      '2) Create custom Container',
                      '3) Check Broadcasting Standards',
                      '4) Create container and check Broadcasting Standards',
                  ]
                  ),
]

if __name__ == "__main__":
    container = Container()
    exercise = inquirer.prompt(menu)['menu']

    if '1)' in exercise:
        data = {
            'name': 'example',
            'duration': '01:00',
            'size': '720p',
            'video_codec': 'h264',
            'audio_codec': 'mp3',
            'bitrate': '94',
        }
        file_path = container.createContainer(data)
        print("\n\nThe container had been stored at:\n", file_path)

    elif '2)' in exercise:
        while(1):
            data = container.menuCreateContainer()
            if(data):
                file_path = container.createContainer(data)
                print("\n\nThe container had been stored at:\n", file_path)
                break

    elif '3)' in exercise:
        print('Enter the path of the container')
        input_file = str(input())
        container.checkBroadcastingStandard(input_file)

    elif '4)' in exercise:
        while(1):
            data = container.menuCreateContainer()
            if(data):
                input_file = container.createContainer(data)
                container.checkBroadcastingStandard(input_file)
                break
