<div align="center">
    <a href="https://lamp.sh/" target="_blank">
        <img alt="LAMP" src="https://github.com/teddysun/lamp/blob/master/conf/lamp.png">
    </a>
</div>

## Description

[LAMP](https://lamp.sh/) is a powerful bash script for the installation of Apache + PHP + MySQL/MariaDB and so on. You can install Apache + PHP + MySQL/MariaDB in an very easy way, just need to choose what you want to install before installation. And all things will be done in few minutes.

- [Supported System](#supported-system)
- [Supported Software](#supported-software)
- [Software Version](#software-version)
- [Installation](#installation)
- [Upgrade](#upgrade)
- [Backup](#backup)
- [Uninstall](#uninstall)
- [Default Installation Location](#default-installation-location)
- [Process Management](#process-management)
- [lamp command](#lamp-command)
- [Bugs & Issues](#bugs--issues)
- [License](#license)

## Supported System

- Amazon Linux 2018.03
- Amazon Linux 2
- CentOS-6.x
- CentOS-7.x
- CentOS-8.x (recommend)
- Debian-8.x
- Debian-9.x
- Debian-10.x (recommend)
- Ubuntu-16.x
- Ubuntu-18.x
- Ubuntu-20.x (recommend)

## Supported Software

- Apache-2.4 (Include HTTP/2 module: [nghttp2](https://github.com/nghttp2/nghttp2), [mod_http2](https://httpd.apache.org/docs/2.4/mod/mod_http2.html))
- Apache Additional Modules: [mod_wsgi](https://github.com/GrahamDumpleton/mod_wsgi), [mod_security](https://github.com/SpiderLabs/ModSecurity), [mod_jk](https://tomcat.apache.org/download-connectors.cgi)
- MySQL-5.6, MySQL-5.7, MySQL-8.0, MariaDB-10.1, MariaDB-10.2, MariaDB-10.3, MariaDB-10.4, MariaDB-10.5
- PHP-5.6, PHP-7.0, PHP-7.1, PHP-7.2, PHP-7.3, PHP-7.4, PHP-8.0
- PHP Additional extensions: [Zend OPcache](https://www.php.net/manual/en/book.opcache.php), [ionCube Loader](https://www.ioncube.com/loaders.php), [PDFlib](https://www.pdflib.com/), [XCache](https://xcache.lighttpd.net/), [APCu](https://pecl.php.net/package/APCu), [imagick](https://pecl.php.net/package/imagick), [gmagick](https://pecl.php.net/package/gmagick), [libsodium](https://github.com/jedisct1/libsodium-php), [memcached](https://github.com/php-memcached-dev/php-memcached), [redis](https://github.com/phpredis/phpredis), [mongodb](https://pecl.php.net/package/mongodb), [swoole](https://github.com/swoole/swoole-src), [yaf](https://github.com/laruence/yaf), [yar](https://github.com/laruence/yar), [msgpack](https://pecl.php.net/package/msgpack), [psr](https://github.com/jbboehr/php-psr), [phalcon](https://github.com/phalcon/cphalcon), [grpc](https://github.com/grpc/grpc), [xdebug](https://github.com/xdebug/xdebug)
- Other Software: [OpenSSL](https://github.com/openssl/openssl), [ImageMagick](https://github.com/ImageMagick/ImageMagick), [GraphicsMagick](http://www.graphicsmagick.org/), [Memcached](https://github.com/memcached/memcached), [phpMyAdmin](https://github.com/phpmyadmin/phpmyadmin), [Adminer](https://github.com/vrana/adminer), [Redis](https://github.com/redis/redis), [re2c](https://github.com/skvadrik/re2c), [KodExplorer](https://github.com/kalcaddle/KodExplorer)

## Software Version

| Apache & Additional Modules   | Version                                                   |
|-------------------------------|-----------------------------------------------------------|
| httpd                         | 2.4.48                                                    |
| apr                           | 1.7.0                                                     |
| apr-util                      | 1.6.1                                                     |
| nghttp2                       | 1.43.0                                                    |
| openssl                       | 1.1.1k                                                    |
| mod_wsgi                      | 4.8.0                                                     |
| mod_security2                 | 2.9.4                                                     |
| mod_jk                        | 1.2.48                                                    |

| Database                      | Version                                                   |
|-------------------------------|-----------------------------------------------------------|
| MySQL                         | 5.6.51, 5.7.34, 8.0.25                                    |
| MariaDB                       | 10.1.48, 10.2.39, 10.3.30, 10.4.20, 10.5.11               |

| PHP & Additional extensions   | Version                                                   |
|-------------------------------|-----------------------------------------------------------|
| PHP                           | 5.6.40, 7.0.33, 7.1.33, 7.2.34, 7.3.29, 7.4.21, 8.0.8     |
| ionCube Loader                | 10.4.5                                                    |
| PDFlib (PHP 7.3+)             | 9.3.1                                                     |
| XCache (PHP 5.6)              | 3.2.0                                                     |
| APCu extension                | 5.1.20                                                    |
| gRPC extension                | 1.38.0                                                    |
| ImageMagick                   | 7.1.0-2                                                   |
| imagick extension             | 3.5.0                                                     |
| GraphicsMagick                | 1.3.36                                                    |
| gmagick extension (PHP 5.6)   | 1.1.7RC3                                                  |
| gmagick extension (PHP 7.0+)  | 2.0.6RC1                                                  |
| libsodium                     | 1.0.18                                                    |
| libsodium extension           | 2.0.23                                                    |
| memcached                     | 1.6.6                                                     |
| libmemcached                  | 1.0.18                                                    |
| memcached extension (PHP 5.6) | 2.2.0                                                     |
| memcached extension (PHP 7.0+)| 3.1.5                                                     |
| redis                         | 5.0.12                                                    |
| redis extension (PHP 5.6)     | 4.3.0                                                     |
| redis extension (PHP 7.0+)    | 5.3.4                                                     |
| mongodb extension             | 1.9.1                                                     |
| swoole extension (PHP 7.2+)   | 4.6.7                                                     |
| yaf extension (PHP 7.0+)      | 3.3.2                                                     |
| yar extension (PHP 7.0+)      | 2.2.0                                                     |
| msgpack extension (PHP 7.0+)  | 2.1.2                                                     |
| psr extension (PHP 7.2+)      | 1.0.1                                                     |
| phalcon extension (PHP 7.3+)  | 4.1.2                                                     |
| xdebug extension (PHP 5.6)    | 2.5.5                                                     |
| xdebug extension (PHP 7.0+)   | 2.9.8                                                     |
| xdebug extension (PHP 8.0+)   | 3.0.4                                                     |

| Database Management Tools     | Version                                                   |
|-------------------------------|-----------------------------------------------------------|
| phpMyAdmin (PHP 5.6, PHP 7.0) | 4.9.7                                                     |
| phpMyAdmin (PHP 7.1+)         | 5.1.1                                                     |
| Adminer                       | 4.8.1                                                     |

| File Managerment Tool         | Version                                                   |
|-------------------------------|-----------------------------------------------------------|
| KodExplorer                   | 4.35                                                      |

## Installation

- If your server system: Amazon Linux/CentOS/RedHat
```bash
yum -y install wget git
git clone https://github.com/teddysun/lamp.git
cd lamp
chmod 755 *.sh
./lamp.sh
```

- If your server system: Debian/Ubuntu
```bash
apt-get -y install wget git
git clone https://github.com/teddysun/lamp.git
cd lamp
chmod 755 *.sh
./lamp.sh
```

- [Automation install mode](https://lamp.sh/autoinstall.html)
```bash
./lamp.sh -h
```

- Automation install mode example
```bash
./lamp.sh --apache_option 1 --apache_modules mod_wsgi,mod_security --db_option 2 --db_root_pwd teddysun.com --php_option 5 --php_extensions apcu,ioncube,imagick,redis,mongodb,libsodium,swoole --db_manage_modules phpmyadmin,adminer --kodexplorer_option 1
```

## Upgrade

```bash
cd ~/lamp
git reset --hard         // Resets the index and working tree
git pull                 // Get latest version first
chmod 755 *.sh

./upgrade.sh             // Select one to upgrade
./upgrade.sh apache      // Upgrade Apache
./upgrade.sh db          // Upgrade MySQL or MariaDB
./upgrade.sh php         // Upgrade PHP
./upgrade.sh phpmyadmin  // Upgrade phpMyAdmin
./upgrade.sh adminer     // Upgrade Adminer
```

## Backup

- You must modify the config before run it
- Backup MySQL or MariaDB datebases, files and directories
- Backup file is encrypted with AES256-cbc with SHA1 message-digest (Depends on `openssl` command) (option)
- Auto transfer backup file to Google Drive (Depends on [`rclone`](https://teddysun.com/469.html) command) (option)
- Auto transfer backup file to FTP server (Depends on `ftp` command) (option)
- Auto delete remote file from Google Drive or FTP server (option)

```bash
./backup.sh
```

## Uninstall

```bash
./uninstall.sh
```

## Default Installation Location

| Apache Location            | Path                                                |
|----------------------------|-----------------------------------------------------|
| Install prefix             | /usr/local/apache                                   |
| Web root location          | /data/www/default                                   |
| Main configuration File    | /usr/local/apache/conf/httpd.conf                   |
| Default virtual host conf  | /usr/local/apache/conf/vhost/default.conf           |
| Virtual host conf          | /usr/local/apache/conf/vhost/your_virtual_host.conf |
| Virtual host SSL location  | /usr/local/apache/conf/ssl/your_virtual_host        |
| Virtual host location      | /data/www/your_virtual_host_names                   |
| Virtual host log location  | /data/wwwlog/your_virtual_host_names                |

| phpMyAdmin Location        | Path                                                |
|----------------------------|-----------------------------------------------------|
| Installation location      | /data/www/default/phpmyadmin                        |

| Adminer Location           | Path                                                |
|----------------------------|-----------------------------------------------------|
| Installation location      | /data/www/default/adminer.php                       |

| KodExplorer Location       | Path                                                |
|----------------------------|-----------------------------------------------------|
| Installation location      | /data/www/default/kod                               |

| PHP Location               | Path                                                |
|----------------------------|-----------------------------------------------------|
| Install prefix             | /usr/local/php                                      |
| Configuration file         | /usr/local/php/etc/php.ini                          |
| ini additional location    | /usr/local/php/php.d                                |

| MySQL Location             | Path                                                |
|----------------------------|-----------------------------------------------------|
| Install prefix             | /usr/local/mysql                                    |
| Default data location      | /usr/local/mysql/data                               |
| my.cnf configuration File  | /etc/my.cnf                                         |

| MariaDB Location           | Path                                                |
|----------------------------|-----------------------------------------------------|
| Install prefix             | /usr/local/mariadb                                  |
| Default data location      | /usr/local/mariadb/data                             |
| my.cnf configuration file  | /etc/my.cnf                                         |

## Process Management

| Process       | Command                                                 |
|---------------|---------------------------------------------------------|
| Apache        | /etc/init.d/httpd  (start\|stop\|status\|restart)       |
| MySQL/MariaDB | /etc/init.d/mysqld (start\|stop\|status\|restart)       |
| Memcached     | /etc/init.d/memcached (start\|stop\|restart)            |
| Redis-Server  | /etc/init.d/redis-server (start\|stop\|restart)         |

## lamp Command

| Command       | Description                       |
|---------------|-----------------------------------|
| lamp add      | Create a new Apache virtual host  |
| lamp del      | Delete a Apache virtual host      |
| lamp list     | List all of Apache virtual hosts  |
| lamp version  | Print version and exit            |

## Bugs & Issues

Please feel free to report any bugs or issues to us, email to: i@teddysun.com or [open issues](https://github.com/teddysun/lamp/issues) on Github.

Support(Chinese only): https://lamp.sh/support.html

## License

Copyright (C) 2013 - 2021 [Teddysun](https://teddysun.com/)

Licensed under the [GPLv3](LICENSE) License.
