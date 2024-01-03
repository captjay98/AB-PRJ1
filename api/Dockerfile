FROM python:3.9
RUN apt update -y && apt install -y --no-install-recommends binutils libstdc++6 libheif-dev libheif1 \
  poppler-utils libjson-c-dev libproj-dev gdal-bin libgdal-dev python3-gdal
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==$(gdal-config --version)
COPY . .
EXPOSE 8000
# RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "api.wsgi:application"]

