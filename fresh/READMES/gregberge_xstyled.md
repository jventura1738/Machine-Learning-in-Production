<h1 align="center">
  <img src="https://raw.githubusercontent.com/gregberge/xstyled/master/resources/xstyled-logo.jpg" alt="xstyled" title="xstyled" width="300">
</h1>
<p align="center" style="font-size: 1.2rem;">A utility-first CSS-in-JS framework built for React.</p>

[![License](https://img.shields.io/npm/l/@xstyled/styled-components.svg)](https://github.com/gregberge/xstyled/blob/master/LICENSE)
[![npm package](https://img.shields.io/npm/v/@xstyled/styled-components/latest.svg)](https://www.npmjs.com/package/@xstyled/styled-components)
[![npm downloads](https://img.shields.io/npm/dm/@xstyled/styled-components.svg)](https://www.npmjs.com/package/@xstyled/styled-components)
[![CircleCI](https://circleci.com/gh/gregberge/xstyled.svg?style=svg)](https://circleci.com/gh/gregberge/xstyled)
[![codecov](https://codecov.io/gh/gregberge/xstyled/branch/master/graph/badge.svg)](https://codecov.io/gh/gregberge/xstyled)
![Code style](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)

```bash
npm install @xstyled/styled-components styled-components
```

## [Docs](https://xstyled.dev)

**See the documentation at [xstyled.dev](https://xstyled.dev)** for more information about using xstyled!

Quicklinks to some of the most-visited pages:

- [**Getting started**](https://xstyled.dev/docs/installation/)
- [Motivation](https://xstyled.dev/docs/introduction/#story)

## Example

```js
import { x } from '@xstyled/styled-components'

function Example() {
  return (
    <x.div p={{ _: 3, md: 6 }} bg="white" display="flex" spaceX={4}>
      <x.div flexShrink={0}>
        <x.img h={12} w={12} src="/img/logo.svg" alt="xstyled Logo" />
      </x.div>
      <x.div>
        <x.h4
          fontSize={{ _: 'md', lg: 'xl' }}
          fontWeight="medium"
          color="black"
        >
          xstyled
        </x.h4>
        <x.p color="gray-500">A CSS-in-JS framework built for React.</x.p>
      </x.div>
    </x.div>
  )
}
```

## License

Licensed under the MIT License, Copyright © 2019-present Greg Bergé.

See [LICENSE](./LICENSE) for more information.
