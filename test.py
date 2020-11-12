#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : test.py
# @Author : yfor
# @Mail   : xxxx@mail.com
# @Date   : 2020/11/10 14:52:22
# @Docs   : test
'''

import os
import Augmentor

if __name__ == "__main__":

    source_directory = u'D:\mywork\work\git\myselfwork\DataAug_testdata'
    output_directory = u'D:\mywork\work\git\myselfwork\DataAug_testdata_output'
    p = Augmentor.Pipeline(source_directory, output_directory)
    # p.rotate(0.5, 10, 10)
    # p.rotate_without_crop(0.5, 20, 20)
    # p.flip_top_bottom(0.5)
    # p.flip_left_right(0.5)
    p.random_distortion(1.0, 5, 15, 3)
    # p.gaussian_distortion(1.0, 20, 20, 5, 'bell', 'out')
    # p.zoom(0.5, 0.8, 1.2)
    # p.zoom_random(0.5, 0.8)
    # p.crop_by_size(0.5, 360, 360)
    # p.crop_centre(0.5, 0.8)
    # p.crop_random(0.5, 0.8)
    # p.histogram_equalisation(0.5)
    # p.scale(0.5, 1.1)
    # p.resize(0.5, 480, 480)
    # p.skew_left_right(0.5, 1)
    # p.skew_top_bottom(0.5, 1)
    # p.shear(0.5, 5, 5)
    # p.greyscale(0.5)
    # p.black_and_white(0.5)
    # p.invert(0.5)
    # p.random_brightness(0.5, 0.1, 0.9)
    # p.random_color(0.5, 0.1, 0.9)
    # p.random_contrast(0.5, 0.1, 0.9)
    # p.random_erasing(1.0, 0.1)
    p.quality(1.0, -1)

    # for augmentor_image in p.augmentor_images:
    #     p._execute(augmentor_image)

    # p.sample(10)
    p.increase(5)
