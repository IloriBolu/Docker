FROM node:20-slim

WORKDIR /app

ARG VERSION=1.0.0
ARG BUILD_DATE

LABEL version=$VERSION
LABEL maintainer="Bolu"
LABEL build_date=$BUILD_DATE

COPY package*.json ./

RUN npm install --omit=dev

COPY . .

ENV PORT=3000

EXPOSE 3000

CMD ["node", "server.js"]