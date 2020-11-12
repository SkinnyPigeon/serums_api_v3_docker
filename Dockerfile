FROM skinnypigeon/serums-start
EXPOSE 5000:5000
COPY /code /code/
COPY /code/config/config.json /etc/config.json
COPY /code/entrypoint/start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh
ENV PGPASSWORD=serums1234
ENV PGPORT=5432
ENV PGUSER=postgres
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENTRYPOINT ["/usr/local/bin/start.sh"]