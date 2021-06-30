from setuptools import find_packages, setup

setup(
    name="yolov5",
    version="0.0.1",
    packages=find_packages(exclude=("train",)),
    url="https://github.com/monkvision/yolov5",
    author="Ultralytics",
    install_requires=[
        "Cython>=0.29.14",
        "numpy>=1.18.5",
        "opencv-python>=4.1.2",  # "opencv_python_headless>=4.1.2.30",
        # "torch>=1.5.1",
        "easydict>=1.9",
        "matplotlib>=3.1.2",
        "Pillow>=7.0.0",
        "tensorboard",
        "PyYAML",
        # "torchvision>=0.4.2",
        "scipy>=1.3.3",
        "tqdm>=4.40.0",
    ],
)
