# Important Notice:

Octopus will enter into maintainance mode once Rails 6 is released - since Rails 6 will include all the features for Database Sharding / Replication into Rails Core (PR: https://github.com/rails/rails/pull/34052).
Once the first version of Rails 6 beta is released, there will be a migration guide to help users migrate from Octopus to Rails 6.

# Octopus - Easy Database Sharding for ActiveRecord

[![Build Status](https://travis-ci.org/thiagopradi/octopus.svg)](https://travis-ci.org/thiagopradi/octopus) [![Code Climate](https://codeclimate.com/badge.png)](https://codeclimate.com/github/thiagopradi/octopus)

Octopus is a better way to do Database Sharding in ActiveRecord. Sharding allows multiple databases in the same rails application. While there are several projects that implement Sharding (e.g. DbCharmer, DataFabric, MultiDb), each project has its own limitations. The main goal of octopus project is to provide a better way of doing Database Sharding.

## Feature list:

The api is designed to be simple as possible. Octopus focuses on the end user, giving the power of multiple databases but with reliable code and flexibility. Octopus is compatible with Rails 4 and Rails 5.

Octopus supports:

- Sharding (with multiple shards, and grouped shards).
- Replication (Master/slave support, with multiple slaves).
- Moving data between shards with migrations.
- Tools to manage database configurations. (soon)

### Replication

When using replication, all writes queries will be sent to master, and read queries to slaves. More info could be found at: <a href="https://github.com/thiagopradi/octopus/wiki/replication"> Wiki</a>

### Sharding

When using sharding, you need to specify which shard to send the query. Octopus supports selecting the shard inside a controller, or manually in each object. More could be found at <a href="https://github.com/thiagopradi/octopus/wiki/sharding"> Wiki</a>

### Replication + Sharding

When using replication and sharding concurrently, you must specify a shard, and can optionally specify a <a href="https://github.com/thiagopradi/octopus/wiki/Slave-Groups">slave group</a>.
All write queries will be sent to each shard's master. If the slave group is specified read queries will be sent to slaves in it, or else to shard's master.
More info could be found at <a href="https://github.com/thiagopradi/octopus/wiki/Slave-Groups"> Wiki</a>

## Install

Add this line to Gemfile:

```
gem 'ar-octopus'
```

Currently, Octopus doesn't support Rails 2. If you need support for rails 2, please use the version 0.5.0.

## Upgrading

### From < 0.5.0

Octopus < 0.5.0 stored schema version information in the master database defined in the database.yml file, and assumed
that each shard's schema matched the others and the master database. Beginning with Octopus 0.5.0, the schema version
information for each shard is stored within that shard's database.

If you are upgrading from < 0.5.0 run the `copy_schema_versions` rake task to copy the schema version information in the
master database to each of the shards:

```bash
rake octopus:copy_schema_versions
```

Once the task completes migrations will operate normally and schema information will be stored in each shard database
going forward.

## How to use Octopus?

First, you need to create a config file, shards.yml, inside your config/ directory. to see the syntax and how this file should look, please checkout <a href="https://github.com/thiagopradi/octopus/wiki/config-file">this page on wiki</a>.

### Syntax

Octopus adds a method to each AR Class and object: the using method is used to select the shard like this:

```ruby
User.where(:name => "Boba").limit(3).using(:read_replica_one)
```

Octopus also supports queries within a block. When you pass a block to the using method, all queries inside the block will be sent to the specified shard.

```ruby
Octopus.using(:read_replica_two) do
  User.create(:name => "Thiago")
end
```

If you want to use the same code for all shards or all shards in a specific group (for example in `db/seeds.rb`), you can use this syntax.

```ruby
# This will return a list of the given block's results, per shard.
Octopus.using_all do
  User.create_from_csv!
end

# This will return a list of the given block's results, per shard in history_shards group.
Octopus.using_group(:history_shards) do
  HistoryCategory.create_from_csv!
end
```

Each model instance knows which shard it came from so this will work automatically:

```ruby
# This will find the user in the shard1
@user = User.using(:shard1).find_by_name("Joao")

# This will find the user in the master database
@user2 = User.find_by_name("Jose")

#Sets the name
@user.name = "Mike"

# Save the user in the correct shard, shard1.
@user.save
```

### Migrations

In migrations, you also have access to the using method. The syntax is basically the same. This migration will run in the brazil and canada shards.

```ruby
class CreateUsersOnBothShards < ActiveRecord::Migration
  using(:brazil, :canada)

  def self.up
    User.create!(:name => "Both")
  end

  def self.down
    User.delete_all
  end
end
```

You also could send a migration to a group of shards. This migration will be sent to all shards that belongs to history_shards group, specified in shards.yml:

```ruby
class CreateUsersOnMultiplesGroups < ActiveRecord::Migration
  using_group(:history_shards)

  def self.up
    User.create!(:name => "MultipleGroup")
  end

  def self.down
    User.delete_all
  end
end
```

You can specify a `default_migration_group` for migrations, so that modifications to each individual migration file are not needed:

```yaml
octopus:
  default_migration_group: europe_databases
```

There is no need for a corresponding `default_migration_shard` - simply define that database to be your master. You might want this setting if all of your databases have identical schemas, but are not replicated.

You can configure a master shard for the rails application, to connect to when rails is going up. The safest would be to configure this to the shard specified in `database.yml` (some things still use it).

```yaml
octopus:
  master_shard: <%= ENV['SHARD'] || 'shard1' %>
```

Then you can use the `SHARD` environment variable to override the `master_shard` specified in `config/shards.yml`, useful for running rake tasks.

```bash
SHARD=shard1 rake db:setup && SHARD=shard2 rake db:setup
```

### Rails Controllers

If you want to send a specified action, or all actions from a controller, to a specific shard, use this syntax:

```ruby
class ApplicationController < ActionController::Base
  around_filter :select_shard

  def select_shard(&block)
    Octopus.using(:brazil, &block)
  end
end
```

To see the complete list of features and syntax, please check out our <a href="https://github.com/thiagopradi/octopus/wiki/"> Wiki</a>
Want to see sample rails applications using octopus features? please check it out: <a href="http://github.com/thiagopradi/octopus_sharding_example">Sharding Example</a> and <a href="http://github.com/thiagopradi/octopus_replication_example">Replication Example</a>. Also, we have an example that shows how to use Octopus without Rails: <a href="http://github.com/thiagopradi/octopus_sinatra"> Octopus + Sinatra Example</a>.

## Mixing Octopus with the Rails multiple database model

If you want to set a custom connection to a specific model, use the syntax `octopus_establish_connection` syntax:

```ruby
#This class sets its own connection
class CustomConnection < ActiveRecord::Base
  octopus_establish_connection(:adapter => "mysql", :database => "octopus_shard2")
end
```

### allow_shard

If you'd like to use specific shards with a model that has a Rails-managed connection, you can use `allow_shard`:

```ruby
class CustomConnectedModel
   octopus_establish_connection(...)
   allow_shard :my_shard
end

#This uses :my_shard
CustomConnectedModel.using(:my_shard).first

#This uses the Rails-managed connection pool (the call to 'using' is ignored)
CustomConnectedModel.using(:some_other_shard).first
```

This can be useful if you have a model that lives in a separate database and would like to add sharding or replication to it. For other use cases, you may be better off with <a href="https://github.com/thiagopradi/octopus/wiki/Slave-Groups">slave groups</a>.

## Contributing with Octopus

Contributors are welcome! To run the test suite, you need mysql, postgresql and sqlite3 installed. This is what you need to setup your Octopus development environment:

```bash
git clone http://github.com/thiagopradi/octopus.git
cd octopus
bundle install
bundle exec rake db:prepare
bundle exec rake appraisal:install
bundle exec rake spec
```

This command will run the spec suite for all rails versions supported.
To run our integrations tests inside sample_app, you need to following commands:

```bash
cd sample_app
bundle install
cucumber
```

If you are having issues running the octopus spec suite, verify your database users and passwords match those inside the config files and your permissions are correct.

## Contributors:

- <a href="https://github.com/thiagopradi/octopus/contributors">All Contributors</a>

## Mailing List:

- <a href="http://groups.google.com/group/octopus-activerecord/">Octopus Mailing List</a>

## Thanks

This project is sponsored by the <a href="http://www.rubysoc.org">Ruby Summer of Code</a>, Rapid River Software,
and my mentors <a href="http://github.com/mperham">Mike Perham</a> and <a href="http://github.com/amitagarwal">Amit Agarwal</a>.

## Copyright

Copyright (c) Thiago Pradi, released under the MIT license.
