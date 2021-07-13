# react-blessed

A [React](https://facebook.github.io/react/) custom renderer for the [blessed](https://github.com/chjj/blessed) library.

This renderer should currently be considered as experimental, is subject to change and will only work with React's latest version (`17.x.x`, using Fiber).

![demo](https://raw.githubusercontent.com/Yomguithereal/react-blessed/master/img/demo.gif)

## Summary

* [Installation](#installation)
* [Demo](#demo)
* [Usage](#usage)
  * [Rendering a basic application](#rendering-a-basic-application)
  * [Nodes & text nodes](#nodes--text-nodes)
  * [Refs](#refs)
  * [Events](#events)
  * [Classes](#classes)
  * [Using blessed forks](#using-blessed-forks)
  * [Using the devtools](#using-the-devtools)
* [Roadmap](#roadmap)
* [FAQ](#faq)
* [Contribution](#contribution)
* [License](#license)

## Installation

You can install `react-blessed` through npm:

```bash
# Be sure to install react>=17.0.0 & blessed>=0.1.81 before
npm install blessed react

# Then just install `react-blessed`
npm install react-blessed
```

## Demo

For a quick demo of what you could achieve with such a renderer you can clone this repository and check some of the [examples](./examples):

```bash
git clone https://github.com/Yomguithereal/react-blessed
cd react-blessed
npm install

# To see which examples you can run:
npm run demo

# Then choose one to run:
npm run demo animation
```

## Usage

### Rendering a basic application

```jsx
import React, {Component} from 'react';
import blessed from 'blessed';
import {render} from 'react-blessed';

// Rendering a simple centered box
class App extends Component {
  render() {
    return (
      <box top="center"
           left="center"
           width="50%"
           height="50%"
           border={{type: 'line'}}
           style={{border: {fg: 'blue'}}}>
        Hello World!
      </box>
    );
  }
}

// Creating our screen
const screen = blessed.screen({
  autoPadding: true,
  smartCSR: true,
  title: 'react-blessed hello world'
});

// Adding a way to quit the program
screen.key(['escape', 'q', 'C-c'], function(ch, key) {
  return process.exit(0);
});

// Rendering the React app using our screen
const component = render(<App />, screen);
```

### Nodes & text nodes

Any of the blessed [widgets](https://github.com/chjj/blessed#widgets) can be rendered through `react-blessed` by using a lowercased tag title.

Text nodes, on the other hand, will be rendered by applying the `setContent` method with the given text on the parent node.

### Refs

As with React's DOM renderer, `react-blessed` lets you handle the original blessed nodes, if you ever need them, through refs.

```jsx
class CustomList extends Component {
  componentDidMount() {

    // Focus on the first box
    this.refs.first.focus();
  }

  render() {
    return (
      <element>
        <box ref="first">
          First box.
        </box>
        <box ref="second">
          Second box.
        </box>
      </element>
    );
  }
}
```

### Events

Any blessed node event can be caught through a `on`-prefixed listener:

```jsx
class Completion extends Component {
  constructor(props) {
    super(props);

    this.state = {progress: 0, color: 'blue'};

    const interval = setInterval(() => {
      if (this.state.progress >= 100)
        return clearInterval(interval);

      this.setState({progress: this.state.progress + 1});
    }, 50);
  }

  render() {
    const {progress} = this.state,
          label = `Progress - ${progress}%`;

    // See the `onComplete` prop
    return <progressbar label={label}
                        onComplete={() => this.setState({color: 'green'})}
                        filled={progress}
                        style={{bar: {bg: this.state.color}}} />;
  }
}
```

### Classes

For convenience, `react-blessed` lets you handle classes looking like what [react-native](https://facebook.github.io/react-native/docs/style.html#content) proposes.

Just pass object or an array of objects as the class of your components likewise:

```jsx
// Let's say we want all our elements to have a fancy blue border
const stylesheet = {
  bordered: {
    border: {
      type: 'line'
    },
    style: {
      border: {
        fg: 'blue'
      }
    }
  }
};

class App extends Component {
  render() {
    return (
      <element>
        <box class={stylesheet.bordered}>
          First box.
        </box>
        <box class={stylesheet.bordered}>
          Second box.
        </box>
      </element>
    );
  }
}
```

You can of course combine classes (note that the given array of classes will be compacted):
```jsx
// Let's say we want all our elements to have a fancy blue border
const stylesheet = {
  bordered: {
    border: {
      type: 'line'
    },
    style: {
      border: {
        fg: 'blue'
      }
    }
  },
  magentaBackground: {
    style: {
      bg: 'magenta'
    }
  }
};

class App extends Component {
  render() {

    // If this flag is false, then the class won't apply to the second box
    const backgroundForSecondBox = this.props.backgroundForSecondBox;

    return (
      <element>
        <box class={[stylesheet.bordered, stylesheet.magentaBackground]}>
          First box.
        </box>
        <box class={[
          stylesheet.bordered,
          backgroundForSecondBox && stylesheet.magentaBackground
        ]}>
          Second box.
        </box>
      </element>
    );
  }
}
```

### Using blessed forks

Because [blessed](https://github.com/chjj/blessed) is not actively maintained in quite a while, you might want to use one of it's forks. To do that, import `createBlessedRenderer` function instead:

```
import React, {Component} from 'react';
import blessed from 'neo-blessed';
import {createBlessedRenderer} from 'react-blessed';

const render = createBlessedRenderer(blessed);
```

### Using the devtools

`react-blessed` can be used along with React's own devtools for convenience. To do so, just install [`react-devtools`](https://www.npmjs.com/package/react-devtools) in your project and all should work out of the box when running the Electron app, as soon as a `react-blessed` program is running on one of your shells.

## Roadmap

* Full support (meaning every tags and options should be handled by the renderer).
* `react-blessed-contrib` to add some sugar over the [blessed-contrib](https://github.com/yaronn/blessed-contrib) library (probably through full-fledged components).

## Faq

 * `<list/>` : To enable interactions, add `mouse={ true }` and/or `keys={ true }`

## Contribution

Contributions are obviously welcome.

Be sure to add unit tests if relevant and pass them all before submitting your pull request.

```bash
# Installing the dev environment
git clone git@github.com:Yomguithereal/react-blessed.git
cd react-blessed
npm install

# Running the tests
npm test
```

## License

MIT
