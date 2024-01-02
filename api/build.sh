!/usr/bin/bash

apt update -y && apt upgrade -y && apt install -y --no-install-recommends binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal

echo "INSTALLING NIXXXXXXXXXXX"
nix-env -f . -iA binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal

echo "FOUND THE JSON"
find / -name libjson-c.so.5

cp -r /usr/lib/x86_64-linux-gnu/* /usr/lib
cp -r /usr/lib/x86_64-linux-gnu/* /nix/store/wprxx5zkkk13hpj6k1v6qadjylh3vq9m-gcc-11.3.0-lib/lib

echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "THIS IS $LD_LIBRARY_PATH"
echo "FOUND THE FILEPATH"
pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==$(gdal-config --version)
