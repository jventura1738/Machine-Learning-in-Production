# did_you_mean [![Gem Version](https://badge.fury.io/rb/did_you_mean.svg)](https://rubygems.org/gems/did_you_mean) [![Build Status](https://travis-ci.org/ruby/did_you_mean.svg?branch=master)](https://travis-ci.org/ruby/did_you_mean)

## Installation

Ruby 2.3 and later ships with this gem and it will automatically be `require`d when a Ruby process starts up. No special setup is required.

## Examples

### NameError

#### Correcting a Misspelled Method Name

```ruby
methosd
# => NameError: undefined local variable or method `methosd' for main:Object
#    Did you mean?  methods
#                   method
```

#### Correcting a Misspelled Class Name

```ruby
OBject
# => NameError: uninitialized constant OBject
#    Did you mean?  Object
```

#### Suggesting an Instance Variable Name

```ruby
@full_name = "Yuki Nishijima"
first_name, last_name = full_name.split(" ")
# => NameError: undefined local variable or method `full_name' for main:Object
#    Did you mean?  @full_name
```

#### Correcting a Class Variable Name

```ruby
@@full_name = "Yuki Nishijima"
@@full_anme
# => NameError: uninitialized class variable @@full_anme in Object
#    Did you mean?  @@full_name
```

### NoMethodError

```ruby
full_name = "Yuki Nishijima"
full_name.starts_with?("Y")
# => NoMethodError: undefined method `starts_with?' for "Yuki Nishijima":String
#    Did you mean?  start_with?
```

### KeyError

```ruby
hash = {foo: 1, bar: 2, baz: 3}
hash.fetch(:fooo)
# => KeyError: key not found: :fooo
#    Did you mean?  :foo
```

### LoadError

```ruby
require 'net-http'
# => LoadError (cannot load such file -- net-http)
#    Did you mean?  net/http
```

## Verbose Formatter

This verbose formatter changes the error message format to take more lines/spaces so it'll be slightly easier to read the suggestions. This formatter can totally be used in any environment including production.

```ruby
OBject
# => NameError: uninitialized constant OBject
#    Did you mean?  Object

require 'did_you_mean/verbose'
OBject
# => NameError: uninitialized constant OBject
#
#        Did you mean? Object
#
```

## Using the `DidYouMean::SpellChecker`

If you need to programmatically find the closest matches to the user input, you could do so by re-using the `DidYouMean::SpellChecker` object.

```ruby
spell_checker = DidYouMean::SpellChecker.new(dictionary: ['email', 'fail', 'eval'])

spell_checker.correct('meail') # => ['email']
spell_checker.correct('afil')  # => ['fail']
```

## Disabling `did_you_mean`

Occasionally, you may want to disable the `did_you_mean` gem for e.g. debugging issues in the error object itself. You
can disable it entirely by specifying `--disable-did_you_mean` option to the `ruby` command:

```bash
$ ruby --disable-did_you_mean -e "1.zeor?"
-e:1:in `<main>': undefined method `zeor?' for 1:Integer (NameError)
```

When you do not have direct access to the `ruby` command (e.g. `rails console`, `irb`), you could apply options using the
`RUBYOPT` environment variable:

```bash
$ RUBYOPT='--disable-did_you_mean' irb
irb:0> 1.zeor?
# => NoMethodError (undefined method `zeor?' for 1:Integer)
```

### Getting the original error message

Sometimes, you do not want to disable the gem entirely, but need to get the original error message without suggestions
(e.g. testing). In this case, you could use the `#original_message` method on the error object:

```ruby
no_method_error = begin
                    1.zeor?
                  rescue NoMethodError => error
                    error
                  end

no_method_error.message
# => NoMethodError (undefined method `zeor?' for 1:Integer)
#    Did you mean?  zero?

no_method_error.original_message
# => NoMethodError (undefined method `zeor?' for 1:Integer)
```

## Benchmarking

Performance is very important as the `did_you_mean` gem attempts to find the closest matches on the fly right after an exception
is thrown. You could use the following rake tasks to get insights into how the gem performs:

```bash
bundle exec rake benchmark:ips:jaro
bundle exec rake benchmark:ips:levenshtein
bundle exec rake benchmark:memory
bundle exec rake benchmark:memory:jaro
bundle exec rake benchmark:memory:levenshtein
```

**Be sure to always use `bundle exec` otherwise it will activate the pre-installed version of the `did_you_mean`
 gem rather than using what's in the `lib/`.**

You could also use the [`benchmark-driver`](https://github.com/benchmark-driver/benchmark-driver) gem to know how each
Ruby performs differently.

```bash
bundle exec benchmark-driver benchmark/speed.yml --rbenv '2.6.0 --jit;2.6.0;2.5.3;truffleruby-1.0.0-rc10' --run-duration 30
```

## Contributing

1. Fork it (https://github.com/ruby/did_you_mean/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Make sure all tests pass (`bundle exec rake`)
5. Push to the branch (`git push origin my-new-feature`)
6. Create new Pull Request

## License

Copyright (c) 2014-16 Yuki Nishijima. See MIT-LICENSE for further details.
