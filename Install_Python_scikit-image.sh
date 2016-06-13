#!/bin/bash
# bootstrapping script
# tested via: virtualenv fresh && source fresh/bin/activate
if [ -f /usr/local/bin/brew ];
then
    echo "homebrew found!"
else
    echo "installing homebrew . . ."
    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
fi

# need mercurial to get latest pyglet
brew install hg

# pip?
easy_install pip

# need a special pyglet
pip install hg+https://pyglet.googlecode.com/hg/

# install my special brand of nodebox
pip install git+https://github.com/jsundram/nodebox-opengl

# numpy
pip install numpy

#scipy
brew install gfortran
pip install scipy

# scikit-image (requires scipy)
pip install Cython
pip install PIL
pip install scikit-image
