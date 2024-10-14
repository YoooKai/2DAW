# Proceso de despliegue de páginas 

`npm init -y`

`npm install -d parcel-bundler`

`npx parcel src/index.html`

`npm install -D gh-pages`

`npm run build`

`npm run deploy`

```json
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "start": "parcel serve -d dist src/index.html",
    "build": "parcel build -d build --public-url /lol/ src/index.html",
    "deploy": "gh-pages -d build"
  },
```