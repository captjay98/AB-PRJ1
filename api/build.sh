!/usr/bin/bash

apt update -y && apt upgrade -y && apt install -y --no-install-recommends binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal


echo "INSTALLING NIXXXXXXXXXXX"
nix-env -f . -iA binutils libstdc++6 libheif-dev libheif1 poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal

# , 'binutils', 'libstdc++6', 'libheif-dev', 'libheif1', 'poppler-utils', 'libjson-c-dev', 'libproj-dev', 'gdal-bin', 'libgdal-dev', 'python3-gdal'
#ldconfig
echo "FOUND THE JSON"
find / -name  libjson-c.so.5

#echo "THIS IS $LD_LIBRARY_PATH"
echo "!!!!!!!!!!!!!!!!!!!"

# cp /usr/lib/x86_64-linux-gnu/libpoppler.so.118 /usr/lib

# cp  /usr/lib/x86_64-linux-gnu/libheif.so.1 /usr/lib

# cp  /usr/lib/x86_64-linux-gnu/libjson-c.so.5 /usr/lib

# cp  /usr/lib/x86_64-linux-gnu/libfreexl.so.1 /usr/lib

# cp  /usr/lib/x86_64-linux-gnu/libqhull_r.so.8.0 /usr/lib

cp  -r /usr/lib/x86_64-linux-gnu/* /usr/lib

echo "!!!!!!!!!!!!!!!!!!!!!!"
echo "THIS IS $LD_LIBRARY_PATH"
echo "FOUND THE FILEPATH"
pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`

# export LD_LIBRARY_PATH 
# nix-env -iA nixpkgs.libheif
# export LD_LIBRARY_PATH=/path/to/libheif/libs:$LD_LIBRARY_PATH
# echo "What is going onnnn"
# LD_LIBRARY_PATH=/nix/store/wprxx5zkkk13hpj6k1v6qadjylh3vq9m-gcc-11.3.0-lib/lib:/nix/store/zaflwh2nwzj1f0wngd7hqm3nvlf3yhsx-zlib-1.2.13/lib:/usr/lib


# pip install -r requirements.txt
# python manage.py collectstatic --no-input

# python manage.py makemigrations core
# python manage.py migrate core

# python manage.py makemigrations users
# python manage.py migrate users

# python manage.py makemigrations seekers
# python manage.py migrate seekers

# python manage.py makemigrations employers
# python manage.py migrate employers

# python manage.py makemigrations
# python manage.py migrate

