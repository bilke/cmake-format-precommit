from setuptools import setup
setup(
    name="cmakelang-precommit-dummy",
    version="0.0.0",
    install_requires=[
        # Includes fixes for FILE_SETS
        "cmakelang @ https://github.com/solarispika/cmake_format/releases/download/v0.6.13.2/cmakelang-0.6.13.2-py3-none-any.whl"
    ],
)
