# [![LOGO][logo-image]][logo-url]  **React Most Wanted** 
[![Build Status][travis-image]][travis-url] [![License][license-image]][license-url] [![Code Style][code-style-image]][code-style-url]

RMW is a set of features and best practices **that you can choose from** and use around your React projects, built on [Create React App](https://github.com/facebookincubator/create-react-app). You can check out the demo at [react-most-wanted.com](https://react-most-wanted.com).

The features include:
- **[Material UI](https://material-ui.com/)**: Material Design ready-to-use React Components
- **[Code splitting](https://webpack.js.org/guides/code-splitting/)**: MPA (Multiple Page Application) ready. A Large codebase can be split into separate bundles that load different parts of the application, lazy-loading the different bundles on demand.
- **[Redux](https://redux.js.org/)**: predictable state management, by enforcing a strict unidirectional data flow and state immutability.
- **[Firebase](https://firebase.google.com)**: use Firebase's platform as backend and database
- **And many more**: Firebase and Redux sync, authentication, authorization (roles and permissions), push notifications UI integration, theming, internationalization, built-in CI/CD, real-time forms...

To find out more about the features it includes, visit the [documentation page](https://www.react-most-wanted.com/docu/getting_started).

## How to start? 

To accommodate major use-cases, we have created three different shells that you can choose depending on your needs:  

**[Base shell](./packages/base-shell/)**:
the basic react setup: routing, internationalization and async load.

```npx create-react-app my-app --template base```

**[Material UI shell](./packages/material-ui-shell/)**:
includes all features from the base shell expanded with [Material-UI](https://material-ui.com).

```npx create-react-app my-app --template material-ui```


**[React Most Wanted shell](./packages/rmw-shell)**:
Base shell + Material UI shell + [Firebase](https://firebase.google.com/)

```npx create-react-app my-app --template rmw```

## Contributing

We appreciate **any** contribution! 

See [Contributing](./CONTRIBUTING.md) for details.

## HELP WANTED

If you want to contribute and don't know where to start. Here are some places you can start:
- Cool  [Landing Page](https://github.com/TarikHuber/react-most-wanted/blob/master/packages/rmw-shell-new/cra-template-rmw/template/src/pages/LandingPage/LandingPage.js) for new ```rmw-shell``` package. It is completely separated from the rest of the Application so you can make it as you want. Just make sure to have at least 95 speed points with [Lighthouse](https://developers.google.com/web/tools/lighthouse)
- Unit tests. Do I need to say anything about this?

## Thanks

[<img src="https://www.browserstack.com/images/mail/browserstack-logo-footer.png" width="120">](https://www.browserstack.com/)

Thank you to [BrowserStack](https://www.browserstack.com/) for providing the infrastructure that allows us to test in real browsers.


## License

This project uses [MIT license](https://github.com/TarikHuber/react-most-wanted/blob/master/LICENSE).


[logo-image]: https://www.react-most-wanted.com/favicon.ico
[logo-url]: https://www.react-most-wanted.com/favicon.ico
[travis-image]: https://travis-ci.org/TarikHuber/react-most-wanted.svg?branch=master
[travis-url]: https://travis-ci.org/TarikHuber/react-most-wanted
[license-image]: https://img.shields.io/npm/l/express.svg
[license-url]: https://github.com/TarikHuber/react-most-wanted/master/LICENSE
[code-style-image]: https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square
[code-style-url]: https://github.com/prettier/prettier
