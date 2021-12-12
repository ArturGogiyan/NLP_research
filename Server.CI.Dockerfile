ARG pythonImage
ARG pythonSlimImage

FROM python:3.8 as builder

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM python:3.8-slim

ENV PATH=/root/.local:$PATH
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

EXPOSE 4242:4242

COPY --from=builder /root/.local /root/.local

WORKDIR /app
COPY Server/src/ ./

ENTRYPOINT ["python", "-u", "main.py"]