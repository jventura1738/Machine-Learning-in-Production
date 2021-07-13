# <img alt='redux-loop' src='https://raw.githubusercontent.com/raisemarketplace/redux-loop/master/logo/logo.png' height='200'>

A port of the [Elm Architecture](https://github.com/evancz/elm-architecture-tutorial) to Redux that allows you to sequence your effects naturally and purely by returning them from your reducers.

> Isn't it incorrect to cause side-effects in a reducer?

Yes! Absolutely.

> Doesn't redux-loop put side-effects in the reducer?

It doesn't. The values returned from the reducer when scheduling an effect with
redux-loop only _describe_ the effect. Calling the reducer will not cause the
effect to run. The value returned by the reducer is just an object that the
store knows how to interpret when it is enhanced by redux-loop. You can safely
call a reducer in your tests without worrying about waiting for effects to finish
and what they will do to your environment.

> What are the environment requirements for redux-loop?

`redux-loop` requires polyfills for ES6 `Promise` and `Symbol` to be included if
the browsers you target don't natively support them.

## Why use this?

Having used and followed the progression of Redux and the Elm Architecture, and
after trying other effect patterns for Redux, we came to the following
conclusion:

> Synchronous state transitions caused by returning a new state from the reducer
> in response to an action are just one of all possible effects an action can
> have on application state.

Many other methods for handling effects in Redux, especially those implemented
with action-creators, incorrectly teach the user that asynchronous effects are
fundamentally different from synchronous state transitions. This separation
encourages divergent and increasingly specific means of processing particular
types effects. Instead, we should focus on making our reducers powerful enough
to handle asynchronous effects as well as synchronous state transitions. With
`redux-loop`, the reducer doesn't just decide what happens _*now*_ due to a
particular action, it decides what happens _*next*_. All of the behavior of your
application can be traced through one place, and that behavior can be easily broken
apart and composed back together. This is one of the most powerful features of the
[Elm architecture](https://github.com/evancz/elm-architecture-tutorial), and with
`redux-loop` it is a feature of Redux as well.

## Installation

```
npm install --save redux-loop
```

## Support

Potential bugs, general discussion, and proposals or RFCs should be submitted
as issues to this repo, we'll do our best to address them quickly. We use this
library as well and want it to be the best it can! For questions about using the
library, [submit questions on StackOverflow](http://stackoverflow.com/questions/ask)
with the [`redux-loop` tag](http://stackoverflow.com/questions/tagged/redux-loop).

### Slack channel

[Come join our slack channel.](https://reduxloop-slack.herokuapp.com/)

### Don't see a feature you want?

If you're interested in adding something to `redux-loop` but don't want to wait
for us to incorporate the idea you can follow these steps to get your own installable
version of `redux-loop` with your feature included:

1. Fork the main repo here
1. Add your feature or change
1. Change the package `"name"` in package.json to be `"@<your-npm-username>/redux-loop`
1. Commit to master and `npm publish`
1. `npm install @<your-npm-username>/redux-loop`

We are _**always**_ interested in new ideas, but sometimes we get a little busy and fall
behind on responding and reviewing PRs. Hopefully this process will allow you to
continue making progress on your projects and also provide us with more context if and
when you do decide to make a PR for your new feature or change. The best way to verify
new features for a library is to use them in real-world scenarios!

## Contributing

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms. Multiple language translations are available at [contributor-covenant.org](https://www.contributor-covenant.org/translations.html)
