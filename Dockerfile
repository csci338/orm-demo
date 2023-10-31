from node:lts
# FROM node:lts-bookworm-slim
COPY ./src/ui /ui
WORKDIR /ui
RUN npm run build


from python:3.11
COPY ./src /app
COPY --from=0 /ui/dist /app/ui/dist
WORKDIR /app
RUN pip install poetry
RUN poetry install 
# RUN poetry run python populate.py -- can't happen until after DB is built
