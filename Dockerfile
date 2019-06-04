FROM jigsawpy/01:latest
RUN pip install nose
COPY . .
RUN python setup.py install
# RUN python setup.py test
RUN Jigsaw
# RUN nosetests tests/test_cjigsaw.py
