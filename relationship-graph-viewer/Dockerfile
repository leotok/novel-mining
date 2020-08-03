FROM node:13.12.0-alpine

WORKDIR /app/
ADD relationship-graph-viewer/package.json package.json

RUN yarn
RUN yarn add react-scripts@3.4.1 -g --silent

ADD ./relationship-graph-viewer .

ENV HOST=0.0.0.0
ENV POST=3000
ENV DANGEROUSLY_DISABLE_HOST_CHECK=true

EXPOSE 3000

CMD yarn start
