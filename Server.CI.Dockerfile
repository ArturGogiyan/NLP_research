ARG pythonImage
ARG pythonSlimImage

FROM $pythonImage as builder

COPY requirements.txt .
RUN pip install --user -r requirements.txt

FROM $pythonSlimImage

ENV PATH=/root/.local:$PATH
ENV FLASK_ENV=development
ENV FLASK_DEBUG=0

COPY --from=builder /root/.local /root/.local
RUN pip install 'dvc[s3]'

WORKDIR /app
COPY Server/src/ ./
COPY common/ ./common/

ENTRYPOINT ["python", "-u", "main.py"]