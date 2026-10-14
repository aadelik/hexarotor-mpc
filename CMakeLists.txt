cmake_minimum_required(VERSION 3.10)
project(HexarotorMPC)

# Use max optimization for accurate timing
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")

find_package(Eigen3 REQUIRED)
find_package(OsqpEigen REQUIRED)

add_executable(hex_mpc main.cpp)
target_link_libraries(hex_mpc Eigen3::Eigen OsqpEigen::OsqpEigen)

add_executable(mpc_sensitivity sensitivity.cpp)
target_link_libraries(mpc_sensitivity OsqpEigen::OsqpEigen)