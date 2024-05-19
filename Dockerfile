FROM python:3.10-bullseye
COPY dist/* /dist/
RUN pip install /dist/*.whl
WORKDIR /usr/local/lib/python3.10/site-packages/backend1
EXPOSE 8000
CMD ["uvicorn", "main:app", "--root-path", "backend", "--host", "0.0.0.0", "--port", "8000"]