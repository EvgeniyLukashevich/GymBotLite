import random

from aiogram.types import InputMedia

from data import content_file_read


class Unit:
    __photos_for_links = ['database/__materials/logo.png',
                          'database/__materials/logo1.jpg',
                          'database/__materials/logo2.jpg']
    __default_content_list = ['database/__materials/photo_default.png',
                              'database/__materials/video_default.mp4']
    __name = 'content_0'
    __content_id = random.choice(__default_content_list)
    if __content_id == __default_content_list[0]:
        __type = 'photo'
    else:
        __type = 'video'

    def __init__(self, user_id, content_name):
        if user_id is not None and content_name is not None:
            self.__name = content_name
            component_list = content_file_read(user_id=user_id,
                                               content_name=content_name)
            self.__type = component_list[0]
            self.__content_id = component_list[1]

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_content_address(self):
        return self.__content_id

    def get_content_standard(self):
        if self.__content_id in self.__default_content_list:
            return open(self.__content_id, 'rb')
        else:
            return self.__content_id

    def get_content_callback(self):
        if self.__type == 'photo':
            return InputMedia(type='photo',
                              media=self.get_content_standard(),
                              caption=f'{self.__name}: photo')
        elif self.__type == 'video':
            return InputMedia(type='video',
                              media=self.get_content_standard(),
                              caption=f'{self.__name}: video')
        else:
            if int(self.__name.replace('content_', '')) % 2 == 0:
                photo = self.__photos_for_links[0]
                return InputMedia(type='photo',
                                  media=open(photo, 'rb'),
                                  caption=f'{self.__name}: {self.__content_id}')
            else:
                photo = self.__photos_for_links[1]
                return InputMedia(type='photo',
                                  media=open(photo, 'rb'),
                                  caption=f'{self.__name}: {self.__content_id}')

    def get_photo_callback(self):
        return InputMedia(type='photo',
                          media=self.get_content_standard(),
                          caption=f'{self.__name}: photo')

    def get_video_callback(self):
        return InputMedia(type='video',
                          media=self.get_content_standard(),
                          caption=f'{self.__name}: video')
