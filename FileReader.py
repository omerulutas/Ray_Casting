import json
import os
import sys
from camera.OrthographicCamera import OrthographicCamera
from object.Sphere import Sphere


# JsonReader class is used for reading data from json file and create objects
class JsonReader:

    def __init__(self, fileName):
        # Firstly we need to hand root directory
        fn = getattr(sys.modules['__main__'], '__file__')
        self.root_path = os.path.abspath(os.path.dirname(fn))
        self.data = json  #
        self.get_json_object(fileName)

    # returns full file path
    def get_file_path(self, file):
        return self.root_path + '\\' + file

    # get_json_object create json objects from .json file
    # and than return objects
    def get_json_object(self, file):
        file_path = self.get_file_path(file)
        with open(file_path) as data_file:
            json_data = json.load(data_file)
            self.data = json_data

    # orthographic_camera_factory function is a orthographic camera factory
    # creates orthographic camera by using necessary parameters
    def orthographic_camera_factory(self):
        orthographic_camera = self.data['orthocamera']
        center = orthographic_camera['center']
        direction = orthographic_camera['direction']
        up = orthographic_camera['up']
        size = int(orthographic_camera['size'])
        return OrthographicCamera(center, direction, up, size)

    # background_factory creates background color by using json file item
    def background_factory(self):
        return tuple(self.data['background']['color'])

    # group_factory function creates object list and return the created list
    def group_factory(self):
        group = self.data['group']
        item_list = []

        for item in group:
            sphere = item['sphere']
            center = sphere['center']
            radius = float(sphere['radius'])
            color = tuple(sphere['color'])

            sphere = Sphere(color, radius, center)
            item_list.append(sphere)

        return item_list
