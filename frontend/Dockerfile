FROM node:18-slim

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Create React App dev server listens on port 3000
EXPOSE 3000

# Use the existing "start" script instead of a non-existent "dev" script
CMD ["npm", "start"]
