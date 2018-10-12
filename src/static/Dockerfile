FROM node:9.6.1
WORKDIR /root
ADD package.json package.json
RUN npm install
ADD . /root
CMD ["npm", "start"]