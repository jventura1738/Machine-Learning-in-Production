<div align="center">
  <a href="https://hoppscotch.io">
    <img
      src="https://raw.githubusercontent.com/hoppscotch/hoppscotch/main/static/logo.png"
      alt="Hoppscotch Logo"
      height="64"
    />
  </a>
  <br />
  <p>
    <h3>
      <b>
        Hoppscotch
      </b>
    </h3>
  </p>
  <p>
    <b>
      Open source API development ecosystem
    </b>
  </p>
  <p>

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen?logo=github)](CODE_OF_CONDUCT.md) [![Website](https://img.shields.io/website?url=https%3A%2F%2Fhoppscotch.io&logo=hoppscotch)](https://hoppscotch.io) [![Tests](https://github.com/hoppscotch/hoppscotch/actions/workflows/tests.yml/badge.svg)](https://github.com/hoppscotch/hoppscotch/actions) [![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fhoppscotch.io%2F)](https://twitter.com/share?text=%F0%9F%91%BD%20Hoppscotch%20%E2%80%A2%20Open%20source%20API%20development%20ecosystem%20-%20Helps%20you%20create%20requests%20faster,%20saving%20precious%20time%20on%20development.&url=https://hoppscotch.io&hashtags=hoppscotch&via=hoppscotch_io)

  </p>
  <p>
    <sub>
      Built with ❤︎ by
      <a href="https://github.com/hoppscotch/hoppscotch/graphs/contributors">
        contributors
      </a>
    </sub>
  </p>
  <br />
  <p>
    <a href="https://hoppscotch.io">
      <img
        src="https://raw.githubusercontent.com/hoppscotch/hoppscotch/main/static/images/screenshots/banner_dark.png"
        alt="Screenshot"
        width="100%"
      />
    </a>
  </p>
</div>

#### **Contact**

[![Chat on Discord](https://img.shields.io/badge/chat-Discord-7289DA?logo=discord)](https://hoppscotch.io/discord) [![Chat on Telegram](https://img.shields.io/badge/chat-Telegram-2CA5E0?logo=Telegram)](https://hoppscotch.io/telegram)

<details open>
  <summary><b>Table of contents</b></summary>

---

- [Features](#features)
- [Demo](#demo)
- [Usage](#usage)
- [Built with](#built-with)
- [Developing](#developing)
- [Docker](#docker)
- [Releasing](#releasing)
- [Contributing](#contributing)
- [Continuous Integration](#continuous-integration)
- [Changelog](#changelog)
- [Authors](#authors)
- [License](#license)

---

</details>

### **Features**

❤️ **Lightweight:** Crafted with minimalistic UI design.

⚡️ **Fast:** Send requests and get/copy responses in real-time.

<details>
  <summary><i>HTTP Methods</i></summary>

---

- `GET` - Requests retrieve resource information
- `HEAD` - Retrieve response headers identical to those of a GET request, but without the response body.
- `POST` - The server creates a new entry in a database
- `PUT` - Updates an existing resource
- `DELETE` - Deletes resource or related component
- `CONNECT` - Establishes a tunnel to the server identified by the target resource
- `OPTIONS` - Describe the communication options for the target resource
- `TRACE` - Performs a message loop-back test along the path to the target resource
- `PATCH` - Very similar to `PUT` but makes a partial update on a resource
- `<custom>` - Some APIs use custom request methods such as `LIST`. Type in your custom methods.

---

</details>

🌈 **Make it yours:** Customizable combinations for background, foreground and accent colors. [Customize now ✨](https://hoppscotch.io/settings)

<details>
  <summary><i>Theming</i></summary>

---

- Choose theme: System, Light, Dark (default) and Black
- Choose accent color: Blue, Green (default), Teal, Indigo, Purple, Orange, Pink, Red, and Yellow
- Toggle auto-scroll to response

<p>
  <a href="https://hoppscotch.io"><img src="https://raw.githubusercontent.com/hoppscotch/hoppscotch/main/static/images/screenshots/banner_light.png" alt="Screenshot" width="100%"></a>
</p>

---

</details>

_Customized themes are synced with local session storage_

🔥 **PWA:** Install as a [PWA](https://developers.google.com/web/progressive-web-apps) on your device.

<details>
  <summary><i>Features</i></summary>

---

- Instant loading with Service Workers
- Offline support
- Low RAM/memory and CPU usage
- Add to Home Screen
- Desktop PWA

---

</details>

🚀 **Request:** Retrieve response from endpoint instantly.

- Choose `method`
- Enter `URL`
- Send

<details>
  <summary><i>Features</i></summary>

---

- Copy/share public "Share URL"
- Generate/copy request code snippets for 10+ languages and frameworks
- Import `cURL`
- Label requests

---

</details>

🔌 **WebSocket:** Establish full-duplex communication channels over a single TCP connection.

📡 **Server Sent Events:** Receive a stream of updates from a server over a HTTP connection without resorting to polling.

🌩 **Socket.IO:** Send and Receive data with SocketIO server.

🦟 **MQTT:** Subscribe and Publish to topics of a MQTT Broker.

🔮 **GraphQL:** GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data.

<details>
  <summary><i>Features</i></summary>

---

- Set endpoint and get schemas
- Multi-column docs
- Set custom request headers
- Query schema
- Get query response

---

</details>

🔐 **Authentication:** Allows to identify the end user.

<details>
  <summary><i>Types</i></summary>

---

- None
- Basic
- Bearer Token
- OAuth 2.0
- OIDC Access Token/PKCE

---

</details>

📢 **Headers:** Describes the format the body of your request is being sent as.

📫 **Parameters:** Use request parameters to set varying parts in simulated requests.

📃 **Request Body:** Used to send and receive data via the REST API.

<details>
  <summary><i>Options</i></summary>

---

- Set `Content Type`
- Add or remove Parameter list
- Toggle between key-value and RAW input parameter list

---

</details>

👋 **Response:** Contains the status line, headers and the message/response body.

<details>
  <summary><i>Features</i></summary>

---

- Copy response to clipboard
- Download response as a file
- View response headers
- View raw and preview of HTML, image, JSON, XML responses

---

</details>

⏰ **History:** Request entries are synced with cloud / local session storage to restore with a single click.

📁 **Collections:** Keep your API requests organized with collections and folders. Reuse them with a single click.

<details>
  <summary><i>Features</i></summary>

---

- Unlimited collections, folders and requests
- Nested folders
- Export as / import from GitHub gist

---

</details>

_Collections are synced with cloud / local session storage_

🌐 **Proxy:** Enable Proxy Mode from Settings to access blocked APIs.

<details>
  <summary><i>Features</i></summary>

---

- Hide your IP address
- Fixes [`CORS`](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (Cross Origin Resource Sharing) issues
- Access APIs served in non-HTTPS (`http://`)
- Use custom Proxy URL

---

</details>

_Official proxy server is hosted by Hoppscotch - **[GitHub](https://github.com/hoppscotch/proxyscotch)** - **[Privacy Policy](https://github.com/hoppscotch/proxyscotch/wiki/Privacy-policy)**_

📜 **Pre-Request Scripts β:** Snippets of code associated with a request that are executed before the request is sent.

<details>
  <summary><i>Use-cases</i></summary>

---

- Initialize environment variables
- Include timestamp in the request headers
- Send a random alphanumeric string in the URL parameters

---

</details>

📄 **API Documentation:** Create and share dynamic API documentation easily, quickly.

<details>
  <summary><i>Usage</i></summary>

---

1. Add your requests to Collections and Folders
2. Export Collections and easily share your APIs with the rest of your team
3. Import Collections and Generate Documentation on-the-go

---

</details>

⌨️ **Keyboard Shortcuts:** Optimized for efficiency.

> **[Shortcuts WIki](https://github.com/hoppscotch/hoppscotch/wiki/Shortcuts)**

🌎 **i18n:** Experience the app in your own language.

<details>
  <summary><i>Usage</i></summary>

---

1. Scroll down to the footer
2. Click "Choose Language" icon button
3. Select your language from the menu

---

</details>

_Keep in mind: Translations aren't available for all source and target language combinations_

**To provide a localized experience for users around the world, you can add you own translations.**

_**All `i18n` contributions are welcome to `i18n` [branch](https://github.com/hoppscotch/hoppscotch/tree/i18n) only!**_

📦 **Add-ons:** Official add-ons for hoppscotch.

- **[Proxy](https://github.com/hoppscotch/proxyscotch)** - A simple proxy server created for Hoppscotch
- **[CLI β](https://github.com/hoppscotch/hopp-cli)** - A CLI solution for Hoppscotch
- **[Browser Extensions](https://github.com/hoppscotch/hoppscotch-extension)** - Browser extensions that simplifies access to Hoppscotch

  [![Firefox](https://raw.github.com/alrra/browser-logos/master/src/firefox/firefox_16x16.png) **Firefox**](https://addons.mozilla.org/en-US/firefox/addon/hoppscotch) &nbsp;|&nbsp; [![Chrome](https://raw.github.com/alrra/browser-logos/master/src/chrome/chrome_16x16.png) **Chrome**](https://chrome.google.com/webstore/detail/hoppscotch-extension-for-c/amknoiejhlmhancpahfcfcfhllgkpbld)

  > **Extensions fixes `CORS` issues.**

- **[Hopp-Doc-Gen](https://github.com/hoppscotch/hopp-doc-gen)** - An API doc generator CLI for Hoppscotch

_Add-ons are developed and maintained under **[Official Hoppscotch Organization](https://github.com/hoppscotch)**._

☁️ **Auth + Sync:** Sign in and sync in real-time.

**Sign in with**

- Google
- GitHub

**Sync**

- History
- Collections
- Environments

✅ **Post-Request Tests β:** Write tests associated with a request that are executed after the request response.

<details>
  <summary><i>Use-cases</i></summary>

---

- Check the status code as an integer
- Filter response headers
- Parse the response data

---

</details>

🌱 **Environments** : Environment variables allow you to store and reuse values in your requests and scripts.

<details>
  <summary><i>Features</i></summary>

---

- Unlimited environments and variables
- Initialize through pre-request script
- Export as / import from GitHub gist

---

</details>

<details>
  <summary><i>Use-cases</i></summary>

---

- By storing a value in a variable, you can reference it throughout your request section
- If you need to update the value, you only have to change it in one place
- Using variables increases your ability to work efficiently and minimizes the likelihood of error

---

</details>

👨‍👩‍👧‍👦 **Teams β:** Helps you collaborate across your team to design, develop, and test APIs faster.

<details>
  <summary><i>Features</i></summary>

---

- Unlimited team collections and shared requests
- Unlimited team members
- User roles

---

</details>

**To find out more, please check out [Hoppscotch Wiki](https://github.com/hoppscotch/hoppscotch/wiki).**

## **Demo**

[hoppscotch.io](https://hoppscotch.io)

## **Usage**

1. Choose `method`
2. Enter `URL`
3. Send request
4. Get response

## **Built with**

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [SCSS](https://sass-lang.com), [Windi CSS](https://windicss.org)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [TypeScript](https://www.typescriptlang.org)
- [Vue](https://vuejs.org)
- [Nuxt](https://nuxtjs.org)

## **Developing**

0. Update [`.env.example`](https://github.com/hoppscotch/hoppscotch/blob/main/.env.example) file found in repository's root directory with your own keys and rename it to `.env`.

_Sample keys only works with the [production build](https://hoppscotch.io)._

### Browser based development environment

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/hoppscotch/hoppscotch)

### Local development environment

1. [Clone this repo](https://help.github.com/en/articles/cloning-a-repository) with git.
2. Install dependencies by running `npm install` within the directory that you cloned (probably `hoppscotch`).
3. Start the development server with `npm run dev`.
4. Open development site by going to [`http://localhost:3000`](http://localhost:3000) in your browser.

### Docker compose

1. [Clone this repo](https://help.github.com/en/articles/cloning-a-repository) with git.
2. Run `docker-compose up`
3. Open development site by going to [`http://localhost:3000`](http://localhost:3000) in your browser.

## **Docker**

**Official container** &nbsp; [![hoppscotch/hoppscotch](https://img.shields.io/docker/pulls/hoppscotch/hoppscotch?style=social)](https://hub.docker.com/r/hoppscotch/hoppscotch)

```bash
docker run --rm --name hoppscotch -p 3000:3000 hoppscotch/hoppscotch:latest
```

## **Releasing**

1. [Clone this repo](https://help.github.com/en/articles/cloning-a-repository) with git.
2. Install dependencies by running `npm install` within the directory that you cloned (probably `hoppscotch`).
3. Build the release files with `npm run generate`.
4. Find the built project in `./dist`.

## **Contributing**

Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/hoppscotch/hoppscotch/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## **Continuous Integration**

We use [GitHub Actions](https://github.com/features/actions) for continuous integration. Check out our [Build Workflows](https://github.com/hoppscotch/hoppscotch/actions).

## **Changelog**

See the [`CHANGELOG`](CHANGELOG.md) file for details.

## **Authors**

This project exists thanks to all the people who contribute [[Contribute](CONTRIBUTING.md)].

<div align="center">
  <a href="https://github.com/hoppscotch/hoppscotch/graphs/contributors">
    <img src="https://opencollective.com/hoppscotch/contributors.svg?width=840&button=false"
      alt="Contributors"
      width="100%" />
  </a>
</div>

## **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [`LICENSE`](LICENSE) file for details.
