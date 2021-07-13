# itty.bitty.site

itty.bitty takes html (or other data), compresses it into a URL fragment, and provides a link that can be shared. When it is opened, it inflates that data on the receiver’s side.

Learn more at [about.bitty.site](http://about.bitty.site)

Detailed workings [how.bitty.site](http://how.bitty.site)

## Advanced

**Handcrafted HTML files**

Drag one into the editor to convert it.

**Using Codepen.io**

Paste a codepen URL into the editor. Get started with a [template](https://codepen.io/pen?template=MXgrEr) or look at [some samples](https://codepen.io/collection/XprVQL/).

**Size Limits**

While most sites support 2000 bytes, [some can handle more](http://reference.bitty.site).
      
**Hosting**

One simple way to host is to [forward a domain](https://support.google.com/domains/answer/4522141?hl=en). Just paste the itty.bitty url in the redirect.

## Generating links programmatically
Encoding (Mac)

```echo -n 'hello world' | lzma -9 | base64 | xargs -0 printf "https://itty.bitty.site/#/%s\n"```

Encoding (Linux)

```echo -n 'hello world' | lzma -9 | base64 -w0 | xargs -0 printf "https://itty.bitty.site/#/%s\n"```

Encoding (Win Git/WSL)

`echo -n 'hello world' | xz --format=lzma -9 | base64 -w0 | printf "https://itty.bitty.site/#/%s\n" "$(cat -)"`

Encoding (Python)

`'https://itty.bitty.site/#/'+base64.b64encode(lzma.compress(bytes("hello world",encoding="utf-8"), format=lzma.FORMAT_ALONE, preset=9)).decode("utf-8")`

Encoding (Node.js)

`'https://itty.bitty.site/#/'+Buffer.from(lzma.compress("Hello World", 9)).toString('base64')`

Decoding (Mac)

`echo -n "[URL]" | sed -E 's/^.*#[^\/]*\/\??//g' | base64 -D | lzma -d `

Decoding (Linux)

`echo -n "[URL]" | sed -E 's/^.*#[^\/]*\/\??//g' | base64 -d | lzma -d`

Decoding (Win Git/WSL)

`echo -n "[URL]" | sed 's/^.*#[^\/]*\///g' | base64 -d | xz --format=lzma -d`  
