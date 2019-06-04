FROM python:latest

# install scikit-build
RUN git clone https://github.com/scikit-build/scikit-build.git
WORKDIR /scikit-build
RUN python setup.py install

# pip dependencies
RUN pip install Cython
RUN pip install ninja

# Since this is a scikit-build, we need to set LD_LIBRARY_PATH to target
ENV LD_LIBRARY_PATH=/jigsawpy/_skbuild/linux-x86_64-3.7/cmake-install/jigsaw/lib:$LD_LIBRARY_PATH

# copy jigsawpy jigsawpy
RUN mkdir /jigsawpy
WORKDIR /jigsawpy
COPY . .

# init jigsaw submodule
RUN git submodule update --init

# install jigsawpy
RUN python setup.py install

# test jigsawpy
RUN python setup.py test