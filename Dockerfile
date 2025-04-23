FROM python:3.10-alpine

WORKDIR /workspace

RUN apk add --no-cache gcc musl-dev libffi-dev

COPY . /workspace/

CMD ["python", "main.py"]
