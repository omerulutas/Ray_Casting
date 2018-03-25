from PIL import Image
from Hit import Hit
from FileReader import JsonReader


class Driver:

    # When we want to show any thing we need a few things
    # so we need scene frame, background color, camera and objects
    # this funtion carries above needs
    def getScene(self, pScene):
        scene = pScene + '.json'
        file_reader = JsonReader(scene)
        orthographic_cam = file_reader.orthographic_camera_factory()
        color = file_reader.background_factory()
        group = file_reader.group_factory()
        hit = Hit(0, [0, 0, 0])

        frame_size = (1024, 1024)
        image = Image.new('RGB', frame_size, color)
        image_depth = Image.new('RGB', frame_size, color)

        near = 15
        far = 25

        # for each pixel
        for y in range(frame_size[0]):
            for x in range(frame_size[1]):
                ray = orthographic_cam.generate_ray(1.0 * x / frame_size[0], 1.0 * y / frame_size[1])

                distance = 1000000
                col = (0, 0, 0)
                col_dep = (0, 0, 0)
                for s in group:

                    is_hit = s.intersect(ray, hit, 1)

                    if is_hit:
                        if distance > hit.t:
                            distance = hit.t
                            col = hit.color
                            depth = (far - hit.t) / (far - near)
                            cc = (int(depth * 255))
                            col_dep = (cc, cc, cc)

                image.putpixel((y, x), col)
                image_depth.putpixel((y, x), col_dep)

        # this section is working for colored images
        image.show()
        image.save(pScene + ".jpg")
        image.close()

        # this section is working for uncolored images
        image_depth.show()
        image_depth.save(pScene + "_depth.jpg")
        image_depth.close()


# this function is main function of the system
def main():
    d = Driver()
    scenes = ['scene\\scene1', 'scene\\scene2']
    for file in scenes:
        d.getScene(file)


main()
