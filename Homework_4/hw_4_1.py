'''
Task 1

Условия задачи:
Основной класс:

Создай базовый класс Device с атрибутами name (название устройства) и power_status (состояние устройства: включено/выключено).
Добавь методы turn_on() и turn_off() для управления состоянием устройства.
Миксины:

AudioMixin: добавляет метод play_audio(track), который выводит: "Воспроизведение аудио: {track}".
VideoMixin: добавляет метод play_video(video), который выводит: "Воспроизведение видео: {video}".
InternetMixin: добавляет метод connect_to_internet(), который выводит: "Подключено к интернету".
Подклассы устройств:

Radio: наследует Device и миксин AudioMixin (может только воспроизводить аудио).
TV: наследует Device и миксины VideoMixin и AudioMixin (может воспроизводить аудио и видео).
SmartDevice: наследует Device и миксины AudioMixin, VideoMixin, InternetMixin (может всё: воспроизводить аудио, видео и подключаться к интернету).
Задание:

Создай объекты для каждого типа устройства.
Попробуй включить/выключить устройства, воспроизвести аудио и видео, подключиться к интернету (если это возможно для устройства).
Используй список, чтобы объединить устройства, и вызови методы, доступные для каждого из них.

'''


class Device:
    def __init__(self, name: str):
        self.name = name
        self.power_status = 'off'

    def turn_on(self):
        self.power_status = 'on'
        print(f'Device {self.name} is: {self.power_status}')

    def turn_off(self):
        self.power_status = 'off'
        print(f'Device {self.name} is: {self.power_status}')


class AudioMixin:
    def play_audio(self, track: str):
        print(f'Playing audio: {track}')


class VideoMixin:
    def play_video(self, video: str):
        print(f'Playing video: {video}')


class InternetMixin:
    def connect_to_internet(self):
        print('Connected to the internet')


class Radio(Device, AudioMixin):
    pass


class Tv(Device, VideoMixin, AudioMixin):
    pass


class SmartDevice(Device, AudioMixin, VideoMixin, InternetMixin):
    pass


radio = Radio("Радио FM")
tv = Tv("Телевизор Samsung")
smart_device = SmartDevice("Смарт-колонка Alexa")

radio.turn_on()
radio.play_audio("Jazz FM")

tv.turn_on()
tv.play_audio("Реклама")
tv.play_video("Новости")

smart_device.turn_on()
smart_device.play_audio("Плейлист Spotify")
smart_device.play_video("YouTube")
smart_device.connect_to_internet()

