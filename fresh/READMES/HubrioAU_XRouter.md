<p align="center">
<img src="https://raw.githubusercontent.com/hubrioau/XRouter/master/XRouter.png" alt="XRouter" width="400" style="max-width:400px;width:auto;height:auto;"/>
</p>

<p align="center">
<a href="https://travis-ci.org/hubrioAU/XRouter"><img src="https://travis-ci.org/hubrioAU/XRouter.svg?branch=master" alt="Master Build Status" /></a>
<a href="https://codecov.io/gh/hubrioau/XRouter"><img src="https://codecov.io/gh/hubrioAU/XRouter/branch/master/graph/badge.svg" alt="CodeCov" /></a>
<a href="https://app.codacy.com/app/hubrioAU/XRouter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=hubrioAU/XRouter&amp;utm_campaign=Badge_Grade_Dashboard"><img src="https://api.codacy.com/project/badge/Grade/d0ef88b70fc843adb2944ce0d956269d" alt="Codacy Badge" /></a>
<a href="https://hubrioau.github.io/XRouter"><img src="https://img.shields.io/badge/📒%20docs-100%25-success.svg" alt="Documentation" /></a>
<br/>
<a href="https://swift.org"><img src="https://img.shields.io/badge/swift%20package-v2.0.1-FF3527.svg" alt="Swift Package Manager Version" /></a>
<a href="https://cocoapods.org/pods/XRouter"><img src="https://img.shields.io/cocoapods/v/XRouter.svg?style=flat" alt="Cocoapods Version" /></a>
<a href="https://cocoapods.org/pods/XRouter"><img src="https://img.shields.io/cocoapods/l/XRouter.svg?style=flat" alt="License" /></a>
<a href="https://swift.org"><img src="https://img.shields.io/badge/RxSwift-✔-blueviolet.svg" alt="Language" /></a>
</p>

# XRouter

Add powerful deep-linking, simplify navigation and ditch the expensive boilerplate.

## Docs

Complete [documentation is available here](https://hubrioau.github.io/XRouter/) and is generated using [Jazzy](https://github.com/realm/jazzy).

## Get started

### Installation

#### Swift Package Manager (SPM)

XRouter is available via Swift Package Manager version `2.0.1` onwards.

#### CocoaPods

XRouter is available through [CocoaPods](https://cocoapods.org). To install
it, simply add the following line to your Podfile:

```ruby
pod 'XRouter'
```

### Basic Usage

#### Defining your routes
Create a file containing the routes for your application.

```swift
enum Route: RouteType {
    case login
    case profile(userID: Int)
}
```

##### Create a Router
Configure a concrete instance of `XRouter` to resolve a standalone view controller, or start a modal flow by passing a navigation controller.

```swift
class Router: XRouter<Route> {
    override func prepareDestination(for route: Route) throws -> UIViewController {
        switch route {
        case .login:
            return AuthLoginFlowCoordinator().navigationController

        case .profile(let userID):
            return UserProfileViewController(profile: try repo.fetch(user: userID))
        }
    }
}
```

##### Perform navigation
```swift
router.navigate(to: .profile(userID: 3355))
```

### Advanced Usage

#### Deep Link Support

XRouter provides support for deep links and universal links.

You only need to do one thing to add URL support for your routes.
Implement the static method `registerURLs`:
```swift
enum Route: RouteType {
    static func registerURLs() -> URLMatcherGroup<Route>? {
        return .group {
            $0.map("/products") { .allProducts }
            $0.map("/user/*/logout") { .logout }
            $0.map("/products/{cat}/view") { try .products(category: $0.path("cat")) }

            $0.map("/user/{id}/profile") {
                try .viewProfile(withID: $0.path("id"), parameters: $0.query)
            }
        }
    }
}
```

Then you can call the `openURL(_:animated:completion:)` and/or `continue(_ userActivity:)` methods, e.g. from in your AppDelegate:
```swift
extension AppDelegate {
    /// Handle deep links.
    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
        return router.openURL(url, animated: false)
    }

    /// Handle universal links.
    func application(_ application: UIApplication, continue userActivity: NSUserActivity, restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool {
        return router.continue(userActivity)
    }
}
```

You can even define more advanced URL routing. For example, these rules could be used to match:

* `http://example.com/login` --> `.login`
* `https://example.com/signup` --> `.signup`
* `customScheme://myApp/qr-code?code=abcdef...` --> `.openQRCode("abcdef...")`
* `https://www.example.com/products` --> `.allProducts`
* `https://api.example.com/user/my-user-name/logout` --> `.logout`

```swift
enum Route: RouteType {
    static func registerURLs() -> URLMatcherGroup<Route>? {
        return .init(matchers: [
            .host("example.com") {
                $0.map("/login") { .login }
                $0.map("/signup") { .signup }
            },
            .scheme("customScheme") {
                $0.map("/qr-code") { .openQRCode($0.query("code")) }
            },
            .group {
                $0.map("/products") { .allProducts }
                $0.map("/user/*/logout") { .logout }
            }
        ])
    }
}
```

#### Global error navigation handling

If you handle all navigation errors in the same way, you can override the `received(unhandledError:)` method.

```swift
class Router: XRouter<Route> {
    override func received(unhandledError error: Error) {
        log.error("Oh no! An error occured: \(error)")
    }
}
```

Or you can set a custom completion handler for some individual navigation action:

```swift
router.navigate(to: .profilePage(withID: 24)) { (optionalError) in
    if let error = optionalError {
        print("Oh no, we couldn't go here because there was an error!")
    }
}
```

#### Custom Transitions
Here is an example using the popular [Hero Transitions](https://github.com/HeroTransitions/Hero) library.

Define your custom transitions:
```swift
  /// Perform a cross-fade transition using Hero library.
  static let heroCrossFade = RouteTransition { (source, destination, animated, completion) in
      source.hero.isEnabled = true
      destination.hero.isEnabled = true
      destination.hero.modalAnimationType = .fade

      /* Present the hero animation */
      source.present(destination, animated: animated) {
          completion(nil)
      }
  }
```

And set the transition to your custom transition in your Router:
```swift
    override func transition(for route: Route) -> RouteTransition {
        if case .profile = route {
          return .heroCrossFade
        }

        return .automatic
    }
```

#### RxSwift Support
XRouter also supports Rx out of the box. Bindings exist for `navigate(to:)`, which returns a `Completable`, and `openURL(_:)`, which returns a `Single<Bool>`.
```swift
router.rx.navigate(to: .loginFlow) // -> Completable
router.rx.openURL(url) // -> Single<Bool>
```

## Demo Project

To run the example project, clone the repo, and run it in the latest version of [Xcode](https://developer.apple.com/xcode/).

## License

XRouter is available under the MIT license. See the LICENSE file for more info.
