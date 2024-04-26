ENV PYTHONBUFFERED True

ENV APP_HOME /back_end
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt      


CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout - app:app
