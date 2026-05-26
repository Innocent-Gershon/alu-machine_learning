#!/usr/bin/env python3
"""
0-neural_style.py
"""
import numpy as np
import tensorflow as tf


class NST:
    """
    Neural Style Transfer class
    """

    style_layers = [
        'block1_conv1',
        'block2_conv1',
        'block3_conv1',
        'block4_conv1',
        'block5_conv1'
    ]

    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image,
                 alpha=1e4, beta=1):
        """
        Class constructor
        """

        # Validate style_image
        if (not isinstance(style_image, np.ndarray) or
                len(style_image.shape) != 3 or
                style_image.shape[2] != 3):
            raise TypeError(
                "style_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        # Validate content_image
        if (not isinstance(content_image, np.ndarray) or
                len(content_image.shape) != 3 or
                content_image.shape[2] != 3):
            raise TypeError(
                "content_image must be a numpy.ndarray with shape (h, w, 3)"
            )

        # Validate alpha
        if (not isinstance(alpha, (int, float)) or alpha < 0):
            raise TypeError(
                "alpha must be a non-negative number"
            )

        # Validate beta
        if (not isinstance(beta, (int, float)) or beta < 0):
            raise TypeError(
                "beta must be a non-negative number"
            )

        # Enable eager execution
        tf.compat.v1.enable_eager_execution()

        # Set instance attributes
        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta

    @staticmethod
    def scale_image(image):
        """
        Rescales an image such that its pixels values are between 0 and 1
        and its largest side is 512 pixels
        """

        # Validate image
        if (not isinstance(image, np.ndarray) or
                len(image.shape) != 3 or
                image.shape[2] != 3):
            raise TypeError(
                "image must be a numpy.ndarray with shape (h, w, 3)"
            )

        h, w, _ = image.shape

        # Compute new dimensions
        max_dim = 512

        if h > w:
            new_h = max_dim
            new_w = int((w / h) * max_dim)
        else:
            new_w = max_dim
            new_h = int((h / w) * max_dim)

        # Resize image using bicubic interpolation
        resized = tf.image.resize(
            image,
            (new_h, new_w),
            method=tf.image.ResizeMethod.BICUBIC
        )

        # Scale pixel values to [0, 1]
        resized = resized / 255.0

        # Clip values to ensure range [0, 1]
        resized = tf.clip_by_value(resized, 0.0, 1.0)

        # Add batch dimension
        resized = tf.expand_dims(resized, axis=0)

        return resized
