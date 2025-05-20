from setuptools import setup, find_packages

setup(
    name="lang2segtrack",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "opencv-python",
        "numpy",
        "imageio",
        "imageio-ffmpeg",
    ],
    author="wngkj",
    author_email="unknown@someemail.com",
    description="Language-driven visual segmentation and object tracking system based on Grounding-DINO and SAMURAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/frank-Regal/Lang2SegTrack",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)