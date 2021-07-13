<p align="center"><img src="https://cloud.githubusercontent.com/assets/8311605/24083714/e921a0d4-0cb2-11e7-8384-d42113ef5056.png" alt="SlackKit" width="500"/></p>

[![Build Status](https://dev.azure.com/pzignego/SlackKit/_apis/build/status/pvzig.SlackKit?branchName=master)](https://dev.azure.com/pzignego/SlackKit/_build/latest?definitionId=2&branchName=master)

![Swift Version](https://img.shields.io/badge/Swift-5-orange.svg)
![Plaforms](https://img.shields.io/badge/Platforms-macOS,_iOS,_tvOS,_Linux-lightgrey.svg)
![License MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)
[![SwiftPM compatible](https://img.shields.io/badge/SwiftPM-compatible-brightgreen.svg)](https://github.com/apple/swift-package-manager)
[![Carthage compatible](https://img.shields.io/badge/Carthage-compatible-brightgreen.svg)](https://github.com/Carthage/Carthage)
[![CocoaPods compatible](https://img.shields.io/badge/CocoaPods-compatible-brightgreen.svg)](https://cocoapods.org)

## SlackKit: Slack Apps in Swift
### Description

SlackKit makes it easy to build Slack apps in Swift.

It's intended to expose all of the functionality of Slack's [Real Time Messaging API](https://api.slack.com/rtm) as well as the [web APIs](https://api.slack.com/web) that are accessible to [bot users](https://api.slack.com/bot-users). SlackKit also supports Slack’s [OAuth 2.0](https://api.slack.com/docs/oauth) flow including the [Add to Slack](https://api.slack.com/docs/slack-button) and [Sign in with Slack](https://api.slack.com/docs/sign-in-with-slack) buttons, [incoming webhooks](https://api.slack.com/incoming-webhooks), [slash commands](https://api.slack.com/slash-commands), and [message buttons](https://api.slack.com/docs/message-buttons).

### Installation

#### Swift Package Manager

Add `SlackKit` to your `Package.swift`

```swift  
let package = Package(
	dependencies: [
		.package(url: "https://github.com/pvzig/SlackKit.git", .upToNextMinor(from: "4.6.0"))
	]
)
```

**When built using Swift Package Manager, SlackKit includes the [vapor websocket framework](https://github.com/vapor/websocket) by default which requires libressl.**

You can install it with [homebrew](https://brew.sh): `brew install libressl`

For additional details, see the [SKRTMAPI readme](https://github.com/pvzig/SlackKit/tree/master/SKRTMAPI#swift-package-manager).

#### Carthage

Add `SlackKit` to your `Cartfile`:

```
github "pvzig/SlackKit"
```

**SlackKit is now using .xcframeworks. When building your dependencies with carthage, please specify a platform: `carthage bootstrap --use-xcframeworks --platform macos`**

#### CocoaPods
Add `SlackKit` to your `Podfile`:

```
pod 'SlackKit'
```

### Usage
To use the library in your project import it:

```swift
import SlackKit
```

#### The Basics
Create a bot user with an API token:

```swift
import SlackKit

let bot = SlackKit()
bot.addRTMBotWithAPIToken("xoxb-SLACK-BOT-TOKEN")
// Register for event notifications
bot.notificationForEvent(.message) { (event, _) in
	// Your bot logic here
	print(event.message)
}
```

or create a ready-to-launch Slack app with your [application’s `Client ID` and `Client Secret`](https://api.slack.com/apps):

```swift
import SlackKit

let bot = SlackKit()
let oauthConfig = OAuthConfig(clientID: "CLIENT_ID", clientSecret: "CLIENT_SECRET")
bot.addServer(oauth: oauthConfig)
```

or just make calls to the Slack Web API:

```swift
import SlackKit

let bot = SlackKit()
bot.addWebAPIAccessWithToken("xoxb-SLACK-BOT-TOKEN")
bot.webAPI?.authenticationTest(success: { (success) in
	print(success)
}, failure: nil)

```

#### Slash Commands
After [configuring your slash command in Slack](https://my.slack.com/services/new/slash-commands) (you can also provide slash commands as part of a [Slack App](https://api.slack.com/slack-apps)), create a route, response middleware for that route, and add it to a responder:

```swift
let slackkit = SlackKit()
let middleware = ResponseMiddleware(token: "SLASH_COMMAND_TOKEN", response: SKResponse(text: "👋"))
let route = RequestRoute(path: "/hello", middleware: middleware)
let responder = SlackKitResponder(routes: [route])
slackkit.addServer(responder: responder)
```
When a user enters that slash command, it will hit your configured route and return the response you specified.

#### Message Buttons
Add [message buttons](https://api.slack.com/docs/message-buttons) to your responses for additional interactivity.

To send messages with actions, add them to an attachment and send them using the Web API:

```swift
let helloAction = Action(name: "hello", text: "🌎")
let attachment = Attachment(fallback: "Hello World", title: "Welcome to SlackKit", callbackID: "hello_world", actions: [helloAction])
slackkit.webAPI?.sendMessage(channel: "CXXXXXX", text: "", attachments: [attachment], success: nil, failure: nil)
```

To respond to message actions, add a `RequestRoute` with `MessageActionMiddleware` using your app’s verification token to your `SlackKitResponder`:

```swift
let response = ResponseMiddleware(token: "SLACK_APP_VERIFICATION_TOKEN", response: SKResponse(text: "Hello, world!"))
let actionRoute = MessageActionRoute(action: helloAction, middleware: response)
let actionMiddleware = MessageActionMiddleware(token: "SLACK_APP_VERIFICATION_TOKEN", routes:[actionRoute])
let actions = RequestRoute(path: "/actions", middleware: actionMiddleware)
let responder = SlackKitResponder(routes: [actions])
slackkit.addServer(responder: responder)
```

#### OAuth
Slack has [many different oauth scopes](https://api.slack.com/docs/oauth-scopes) that can be combined in different ways. If your application does not request the proper OAuth scopes, your API calls will fail. 

If you authenticate using OAuth and the Add to Slack or Sign in with Slack buttons this is handled for you.

For local development of things like OAuth, slash commands, and message buttons, you may want to use a tool like [ngrok](https://ngrok.com).
#### Advanced Usage
Don’t need the whole banana? Want more control over the low-level implementation details? Use the extensible frameworks SlackKit is built on:

| Framework        | Description |
| ------------- |-------------  |
| **[SKClient](https://github.com/pvzig/SlackKit/tree/master/SKClient)** | Write your own client implementation|
| **[SKRTMAPI](https://github.com/pvzig/SlackKit/tree/master/SKRTMAPI)**     | Connect to the Slack RTM API|
| **[SKServer](https://github.com/pvzig/SlackKit/tree/master/SKServer)**      | Spin up a server for a Slack app|
| **[SKWebAPI](https://github.com/pvzig/SlackKit/tree/master/SKWebAPI)** | Access the Slack Web API|

### Examples
You can find the source code for several example applications [here](https://github.com/pvzig/SlackKit/tree/master/Examples).

### Tutorials
- [Build a Slack Bot and Deploy to Heroku](https://medium.com/@pvzig/building-slack-bots-in-swift-b99e243e444c)

### Get In Touch
Twitter: [@pvzig](https://twitter.com/pvzig)

Email: <peter@launchsoft.co>
