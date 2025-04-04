# Usar a imagem oficial do Node.js para build
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./

RUN npm install --force

COPY . .

RUN npm run build

# Usar a imagem do Nginx para servir os arquivos estáticos
FROM nginx:alpine

# Copiar os arquivos construídos para a pasta padrão do Nginx
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]