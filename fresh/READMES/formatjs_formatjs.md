# FormatJS

[![Unit + Karma Tests](https://github.com/formatjs/formatjs/actions/workflows/tests.yml/badge.svg)](https://github.com/formatjs/formatjs/actions/workflows/tests.yml)
[![Slack FormatJS](https://img.shields.io/badge/slack-@formatjs-green.svg?logo=slack)](https://join.slack.com/t/formatjs/shared_invite/enQtNjM2MjM4NjE4ODIxLTMyMWE0YTNhMTlmMzZlNzJlNjEzMWY0YjM2ODUxYjlmNDE2YzQyMDIxZDg3Y2Q5YWNlMzhhYzRiNDk0OGQwNGI)

[![Sauce Browser Matrix Status](https://app.saucelabs.com/browser-matrix/formatjsproject.svg)](https://app.saucelabs.com/u/formatjsproject)

This repository is the home of [FormatJS](http://formatjs.io/) and related libraries.

**Slack:** Join us on Slack at [formatjs.slack.com](https://formatjs.slack.com/) for help, general conversation and more 💬🎊🎉
You can sign-up using this [invitation link](https://join.slack.com/t/formatjs/shared_invite/enQtNjYwMzE4NjM1MDQzLTA5NDE1Y2Y1ZWNiZWI1YTU5MGUxY2M0YjA4NWNhMmU3YTRjZmQ3MTE3NzJmOTAxMWRmYWE1ZTdkMmYzNzA5Y2M).

## Development

We currently use [`bazel`](https://bazel.build/) to develop, along with [lerna](https://lerna.js.org/) for package management.

To setup locally, first initialize the git submodule:

```sh
git submodule init
git submodule update
```

Now you can build & test with `npm`:

```sh
npm i && npm run build && npm run test
```

To run examples:

```sh
npm run examples
```

To build/test individual package:

```sh
npx bazel build //packages/react-intl
npx bazel test //packages/react-intl
```

Releases can be done with the following steps (**must use `npm`**):

```sh
npm run release
```

To publish next tag (**must use `npm`**):

```sh
npm run release:next
```

## Published Packages

| Package                                                                                                | Version                                                                 | Changelog                                                             | License                                                       |
| ------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| [@formatjs/cli](https://www.npmjs.com/package/@formatjs/cli)                                           | ![version](https://badgen.net/npm/v/@formatjs/cli)                      | [CHANGELOG](packages/cli/CHANGELOG.md)                                | [MIT](packages/cli/LICENSE.md)                                |
| [@formatjs/ecma402-abstract](https://www.npmjs.com/package/@formatjs/ecma402-abstract)                 | ![version](https://badgen.net/npm/v/@formatjs/ecma402-abstract)         | [CHANGELOG](packages/ecma402-abstract/CHANGELOG.md)                   | [MIT](packages/ecma402-abstract/LICENSE.md)                   |
| [@formatjs/icu-messageformat-parser](https://www.npmjs.com/package/@formatjs/icu-messageformat-parser) | ![version](https://badgen.net/npm/v/@formatjs/icu-messageformat-parser) | [CHANGELOG](packages/@formatjs/icu-messageformat-parser/CHANGELOG.md) | [MIT](packages/@formatjs/icu-messageformat-parser/LICENSE.md) |
| [@formatjs/intl-datetimeformat](https://www.npmjs.com/package/@formatjs/intl-datetimeformat)           | ![version](https://badgen.net/npm/v/@formatjs/intl-datetimeformat)      | [CHANGELOG](packages/intl-datetimeformat/CHANGELOG.md)                | [MIT](packages/intl-datetimeformat/LICENSE.md)                |
| [@formatjs/intl-displaynames](https://www.npmjs.com/package/@formatjs/intl-displaynames)               | ![version](https://badgen.net/npm/v/@formatjs/intl-displaynames)        | [CHANGELOG](packages/intl-displaynames/CHANGELOG.md)                  | [MIT](packages/intl-displaynames/LICENSE.md)                  |
| [@formatjs/intl-getcanonicallocales](https://www.npmjs.com/package/@formatjs/intl-getcanonicallocales) | ![version](https://badgen.net/npm/v/@formatjs/intl-getcanonicallocales) | [CHANGELOG](packages/intl-getcanonicallocales/CHANGELOG.md)           | [MIT](packages/intl-getcanonicallocales/LICENSE.md)           |
| [@formatjs/intl-listformat](https://www.npmjs.com/package/@formatjs/intl-listformat)                   | ![version](https://badgen.net/npm/v/@formatjs/intl-listformat)          | [CHANGELOG](packages/intl-listformat/CHANGELOG.md)                    | [MIT](packages/intl-listformat/LICENSE.md)                    |
| [@formatjs/intl-locale](https://www.npmjs.com/package/@formatjs/intl-locale)                           | ![version](https://badgen.net/npm/v/@formatjs/intl-locale)              | [CHANGELOG](packages/intl-locale/CHANGELOG.md)                        | [MIT](packages/intl-locale/LICENSE.md)                        |
| [@formatjs/intl-numberformat](https://www.npmjs.com/package/@formatjs/intl-numberformat)               | ![version](https://badgen.net/npm/v/@formatjs/intl-numberformat)        | [CHANGELOG](packages/intl-numberformat/CHANGELOG.md)                  | [MIT](packages/intl-numberformat/LICENSE.md)                  |
| [@formatjs/intl-pluralrules](https://www.npmjs.com/package/@formatjs/intl-pluralrules)                 | ![version](https://badgen.net/npm/v/@formatjs/intl-pluralrules)         | [CHANGELOG](packages/intl-pluralrules/CHANGELOG.md)                   | [MIT](packages/intl-pluralrules/LICENSE.md)                   |
| [@formatjs/intl-relativetimeformat](https://www.npmjs.com/package/@formatjs/intl-relativetimeformat)   | ![version](https://badgen.net/npm/v/@formatjs/intl-relativetimeformat)  | [CHANGELOG](packages/intl-relativetimeformat/CHANGELOG.md)            | [MIT](packages/intl-relativetimeformat/LICENSE.md)            |
| [@formatjs/ts-transformer](https://www.npmjs.com/package/@formatjs/ts-transformer)                     | ![version](https://badgen.net/npm/v/@formatjs/ts-transformer)           | [CHANGELOG](packages/ts-transformer/CHANGELOG.md)                     | [MIT](packages/ts-transformer/LICENSE.md)                     |
| [babel-plugin-formatjs](https://www.npmjs.com/package/babel-plugin-formatjs)                           | ![version](https://badgen.net/npm/v/babel-plugin-formatjs)              | [CHANGELOG](packages/babel-plugin-formatjs/CHANGELOG.md)              | [MIT](packages/babel-plugin-formatjs/LICENSE.md)              |
| [eslint-plugin-formatjs](https://www.npmjs.com/package/eslint-plugin-formatjs)                         | ![version](https://badgen.net/npm/v/eslint-plugin-formatjs)             | [CHANGELOG](packages/eslint-plugin-formatjs/CHANGELOG.md)             | [MIT](packages/eslint-plugin-formatjs/LICENSE.md)             |
| [intl-messageformat](https://www.npmjs.com/package/intl-messageformat)                                 | ![version](https://badgen.net/npm/v/intl-messageformat)                 | [CHANGELOG](packages/intl-messageformat/CHANGELOG.md)                 | [BSD](packages/intl-messageformat/LICENSE.md)                 |
| [react-intl](https://www.npmjs.com/package/react-intl)                                                 | ![version](https://badgen.net/npm/v/react-intl)                         | [CHANGELOG](packages/react-intl/CHANGELOG.md)                         | [BSD](packages/react-intl/LICENSE.md)                         |

## Big Thanks

Cross-browser Testing Platform and Open Source <3 Provided by [Sauce Labs][saucelabs]

[lerna]: https://lerna.js.org/
[saucelabs]: https://saucelabs.com
