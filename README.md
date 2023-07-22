# django-tailwind

Django TailwindCSS integration template project

## Running the project (Docker)

Dev:
`docker compose -f docker-compose.dev.yml up`

Debug:
`docker compose -f docker-compose.debug.yml up`

## Initializing JS packages / TWCSS staticfiles

This application is configured for Heroku pre- and post-build hooks. To generate these assets locally, you can utilize the same commands from the top-level structure:

- `npm run heroku-prebuild` Builds the JS toolchain
- `npm run heroku-postbuild` Builds the TailwindCSS static files

### Creating TailwindCSS static files

To create staticfiles manually, from the `./jstoolchain` directory run:

`npx postcss styles.css -o compiled.css`

The application is configured to run the TWCSS compiler in `watch` mode. To watch for changes, from the top level directory run:

`npm run tailwind-watch --prefix ./jstoolchain`

When running the project with Docker, this watcher is pre-configured.
