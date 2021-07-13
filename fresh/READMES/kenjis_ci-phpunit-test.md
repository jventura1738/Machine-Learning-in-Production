# ci-phpunit-test for CodeIgniter 3.x

[![Latest Stable Version](https://poser.pugx.org/kenjis/ci-phpunit-test/v/stable)](https://packagist.org/packages/kenjis/ci-phpunit-test) [![Total Downloads](https://poser.pugx.org/kenjis/ci-phpunit-test/downloads)](https://packagist.org/packages/kenjis/ci-phpunit-test) [![Latest Unstable Version](https://poser.pugx.org/kenjis/ci-phpunit-test/v/unstable)](https://packagist.org/packages/kenjis/ci-phpunit-test) [![License](https://poser.pugx.org/kenjis/ci-phpunit-test/license)](https://packagist.org/packages/kenjis/ci-phpunit-test)

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/kenjis/ci-phpunit-test/badges/quality-score.png?b=3.x)](https://scrutinizer-ci.com/g/kenjis/ci-phpunit-test/?branch=3.x)
[![Coverage Status](https://coveralls.io/repos/kenjis/ci-phpunit-test/badge.svg?branch=3.x)](https://coveralls.io/r/kenjis/ci-phpunit-test?branch=3.x)
[![Build Status](https://travis-ci.com/kenjis/ci-phpunit-test.svg?branch=3.x)](https://travis-ci.com/kenjis/ci-phpunit-test)

An easier way to use PHPUnit with [CodeIgniter](https://github.com/bcit-ci/CodeIgniter) 3.x.

* You don't have to modify CodeIgniter core files at all.
* You can write controller tests easily.
* Nothing is untestable, maybe.
* Well documented.

![Screenshot: Running tests on NetBeans 8.1](docs/imgs/netbeans-8.1.png)

## Requirements

* PHP 7.3 or later
  * If you use Monkey Patching, you must use PHP-Parser 4.2 or later as a Composer dependency.
* CodeIgniter 3.x
  * If you want to upgrade to CodeIgniter4, see [#361](https://github.com/kenjis/ci-phpunit-test/issues/361).
* PHPUnit 9.3 or later
  * If you want to use PHPUnit 9.2 or earlier, please use ci-phpunit-test [2.x](https://github.com/kenjis/ci-phpunit-test/tree/2.x).

## Optional

* NetBeans
  * Go to *Project Properties > Testing > PHPUnit*, check *Use Custom Test Suite* checkbox, and select `application/tests/_ci_phpunit_test/TestSuiteProvider.php`.

## Change Log

See [Change Log](https://github.com/kenjis/ci-phpunit-test/blob/3.x/application/tests/_ci_phpunit_test/ChangeLog.md).

## Folder Structure

~~~
codeigniter/
├── application/
│   └── tests/
│        ├── _ci_phpunit_test/ ... don't touch! files ci-phpunit-test uses
│        ├── Bootstrap.php     ... bootstrap file for PHPUnit
│        ├── DbTestCase.php    ... DbTestCase class
│        ├── TestCase.php      ... TestCase class
│        ├── controllers/      ... put your controller tests
│        ├── libraries/        ... put your library tests
│        ├── mocks/
│        │   └── libraries/    ... mock libraries
│        ├── models/           ... put your model tests
│        └── phpunit.xml       ... config file for PHPUnit
└── vendor/
~~~

## Installation

### Manual Installation

1. Download latest `ci-phpunit-test` from <https://github.com/kenjis/ci-phpunit-test/releases>.
2. Unzip and copy `application/tests` folder into your `application` folder in CodeIgniter project.

That's it.

### Composer Installation

~~~sh-session
$ cd /path/to/codeigniter/
$ composer require kenjis/ci-phpunit-test:^3.0 --dev
~~~

And run `install.php`:

~~~sh-session
$ php vendor/kenjis/ci-phpunit-test/install.php --from-composer
~~~

* The above command always overwrites existing files.
* You must run it at CodeIgniter project root folder.
* You can specify your `application` and `public` folder with option arguments, if you use custom folder paths.

~~~sh-session
$ php vendor/kenjis/ci-phpunit-test/install.php -a <application_dir> -p <public_dir> -t <unittest_dir>
~~~

So the default would be:
~~~sh-session
$ php vendor/kenjis/ci-phpunit-test/install.php -a application -p public -t application/tests
~~~

* But some paths may be not correct, in that case, please fix them in [tests/Bootstrap.php](https://github.com/kenjis/ci-phpunit-test/blob/3.x/application/tests/Bootstrap.php#L98).

## Upgrading

### Manual Upgrading

1. Download latest `ci-phpunit-test` from <https://github.com/kenjis/ci-phpunit-test/releases>.
2. Unzip and replace `application/tests/_ci_phpunit_test` folder.
3. Read [Change Log](https://github.com/kenjis/ci-phpunit-test/blob/3.x/application/tests/_ci_phpunit_test/ChangeLog.md).

### Composer Upgrading

~~~sh-session
$ cd /path/to/codeigniter/
$ composer update kenjis/ci-phpunit-test
~~~

Read [Change Log](https://github.com/kenjis/ci-phpunit-test/blob/3.x/application/tests/_ci_phpunit_test/ChangeLog.md).

#### If you want to remove application/test/_ci_phpunit_test/

If you're upgrading from a previous version of `ci-phpunit-test` that created
an `application/test/_ci_phpunit_test` directory and now want to directly use
`ci-phpunit-test` from Composer, you have a couple of additional steps:

1. Delete the old test library directory: 
    ```sh-session
    $ rm -rf /path/to/codeigniter/application/tests/_ci_phpunit_test
    ```
2. Edit the `application/tests/Bootstrap.php` file. At the bottom of the "set the main path constants"
   section, add the following:
    ```php
    define('CI_PHPUNIT_TESTPATH', implode(
        DIRECTORY_SEPARATOR,
        [dirname(APPPATH), 'vendor', 'kenjis', 'ci-phpunit-test', 'application', 'tests', '_ci_phpunit_test']
    ).DIRECTORY_SEPARATOR);
    ```
    And replace any references to `__DIR__ . '/_ci_phpunit_test/` or `TESTPATH . '_ci_phpunit_test` with
    `CI_PHPUNIT_TESTPATH . '`.  (So, for example, `__DIR__ . '/_ci_phpunit_test/CIPHPUnitTest.php'`
    would become `CI_PHPUNIT_TESTPATH . '/CIPHPUnitTest.php'`.)

## How to Run Tests

You need to install PHPUnit before running tests.

If you use Composer:
```sh-session
$ composer require phpunit/phpunit --dev
```

### Run All Tests

~~~sh-session
$ cd /path/to/codeigniter/
$ vendor/bin/phpunit -c application/tests/
PHPUnit 9.5.4 by Sebastian Bergmann and contributors.

...                                                                 3 / 3 (100%)

Time: 00:00.102, Memory: 12.00 MB

OK (3 tests, 3 assertions)

Generating code coverage report in Clover XML format ... done [00:00.002]

Generating code coverage report in HTML format ... done [00:00.012]
~~~

To generate coverage report, Xdebug is needed.

### Run a Single Test

If you want to run a single test case file:

~~~sh-session
$ vendor/bin/phpunit -c application/tests/ application/tests/models/Category_model_test.php
~~~

## How to Write Tests

As an example, a test case class for `Inventory_model` would be as follows:

~~~php
<?php

class Inventory_model_test extends TestCase
{
    public function setUp(): void
    {
        $this->resetInstance();
        $this->CI->load->model('Inventory_model');
        $this->obj = $this->CI->Inventory_model;
    }

    public function test_get_category_list()
    {
        $expected = [
            1 => 'Book',
            2 => 'CD',
            3 => 'DVD',
        ];
        $list = $this->obj->get_category_list();
        foreach ($list as $category) {
            $this->assertEquals($expected[$category->id], $category->name);
        }
    }

    public function test_get_category_name()
    {
        $actual = $this->obj->get_category_name(1);
        $expected = 'Book';
        $this->assertEquals($expected, $actual);
    }
}
~~~

As an example, a test case class for Welcome controller would be as follows:

~~~php
<?php

class Welcome_test extends TestCase
{
    public function test_index()
    {
        $output = $this->request('GET', 'welcome/index');
        $this->assertStringContainsString(
            '<title>Welcome to CodeIgniter</title>', $output
        );
    }
}
~~~

See [How to Write Tests](https://github.com/kenjis/ci-phpunit-test/blob/3.x/docs/HowToWriteTests.md) for details.

## Function/Class Reference

See [Function and Class Reference](https://github.com/kenjis/ci-phpunit-test/blob/3.x/docs/FunctionAndClassReference.md).

## Tips

See [Tips](https://github.com/kenjis/ci-phpunit-test/blob/3.x/docs/Tips.md).

## Stand-alone Packages

Some features of *ci-phpunit-test* are available in the following standalone packages.

* https://github.com/kenjis/phpunit-helper
* https://github.com/kenjis/monkey-patch

## Related Projects for CodeIgniter 3.x

* [CodeIgniter Test Application for ci-phpunit-test](https://github.com/kenjis/ci-app-for-ci-phpunit-test)
* [CodeIgniter Composer Installer](https://github.com/kenjis/codeigniter-composer-installer)
* [Cli for CodeIgniter 3.0](https://github.com/kenjis/codeigniter-cli)
* [CodeIgniter Simple and Secure Twig](https://github.com/kenjis/codeigniter-ss-twig)
* [CodeIgniter Doctrine](https://github.com/kenjis/codeigniter-doctrine)
* [CodeIgniter Deployer](https://github.com/kenjis/codeigniter-deployer)
* [CodeIgniter3 Filename Checker](https://github.com/kenjis/codeigniter3-filename-checker)
* [CodeIgniter Widget (View Partial) Sample](https://github.com/kenjis/codeigniter-widgets)
* [CodeIgniter3 Namespaced Controller](https://github.com/kenjis/codeigniter3-namespaced-controller)
