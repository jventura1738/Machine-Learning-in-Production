<p align="center">
  <a href="https://getleon.ai"><img width="96" src="https://getleon.ai/img/logo.svg"></a><br><br>
  <a href="https://www.youtube.com/watch?v=p7GRGiicO1c"><img width="512" src="https://getleon.ai/img/1.0.0-beta.0_preview_en.png"></a><br>
</p>

<h1 align="center">Leon</h1>

*<p align="center">Your open-source personal assistant.</p>*

<p align="center">
  <a href="https://github.com/leon-ai/leon/blob/develop/LICENSE.md"><img src="https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat" /></a>
  <a href="https://github.com/leon-ai/leon/blob/develop/.github/CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" /></a>
  <br>
  <a href="https://github.com/leon-ai/leon/actions/workflows/build.yml"><img src="https://github.com/leon-ai/leon/actions/workflows/build.yml/badge.svg?branch=develop" /></a>
  <a href="https://github.com/leon-ai/leon/actions/workflows/tests.yml"><img src="https://github.com/leon-ai/leon/actions/workflows/tests.yml/badge.svg?branch=develop" /></a>
  <a href="https://github.com/leon-ai/leon/actions/workflows/lint.yml"><img src="https://github.com/leon-ai/leon/actions/workflows/lint.yml/badge.svg?branch=develop" /></a>
  <br>
  <a href="https://discord.gg/MNQqqKg"><img src="https://svgshare.com/i/V09.svg"/></a>
  <a href="https://twitter.com/louistiti_fr"><img src="https://img.shields.io/twitter/follow/louistiti_fr?label=Follow&style=social" /></a>
</p>

<p align="center">
  <a href="https://getleon.ai">Website</a> ::
  <a href="https://docs.getleon.ai">Documentation</a> ::
  <a href="https://roadmap.getleon.ai">Roadmap</a> ::
  <a href="https://github.com/leon-ai/leon/blob/develop/.github/CONTRIBUTING.md">Contributing</a> ::
  <a href="https://blog.getleon.ai/the-story-behind-leon/">Story</a>
</p>

---

## 👋 Introduction

**Leon** is an **open-source personal assistant** who can live **on your server**.

He **does stuff** when you **ask him for**.

You can **talk to him** and he can **talk to you**.
You can also **text him** and he can also **text you**.
If you want to, Leon can communicate with you by being **offline to protect your privacy**.

### Why?

> 1. If you are a developer (or not), you may want to build many things that could help in your daily life.
> Instead of building a dedicated project for each of those ideas, Leon can help you with his
> packages/modules (skills) structure.
> 2. With this generic structure, everyone can create their own modules and share them with others.
> Therefore there is only one core (to rule them all).
> 3. Leon uses AI concepts, which is cool.
> 4. Privacy matters, you can configure Leon to talk with him offline. You can already text with him without any third party services.
> 5. Open source is great.

### What is this repository for?

> This repository contains the following nodes of Leon:
> - The server
> - The packages/modules
> - The web app
> - The hotword node

### What is Leon able to do?

> Today, the most interesting part is about his core and the way he can scale up. He is pretty young but can easily scale to have new features (packages/modules).
> You can find what he is able to do by browsing the [packages list](https://github.com/leon-ai/leon/tree/develop/packages).

Sounds good for you? Then let's get started!

## ☁️ Try with a Single-Click

Gitpod will automatically setup an environment and run an instance for you.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/leon-ai/leon)

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) >= 14
- [npm](https://npmjs.com/) >= 5
- [Python](https://www.python.org/downloads/) >= 3
- [Pipenv](https://docs.pipenv.org) >= 2020.11.15
- Supported OSes: Linux, macOS and Windows

To install these prerequisites, you can follow the [How To section](https://docs.getleon.ai/how-to/) of the documentation.

### Installation

```sh
# Clone the repository (stable branch)
git clone -b master https://github.com/leon-ai/leon.git leon
# OR download the latest release at: https://github.com/leon-ai/leon/releases/latest

# Go to the project root
cd leon

# Install
npm install
```

### Usage

```sh
# Check the setup went well
npm run check

# Build
npm run build

# Run
npm start

# Go to http://localhost:1337
# Hooray! Leon is running
```

### Docker Installation

```sh
# Build
npm run docker:build

# Run
npm run docker:run

# Go to http://localhost:1337
# Hooray! Leon is running
```

## 📚 Documentation

For full documentation, visit [docs.getleon.ai](https://docs.getleon.ai).

## 🧭 Roadmap

To know what is going on, follow [roadmap.getleon.ai](https://roadmap.getleon.ai).

## ❤️ Contributing

If you have an idea for improving Leon, do not hesitate.

**Leon needs open source to live**, the more modules he has, the more skillful he becomes.

## 📖 The Story Behind Leon

You'll find a write-up on this [blog post](https://blog.getleon.ai/the-story-behind-leon/).

## 🔔 Stay Tuned

- [Newsletter](https://getleon.ai)
- [Blog](https://blog.getleon.ai)
- [GitHub issues](https://github.com/leon-ai/leon/issues)
- [Twitter](https://twitter.com/louistiti_fr)
- [#LeonAI](https://twitter.com/hashtag/LeonAI)

## 👨 Author

**Louis Grenard** ([@louistiti_fr](https://twitter.com/louistiti_fr))

## 👍 Sponsor

You can also contribute by [sponsoring Leon](https://sponsor.getleon.ai).

Please note that I dedicate most of my free time to Leon.

By sponsoring the project you make the project sustainable and faster to develop features.

The focus is not only limited to the activity you see on GitHub but also a lot of thinking about the direction of the project. Which is naturally related to the overall design, architecture, vision, learning process and so on...

## 📝 License
[MIT License](https://github.com/leon-ai/leon/blob/develop/LICENSE.md)

Copyright (c) 2019-present, Louis Grenard <louis.grenard@gmail.com>

## Cheers!
![Cheers!](https://github.githubassets.com/images/icons/emoji/unicode/1f379.png "Cheers!")
