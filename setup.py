#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# Add here console scripts and other entry points in ini-style format
# entry_points = """
# ;[console_scripts]
# ;#mysql-replicate = db_replication.main:run
# """


def setup_package():
    setup(
        name="db_replication",
        version='0.0.1',
        description="mysql replication to kafka",
        platforms=['Any'],
        packages=['db_replication'],
        include_package_data=True,
        zip_safe=False
    )


if __name__ == "__main__":
    setup_package()
