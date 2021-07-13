
# [Polyfill.io][website] &middot; [![license][license-badge]][license] [![PRs Welcome][pull-requests-badge]][contributing guide]

Polyfill.io is a service which makes web development less frustrating by selectively polyfilling just what the browser needs.
Polyfill.io reads the User-Agent header of each request and returns polyfills that are suitable for the requesting browser.

## Documentation

Polyfill.io documentation is [on the website][website].


## [Contributing][contributing guide]

Read our [contributing guide] to learn about our development process, how to propose bugfixes and improvements, and how to build and test your changes.

## Self-Hosting

If you are wanting to self-host this application you need Node.js 12 and npm or yarn installed.

You can prefix the path the application uses for the polyfill API by setting the environment variable `CONTEXT_PATH`.

## Testing powered by 
<a target="_blank" href="https://www.browserstack.com/"><img width="200" src="https://www.browserstack.com/images/layout/browserstack-logo-600x315.png"></a><br>
[[BrowserStack Open-Source Program](https://www.browserstack.com/open-source)]<br>


## License

Polyfill.io is licensed under the terms of the [MIT license][license]. Contributors must accept our [contribution terms].

[contributing guide]: ./.github/CONTRIBUTING.md
[contribution terms]: ./.github/contribution_licence_agreement.md
[license]: ./LICENSE.md
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg
[pull-requests-badge]: https://img.shields.io/badge/PRs-welcome-brightgreen.svg
[website]: https://polyfill.io
