# A permalink for your MIT License ![Travis CI Status](https://img.shields.io/travis/remy/mit-license/master.svg?style=for-the-badge)

I always forget to add a `LICENSE` file to my projects, so I wanted to link to a single resource that would always be up to date and would always have my details online.

Why keep this to myself, there are two ways to create your _own_ MIT license page:

1.  Use the generator tool (easiest)
2.  Make a request to the API (details below)
3.  Fork this project and send a pull request

Now I can always include <https://rem.mit-license.org> in all my projects which links `rem` (the CNAME) against my copyright holder name `Remy Sharp` - all stored in the `users` directory.

## Requesting your own MIT license page

The simplest way to create your own MIT license page is to use the self-service generator found [here](https://richienb.github.io/mit-license-generator).

You can fork this project, send me a pull request and wait for me to pull (which I'll do as quickly as possible) or if the user is still available you can do it yourself from the command line:

```bash
curl -d'{ "copyright": "Remy Sharp" }' https://rem.mit-license.org
```

If the `rem` user isn't taken already, then this will create the new user file on the fly and the URL will be immediately available.

You can send a full JSON file to the API, not _just_ the copyright, so this works too:

```bash
curl -d'{ "copyright": "Remy Sharp", "url": "https://remysharp.com", "email": "me@mysite.com", "format": "txt" }' https://rem.mit-license.org
```

Whilst the command above sends the data as a string which will later be parsed, you can explicitly specify a JSON `Content-Type`:

```bash
curl -H 'Content-Type: application/json' -d'{ "copyright": "Remy Sharp", "url": "https://remysharp.com", "email": "me@mysite.com", "format": "txt" }' https://rem.mit-license.org
```

You can also encode the data as URL query parameters like so:

```bash
curl -X POST "https://rem.mit-license.org/?copyright=Remy%20Sharp&url=http%3A%2F%2Fremysharp.com&email=me%40mysite.com&format=txt"
```

If there are any problems in the automated creation, send me a pull request and it'll go live soon after.

Equally, if you need to update the user file to include more details that you didn't initially include (extra fields in the next section) you will need to send a pull request on that `user.json` file via GitHub.

## The user.json file

The `users` directory contains a list of files, each representing a host on mit-license.org. The minimum requirement for the JSON is that it contains a `copyright` field - everything else is optional. Remember to ensure the `user.json` file is [valid JSON](https://jsonlint.com/).

Available fields:

* copyright (required)
* URL
* email
* format
* gravatar
* theme
* license

### copyright

Create a new file and give it the name of the CNAME you want (in my case it's `rem.json`). This file contains a JSON object containing at least a `copyright` property:

```json
{
  "copyright": "Remy Sharp, https://remysharp.com"
}
```

Means I can now link to <https://rem.mit-license.org> and it will show my license name (note that the date will always show the current year).

You can also use an array to hold multiple copyright holders:

```json
{
  "copyright": ["Remy Sharp", "Richie Bendall"]
}
```

Which will be formatted as:

    Remy Sharp and Richie Bendall

If you additionally want to include a URL and email with each copyright holder, use objects in the array:

```json
{
  "copyright": [
    {
      "name": "Remy Sharp, https://remysharp.com",
      "url": "https://remysharp.com",
      "email": "remy@remysharp.com"
    },
    {
      "name": "Richie Bendall, https://www.richie-bendall.ml",
      "url": "https://www.richie-bendall.ml",
      "email": "richiebendall@gmail.com"
    }
  ]
}
```

### url

In addition to the `copyright` property, if you want to make a link from the copyright text, you can include a `URL` property:

```json
{
  "copyright": "Remy Sharp, https://remysharp.com",
  "url": "https://remysharp.com"
}
```

### email

You can also include a link to your email which is displayed after the copyright notice using the `email` property (note the `mailto:` is automatically added):

```json
{
  "copyright": "Remy Sharp, https://remysharp.com",
  "url": "https://remysharp.com",
  "email": "me@mysite.com"
}
```

### format

And if you want your license to appear as plain text, just add the `format` property (currently only `txt` and `html` are supported):

```json
{
  "copyright": "Remy Sharp, https://remysharp.com",
  "url": "https://remysharp.com",
  "format": "txt"
}
```

### gravatar

And if you want to show your gravatar, just add the `gravatar` boolean property:

```json
{
  "copyright": "Remy Sharp, https://remysharp.com",
  "url": "https://remysharp.com",
  "email": "me@mysite.com",
  "gravatar": true
}
```

Note that the gravatar requires the email property. You also need to check the compatibility of the chosen theme. Currently, only the default theme supports Gravatar.

### Themes

If you've got an eye for design (or like me: not): you can contribute a theme by adding a CSS file to the `themes` directory. You can use the latest CSS technologies since they are automatically polyfilled. The default theme is simple and clean, but you can add your own as you like.

To use a theme, add the `theme` property to your `user.json` file, for example:

```json
{
  "copyright": "Remy Sharp, https://remysharp.com",
  "url": "https://remysharp.com",
  "theme": "flesch"
}
```

Current available themes:

* default - [preview](http://mit-license.org) (by
  [@remy](https://github.com/remy),
  [@raphaelbastide](https://github.com/raphaelbastide) &
  [@evertton](https://github.com/evertton))
* flesch - [preview](http://jsbin.com/ufefid/3) (by
  [@flesch](https://github.com/flesch))
* eula-modern - [preview](http://jsbin.com/ExiVida/1/) (by [@sauerlo](https://github.com/lsauer))
* afterdark - [preview](http://jsbin.com/ivufon/4) (by [@rmartindotco](https://github.com/rmartindotco))
* orange - [preview](http://jsbin.com/uzubos/2) (by [@kirbylover4000](https://github.com/kirbylover4000))
* plaintext - [preview](http://jsbin.com/uzubos/4) (by [@barberboy](https://github.com/barberboy))
* double-windsor - [preview](http://jsbin.com/uzubos/5/) (by [@desandro](https://github.com))
* cherry - [preview](http://jsbin.com/ufefid/5/) (by [@mustafa-x](https://github.com/mustafa-x))
* white cherry - [preview](http://jsbin.com/uzezas/2/) (by [@mustafa-x](https://github.com/mustafa-x))
* blackwood - [preview](http://jsbin.com/uzezas/) (by [@mustafa-x](https://github.com/mustafa-x))
* hipster-gray - [preview](http://jsbin.com/ivufon/10) (by [@noformnocontent](https://github.com/noformnocontent))
* xtansia - [preview](http://jsbin.com/ereren/1/) (by [@tomass1996](https://github.com/tomass1996))
* magic-mint - [preview](http://jsbin.com/obibot/1/) (by [@ekhager](https://github.com/ekhager))
* default-dark - [preview](http://jsbin.com/uhagaw/10) (by
  [@remy](https://github.com/remy),
  [@raphaelbastide](https://github.com/raphaelbastide) &
  [@evertton](https://github.com/evertton))
* black-beauty - [preview](http://jsbin.com/dovivu) (by [@evertton](https://github.com/evertton))
* silver-style - [preview](http://jsbin.com/erezijI/2) (by [@dev-dipesh](https://github.com/Dev-Dipesh))
* friendly - [preview](http://jsbin.com/hilula) (by [@evertton](https://github.com/evertton))
* opensans - [preview](http://jsbin.com/UfepUvah) (by [@pburtchaell](https://github.com/pburtchaell))
* solarized - [preview](http://jsbin.com/yimax/1) (by [@anmoljagetia](https://github.com/anmoljagetia))
* willpower - [preview](http://jsbin.com/piheyicoyi/1) (by [@willpowerart](https://github.com/willpowerart))
* rokkitt - [preview](http://jsbin.com/zudayiqeco/1) (by [@luizpicolo](https://github.com/luizpicolo))
* mitserrat - [preview](http://jsbin.com/xeqekutuwe/1) (by [@WouterJanson](https://github.com/WouterJanson))
* material - [preview](http://ahaasler.github.io/mit-license-material-theme/) (by [@ahaasler](https://github.com/ahaasler)). *Available colours: blue gray (default), red, pink, purple, deep purple, indigo, blue, light blue, cyan, teal, green, light green, lime, yellow, amber, orange, deep orange, brown and grey. To use a specific colour, add it as a dash-separated suffix on the theme name, such as `material-deep-orange`.*
* hmt-blue - [preview](https://jsbin.com/naqorar/) (by [@J2TeaM](https://github.com/J2TeaM))
* dusk - [preview](https://output.jsbin.com/giqivoh) (by [@georapbox](https://github.com/georapbox))
* 8bits - [preview](https://matricali.github.io/mit-license-8bits-theme/) (by [@matricali](https://github.com/matricali)). *Available colours: monochrome, monochrome-white, monochrome-blue-white, monochrome-green, monochrome-amber. To use a specific colour, add it as a dash-separated suffix on the theme name, such as `8bits-monochrome`.*
* hacker - [preview](https://tommy.mit-license.org/) (by [@TommyPujol06](https://github.com/TommyPujol06))
* anon-pro - [preview](https://b.mit-license.org) (by [@bbbrrriiiaaannn](https://github.com/bbbrrriiiaaannn))
* richienb - [preview](https://richienb.github.io/mit-license-richienb-theme/demo) (by [@Richienb](https://github.com/Richienb)). *Dark variant: `richienb-dark` - [preview](https://richienb.github.io/mit-license-richienb-theme/demo-dark).*
* tryhtml - [preview](https://output.jsbin.com/cawihuwuku) (by [@abranhe](https://github.com/abranhe))
* clarity - [preview](https://output.jsbin.com/likezir) (by [@Richienb](https://github.com/Richienb))
* darkblog - [preview](https://chand1012.dev/mit-license/) (by [@chand1012](https://github.com/chand1012))

## Formats & URLs

The following types of requests can be made to this project:

* <https://rem.mit-license.org/> HTML, or the default format specified in
    the json file (currently none specified on `rem`)
* <https://rem.mit-license.org/license.html> HTML
* <https://rem.mit-license.org/license.txt> Text

The URL also supports including a start year:

* <https://rem.mit-license.org/2009/> will
    show a license year range of 2009-2016 (2016 being the current year)
* <https://rem.mit-license.org/2009-2010>
    allows me to force the year range
* <https://rem.mit-license.org/2009-2010/license.txt> year range of 2009-2010 in plain text

You can also specify either the `MIT` or `ISC` license in the URL:

* <https://rem.mit-license.org/+MIT> will
    show the MIT License (default)
* <https://rem.mit-license.org/+ISC>
    shows the ISC license instead

Finally, the URL also supports pinning the year

* <https://rem.mit-license.org/@2009>
    this is useful for when your software copyright should expire ([as discussed here](https://github.com/remy/mit-license/issues/771))

## Ways to contribute

Aside from code contributions that make the project better, there are a few other specific ways that you can contribute to this project.

Development contributions from:

* [remy](https://github.com/remy)
* [batuhanicoz](https://github.com/batuhanicoz)
* [georgebashi](https://github.com/georgebashi)
* [mathiasbynens](https://github.com/mathiasbynens)
* [evertton](https://github.com/evertton)
* [Richienb](https://github.com/Richienb)

**SSL and wildcard DNS is supported by [CloudFlare](https://www.cloudflare.com) - thank you 🙏💙**

### 1. Donate domain years

I host the domain with namecheap.com and yearly renewal is $9.69 per year. If you want to contribute a year, send me a message and I'll add the years on.

Of course, I'll do my best to continue running the domain and hosting, but this is your chance to contribute to the community project.

Domain contributions:

* [remy](https://github.com/remy) - 2011-2012
* [barberboy](https://github.com/barberboy) - 2012-2013
* [paulirish](https://github.com/paulirish) - 2013-2014
* [batuhanicoz](https://github.com/batuhanicoz) - 2014-2015
* [buritica](https://github.com/buritica) - 2015-2016
* [adamstrawson](https://github.com/adamstrawson) - 2016-2018 (2 years)
* [keithamus](https://github.com/keithamus) - 2018-2026 (8 years)
* [pmuellr](https://github.com/pmuellr) - 2026-2027
* [danielknell](https://github.com/danielknell) - 2027-2029 (2 years)
* [barberboy](https://github.com/barberboy) - 2029-2030
* [mostly-magic](https://github.com/mostly-magic) - 2030-2032

_Please note that the whois says 2021 as you can only have 10 active registered years with ICANN - but the domain is set to auto-renew, so it's all good :)_

### 2. Hosting

For the first 5 years, mit-license.org was hosted on my own dedicated server, but I've now moved to Heroku and am paying a monthly fee. If you would like to donate **[please donate here](https://www.paypal.me/rem)** include a message and I will add your name to the credit. Hosting currently costs $7 per month if you want to donate in months or years, it's gratefully received ❤

Hosting contributions:

* [remy](https://github.com/remy) - 2011-2016 Apr...
* [therebelrobot](https://github.com/therebelrobot) 1 month
* [mkody](https://github.com/mkody) 2 months
* [dan9186](https://github.com/dan9186) 1 year
* Kristin Anthony 1 year
* [zhengyi-yang](https://github.com/zhengyi-yang) 5 months
* [catodd](https://github.com/catodd) 2 months
* [lrz0](https://github.com/lrz0) 1 month
* [matricali](https://github.com/matricali) 3 months
* [youchenlee](https://github.com/youchenlee) 12 months
* [ramsey](https://github.com/ramsey) 12 months
* [rmm5t](https://github.com/rmm5t) 1 month
* [wrainaud](https://github.com/wrainaud) 3 months
* [romkey](https://github.com/romkey) 12 months
* [kylewelsby](https://github.com/kylewelsby) 6 months
* [wiesner](https://github.com/wiesner) 1 month
* [rajinwonderland](https://github.com/rajinwonderland) 3 months
* [miszo](https://github.com/miszo) 1 month
* [you?](https://www.paypal.me/rem)

### 3. A lick of paint

I'm a developer, I seem only capable of _grey_! If you're a designer and want to contribute a decent lick of paint on the project that would be super. Just create a new theme and send me a pull request.

## License

And of course:

MIT: <https://rem.mit-license.org>
