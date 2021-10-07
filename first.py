#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla
import random
import time


def main():
	actor_list = []
	try:
		client = carla.Client('localhost',2000)
		client.set_timeout(10.0)
		world = client.load_world('Town02')

		blueprintLibrary = world.get_blueprint_library()
		vehicle_bp = blueprintLibrary.filter('cybertruck')[0]
		transform = carla.Transform(carla.Location(x=130,y=195,z=40),carla.Rotation(yaw=180))
		vehicle = world.spawn_actor(vehicle_bp,transform)
		actor_list.append(vehicle)

		# camera_bp = blueprintLibrary.find('sensor.camera.rgb')
		# camera_bp.set_attribute('image_size_x','800')
		# camera_bp.set_attribute('image_size_y','600')
		# camera_bp.set_attribute('fov','90')
		# camera_transform = carla.Transform(carla.Location(x=1.5,z=2.4))
		# camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
		# camera.listen(lambda image: image.save_to_disk('output/%d064.png'%image.frame))

		# transform.rotation.yaw=-180
		# for _ in range(0,1000):
		# 	transform.location.z+=8.0
		# 	bp = blueprintLibrary.filter('vehicle.*')[0]
		# 	npc = world.try_spawn_actor(bp,transform)

		# 	if npc is not None:
		# 		actor_list.append(npc)
		# 		npc.set_autopilot = True
		# 		print('created%s'%npc.type_id)

		time.sleep(15)

	finally:
		print("delete actor_list")
		client.apply_batch([carla.command.DestroyActor(x) for x in actor_list])


if __name__ == '__main__':
    main()
