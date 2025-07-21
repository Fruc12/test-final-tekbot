import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/lory/TEST_4_TEKBOT/ros2_ws/install/demo_tri_pkg'
