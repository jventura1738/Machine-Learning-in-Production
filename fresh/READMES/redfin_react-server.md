# React Server is now defunct

Consider [Next.js](https://nextjs.org/) instead.

## React Server

[![Build Status][build-badge-img]][build-url]
[![NPM version][npm-version-img]][npm-url]
[![NPM downloads per month][npm-downloads-img]][npm-url]
[![Chat on Slack][slack-img]][slack-url]
[![NPM license][npm-license-img]][npm-url]
[![Powered by Redfin][redfin-img]][redfin-url]

React framework with server render for blazing fast page load and seamless
transitions between pages in the browser.

** **
#### Just getting started with `react-server`?

The _easiest_ way to get started is with our [yeoman
generator](packages/generator-react-server):

```bash
# install yeoman
npm install -g yo

# install the react-server generator
npm install -g generator-react-server

# make a new react-server project in the CURRENT directory
yo react-server

# run the new app
npm run start
# go to http://localhost:3000
```

That hooks you up with [`react-server-cli`](packages/react-server-cli), which
will take care of the _server_ part and get you up and running right away.

#### Why `react-server`?

One of the great things about React is its support for server-side rendering,
which can make sites show up faster for users and play better with search engine
bots.

However, when you actually try to use React for server-side rendering, you
quickly run into a bunch of practical problems, such as:

- How should I load data on the server for my components?
- How do I ensure that the client and the server load the same data and generate
the same HTML markup?
- How do I write code that can be both generated server-side and be part of a
single-page application (SPA)?
- How should I optimize the delivery of my JavaScript and CSS?
- How do I find out about and follow performance best practices?
- How do I ensure that my site is streamed to the browser as quickly as humanly
possible?
- How can I make my app resilient when my backend has high latency spikes?

`react-server` is a framework designed to make universal (née isomorphic) React
easier to write, providing standard answers for these questions and more. When
you write your app for `react-server`, you concentrate on your React components,
and `react-server` takes care of everything else that's needed to run and deploy
real React server-rendered apps. Under the hood, `react-server` is doing a bunch
of clever optimizations, many borrowed from the ideas behind [Facebook's Big Pipe](https://www.facebook.com/notes/facebook-engineering/bigpipe-pipelining-web-pages-for-high-performance/389414033919/),
to make sure that your site shows up as quickly as humanly possible
for your users.

Once you're hungry for more, dig into [the React Server documentation](https://react-server.io/docs) and
the [`react-server`](packages/react-server) code.
** **

#### Migrating from react-server 0.8.1 to 1.0.0

This release is a major, potentially breaking, change which upgrades react-server's dependencies from webpack 1.x to webpack 4.x, and babel 6.x to babel 7.x.

If using default react-server configuration, you should be able to update to 1.0.0 without issue. However, if you have extended the default react-server webpack config using the `webpackConfig` option, you may need to update your webpack configuration options to match [Webpack 4.x Documentation](https://webpack.js.org/concepts).

**Note**: If you are having trouble loading css bundles in `mode = production`, try switching from `import` to `require()` syntax. https://github.com/webpack-contrib/mini-css-extract-plugin/issues/27


#### Want to help?

Great!  There's a lot to do!
See [the contributing guide](CONTRIBUTING.md) to get started.

#### Where's all the code?!

This is a [Lerna](https://github.com/lerna/lerna) respository with multiple npm packages!
Check out the [`packages/`](packages/) directory :eyes:.

[build-badge-img]: https://travis-ci.org/redfin/react-server.svg?branch=master
[build-url]: https://travis-ci.org/redfin/react-server
[npm-url]: https://npmjs.org/package/react-server
[redfin-url]: https://www.redfin.com
[redfin-img]: https://img.shields.io/badge/Powered%20By-Redfin-c82021.svg
[npm-version-img]: https://badge.fury.io/js/react-server.svg
[npm-license-img]: https://img.shields.io/npm/l/react-server.svg
[npm-downloads-img]: https://img.shields.io/npm/dm/react-server.svg
[slack-url]: https://slack.react-server.io/
[slack-img]: https://slack.react-server.io/badge.svg
