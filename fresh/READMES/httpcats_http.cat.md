#  http.cat [![Build Status](https://travis-ci.com/httpcats/http.cat.svg?branch=master)](https://travis-ci.com/httpcats/http.cat)

![HTTP Cat picture](https://http.cat/204)

## About

This is the website that is hosted at [https://http.cat](https://http.cat).

The code for the older version hosted at the heroku platform is at the [http-status-cats-api](https://github.com/rogeriopvl/http-status-cats-api) repo.

This version does not need any server side code. The API behavior is provided by a Nginx server config.

The interface is built with React and pre-rendered with react-snap.

## Development

    yarn start

Starts the development server.

    yarn test

Runs the tests.

    yarn build

Creates a build of the project.

## Adding a new image

Currently not all HTTP status codes are covered. You are welcome to create an issue or PR to cover them.

We've prepared some templates to make this process easier.

* [Landscape template](https://docs.google.com/presentation/d/1sYxNNKxUbP11kyt9oPixWdFEykHDafr4jixy9uwMh9I/edit?usp=sharing)
* [Portrait template](https://docs.google.com/presentation/d/1Ay5nattHagPfnd-gMaUHumckFt2VANaYwMkXuQ-xS6E/edit?usp=sharing)

You can clone it, replace the information with the new one and export as a JPG image.

Then, upload it to both `public/images` and `public/images-original` folders and update the [statuses.js](https://github.com/httpcats/http.cat/blob/master/src/lib/statuses.js) file.

## Credits

Thanks to [@girliemac](https://github.com/girliemac) for creating the amazing http status cats images.

Thanks to [@pfdborges](https://github.com/pfdborges) for creating the http.cat logo.

Thanks to [@nataly-enne](https://github.com/nataly-enne) for the status 501 image.

Thanks to [@woutfeys](https://github.com/woutfeys) for the status 102 image.

Thanks to [@epitaciosilva](https://github.com/epitaciosilva) for the 407 image.

Thanks to [@luizcieslak](https://github.com/luizcieslak) for the 203 image and 407 image fix.

## License

MIT
