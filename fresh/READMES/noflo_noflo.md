NoFlo: Flow-based programming for JavaScript
============================================

NoFlo is an implementation of [flow-based programming](http://en.wikipedia.org/wiki/Flow-based_programming) for JavaScript running on both Node.js and the browser. From WikiPedia:

> In computer science, flow-based programming (FBP) is a programming paradigm that defines applications as networks of "black box" processes, which exchange data across predefined connections by message passing, where the connections are specified externally to the processes. These black box processes can be reconnected endlessly to form different applications without having to be changed internally. FBP is thus naturally component-oriented.

Developers used to the [Unix philosophy](http://en.wikipedia.org/wiki/Unix_philosophy) should be immediately familiar with FBP:

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

It also fits well in Alan Kay's [original idea of object-oriented programming](http://userpage.fu-berlin.de/~ram/pub/pub_jf47ht81Ht/doc_kay_oop_en):

> I thought of objects being like biological cells and/or individual computers on a network, only able to communicate with messages (so messaging came at the very beginning -- it took a while to see how to do messaging in a programming language efficiently enough to be useful).

NoFlo components can be written in any language that transpiles down to JavaScript, including ES6. The system is heavily inspired by [J. Paul Morrison's](http://www.jpaulmorrison.com/) book [Flow-Based Programming](http://www.jpaulmorrison.com/fbp/#More).

Read more at <https://noflojs.org/>.

## Suitability

NoFlo is not a web framework or a UI toolkit. It is a way to coordinate and reorganize data flow in any JavaScript application. As such, it can be used for whatever purpose JavaScript can be used for. We know of NoFlo being used for anything from building [web servers](https://thegrid.io) and build tools, to coordinating events inside [GUI applications](https://flowhub.io), [driving](http://meemoo.org/blog/2015-01-14-turtle-power-to-the-people) [robots](http://bergie.iki.fi/blog/noflo-ardrone/), or building Internet-connected [art installations](http://bergie.iki.fi/blog/ingress-table/).

## Tools and ecosystem

NoFlo itself is just a library for implementing flow-based programs in JavaScript. There is an ecosystem of tools around NoFlo and the [fbp protocol](https://flowbased.github.io/fbp-protocol/) that make it more powerful. Here are some of them:

* [Flowhub](https://app.flowhub.io) -- browser-based visual programming **IDE** for NoFlo and other flow-based systems
* [noflo-nodejs](https://github.com/noflo/noflo-nodejs) -- command-line interface for running NoFlo programs on **Node.js**
* [noflo-browser-app](https://github.com/noflo/noflo-browser-app) -- template for building NoFlo programs for **the web**
* [noflo-assembly](https://github.com/noflo/noflo-assembly) -- **industrial approach** for designing NoFlo programs
* [fbp-spec](https://github.com/flowbased/fbp-spec) -- **data-driven tests** for NoFlo and other FBP environments
* [flowtrace](https://github.com/flowbased/flowtrace) -- tool for **retroactive debugging** of NoFlo programs. Supports visual replay with Flowhub

See also the [list of reusable NoFlo modules on NPM](https://www.npmjs.com/browse/keyword/noflo).

## Requirements and installing

NoFlo is available for Node.js [via NPM](https://npmjs.org/package/noflo), so you can install it with:

```bash
$ npm install noflo --save
```

You can make a browser build of NoFlo using webpack. For webpack builds, you need configure the component loader statically with [noflo-component-loader](https://github.com/noflo/noflo-component-loader). For projects using Grunt, [grunt-noflo-browser](https://github.com/noflo/grunt-noflo-browser) plugin makes this easy.

### Installing from Git

NoFlo requires a reasonably recent version of [Node.js](http://nodejs.org/), and some [npm](http://npmjs.org/) packages. Ensure that you have NoFlo checked out from Git, and all NPM dependencies installed. Build NoFlo with:

```bash
$ npm run build
```

Then you can install everything needed by a simple:

```bash
$ npm link
```

NoFlo is available from [GitHub](https://github.com/noflo/noflo) under the MIT license.

## Changes

Please refer to the [Release Notes](https://github.com/noflo/noflo/releases) and the [CHANGES.md document](https://github.com/noflo/noflo/blob/master/CHANGES.md).

## Usage

Please refer to <http://noflojs.org/documentation/>. For visual programming with NoFlo, see <https://docs.flowhub.io/>.

## Development

NoFlo development happens on GitHub. Just fork the [main repository](https://github.com/noflo/noflo), make modifications and send a pull request.

We have an extensive suite of tests available for NoFlo. Run them with:

```bash
$ npm run build
$ npm test
```

### Platform-specific tests

By default, the tests are run for both Node.js and the browser. You can also run only the tests for a particular target platform:

```bash
$ npm run test:node
```

or:

```bash
$ npm run test:browser
```

## Discussion

There is a `#noflo` channel on the [Flow-Based Programming Slack](https://join.slack.com/t/fbphq/shared_invite/enQtOTM4ODkzMTYyODE3LTJiMmNlZjhiMWY1MDY1ODA4Y2YzNDBlNDZlMTBkMDNlMjcwNzg2MGZhZjA2NjJjYTliYTM0OTIyYmM0Yzk0MDQ), and questions can be posted with the [`noflo` tag on Stack Overflow](http://stackoverflow.com/questions/tagged/noflo). See <http://noflojs.org/support/> for other ways to get in touch.
