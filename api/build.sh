!/usr/bin/bash

apt update -y && apt upgrade -y && apt install -y --no-install-recommends binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal

nix-env -f . -iA binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal

cp  -r /usr/lib/x86_64-linux-gnu/* /usr/lib

cp  -r /usr/lib/x86_64-linux-gnu/* 

pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`
