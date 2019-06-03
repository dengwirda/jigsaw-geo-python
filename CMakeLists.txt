cmake_minimum_required (VERSION 3.9.4)
project (jigsawpy)

# build libjigsaw
set (CMAKE_CXX_STANDARD 11)
set (CMAKE_INTERPROCEDURAL_OPTIMIZATION TRUE)
add_library (jigsaw-lib SHARED "${CMAKE_CURRENT_SOURCE_DIR}/lib/jigsaw/src/jigsaw.cpp")
target_compile_definitions (jigsaw-lib PRIVATE __lib_jigsaw)
set_target_properties (jigsaw-lib PROPERTIES OUTPUT_NAME jigsaw)
install (TARGETS jigsaw-lib DESTINATION "${CMAKE_INSTALL_PREFIX}/jigsaw/lib")

# scikit-build
find_package(PythonExtensions REQUIRED)
python_extension_module(jigsaw-lib)
