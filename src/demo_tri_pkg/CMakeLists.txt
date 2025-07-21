cmake_minimum_required(VERSION 3.5)
project(demo_tri_pkg)

find_package(ament_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

ament_package()
