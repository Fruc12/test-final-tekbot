from setuptools import setup

package_name = 'demo_tri_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/demo_tri_pkg']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lory',
    maintainer_email='votremail@example.com',
    description='Demo de tri ROS2',
    license='MIT',
    entry_points={
        'console_scripts': [
            'demo_tri = demo_tri_pkg.demo_tri:main',
        ],
    },
)
