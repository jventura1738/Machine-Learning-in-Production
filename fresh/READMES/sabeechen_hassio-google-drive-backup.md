# Home Assistant Google Drive Backup

![screenshot](images/screenshot.png)

## About

A complete and easy way to back up your Home Assistant snapshots to Google Drive.

This is for you if you want to quickly set up a backup strategy without much fuss. It doesn't require much familiarity with Home Assistant, its architecture, or Google Drive. Detailed install instructions are provided below but you can just add this repo, click install and open the Web UI. It will tell you what to do and only takes a few simple clicks.  [Detailed install instructions are below](#detailed-install-instructions) if that doesn't seem clear.

### Features Overview

- Creates snapshots on a configurable schedule.
- Uploads snapshot to Drive, even the ones it didn't create.
- Clean up old snapshots in Home Assistant and Google Drive, so you don't run out of space.
- Lots of options for customization, but never requires you to write a yaml file.
- Restore from a fresh install or recover quickly from disaster by uploading your snapshots directly from Google Drive.
- Integrates with Home Assistant Notifications and provides sensors you can trigger off of.
- Notifies you when something goes wrong with your snapshots.
- Super easy installation and configuration.
- Privacy-centric design philosophy.
- Comprehensive documentation.
- _Most certainly_ doesn't mine bitcoin on your home automation server. Definitely no.  Or does it?

### The Upsell
This addon has been featured by %YOUR_FAVORITE_HA_YOUTUBER% and is often listed as an _essential_ addon when starting with Home Assistant.  Here are some videos about it from others if you'd like to get an idea of what using it looks like or what the community thinks:

[<img src="http://img.youtube.com/vi/GwmPPtBRdjQ/0.jpg" width="300"/>](http://www.youtube.com/watch?v=GwmPPtBRdjQ "Everything Smart Home")
[<img src="http://img.youtube.com/vi/WcErD5PvIYw/0.jpg" width="300"/>](http://www.youtube.com/watch?v=WcErD5PvIYw "DrZzs")

>This project requires financial support to make the Google Drive integration work, but it is free for you to use.  You can join those helping to keep the lights on at:
>  
>[<img src="images/bmc-button.svg" width="150"/>](https://www.buymeacoffee.com/sabeechen)
>[<img src="images/paypal-button.svg" width="150"/>](https://www.paypal.com/paypalme/stephenbeechen)
>[<img src="images/patreon-button.svg" width=150/>](https://www.patreon.com/bePatron?u=4064183)

### Detailed Install Instructions
1. Navigate in your Home Assistant frontend to <kbd>Supervisor</kbd> -> <kbd>Add-on Store</kbd>.

2. Click the 3-dots menu at upper right <kbd>...</kbd> > <kbd>Repositories</kbd> and add this repository's URL: [https://github.com/sabeechen/hassio-google-drive-backup](https://github.com/sabeechen/hassio-google-drive-backup)

   <img src="images/add_ss.png" width="300"/>

3. Scroll down the page to find the new repository, and click the new add-on named "Home Assistant Google Drive Backup"

   <img src="images/repo_ss.png" width="429"/>

4. Click <kbd>Install</kbd> and give it a few minutes to finish downloading.

5. Click <kbd>Start</kbd>, give it a few seconds to spin up, and then click the `Open Web UI` button that appears.

6. The "Getting Started" page will tell you how many snapshots you have and what it will do with them once you connect it to Google Drive. You can click `Settings` to change those options through the add-on (which is the recommended way, they take effect immediately), or update them from the page where you installed the add-on as described below (also works, restart for them to take effect).

7. Click the `Authenticate with Drive` button to link the add-on with your Google Drive account. Alternatively, you can generate your [own Google API credentials](#can-i-use-my-own-google-api-information-to-authenticate-instead-of-yours), though the process is not simple.

8. You should be redirected automatically to the backup status page. Here you can make a new snapshot, see the progress of uploading to Google Drive, etc. You're done!

## Configuration

After you start the addon you have an opportunity to review your settings within the addon's Web-UI before you connect it to Google Drive.  It is recommended to modify the setting this way because the UI makes it easy and explains what each option does.

If you'd still prefer use edit your setting in yaml or through the supervisor, the list of configurable options with explanations is available [here](./hassio-google-drive-backup/DOCS.md#configuration).

## FAQ

### How will I know this will be there when I need it?

Home Assistant is notorious for failing silently, and your backups aren't something you want to find is broken after an erroneous comma makes you unable to turn on any of the lights in your house. That's why I've added some functionality to keep you informed if things start to break. If the add-on runs into trouble and gets more than 12 hours behind its schedule, you'll know in two ways:

- Notifications in Home Assistant UI

  <img src="images/notification_error.png" width="300"/>

- A [binary_sensor](#lovelace-card) you can use to trigger additional actions.

  <img src="images/binary_sensor.png" width="600"/>

Redundancy is the foundation of reliability. With local snapshots, Google Drive's backups, and two flavors of notification I think you're covered.

### How do I restore a snapshot?
The snapshots this addon creates are the same snapshots that Home Assistant makes by itself and can be restored using any of the methods documented elsewhere.  Here are few pointers to get you started.
- If you can still get to the addon's web-UI then can select "Actions" -> "Upload" from any snapshot to have it copied back into Home Assistant.
- If not (eg, maybe your hard drive died and you're starting over):
  - Download one of the snapshots you've previously created from [Google Drive](https://drive.google.com).
  - On whatever hardware you're using to run Home Assistant now, follow the [normal instructions](https://www.home-assistant.io/getting-started/) to install Home Assistant.
  - Once it's running (but before you create a user), click the link on the Home Assistant setup page that says "Alternatively you can restore from a previous snapshot" and upload the snapshot you downloaded from Google Drive.
- If you've got a snapshot that you'd like to restore to an already set up Home Assistant instance that doesn't already have this addon installed, you'll need to use something like the [Samba Addon](https://www.home-assistant.io/hassio/haos_common_tasks/#installing-and-using-the-samba-add-on) to copy a snapshot downloaded from Google Drive into the /backup folder.  

### I never look at HA notifications. Can I show information about backups in my Home Assistant Interface?

The add-on creates a few sensors that show the status of snapshots that you could trigger automations off of. `binary_sensor.snapshots_stale` becomes true when the add-on has trouble backing up or creating snapshots. For example, the Lovelace card below only shows up in the UI when snapshots go stale:

#### Lovelace Card

```yaml
type: conditional
conditions:
  - entity: binary_sensor.snapshots_stale
    state_not: "off"
card:
  type: markdown
  content: >-
    Snapshots are stale! Please visit the "Home Assistant Google Drive Backup" add-on
    status page for details.
  title: Stale Snapshots!`
```

#### Mobile Notifications

If you have [android](https://github.com/Crewski/HANotify) or [iOS](https://www.home-assistant.io/docs/ecosystem/ios/), [other notifications](https://www.home-assistant.io/components/notify/) set up, this automation would let you know if things go stale:

```yaml
    - alias: Snapshots went stale
      id: 'snapshots_went_stale'
      trigger:
      - platform: state
        entity_id: binary_sensor.snapshots_stale
        from: 'off'
        to: 'on'
      condition: []
      action:
      - data:
        service: notify.android
          title: Snapshots are Stale
          message: Please visit the 'Home Assistant Google Drive Backup ' add-on status page
            for details.
```

You could automate anything off of this binary sensor. The add-on also exposes a sensor `sensor.snapshot_backup` that exposes the details of each snapshot. I'm working on a custom Lovelace component to expose that information.

### Can I specify what time of day snapshots should be created?

You can add `"snapshot_time_of_day": "13:00"` to your add-on configuration to make snapshots always happen at 1 pm. Specify the time in the 24-hour format of `"HH:MM"`. When unspecified, the next snapshot will be created at the same time of day as the last one.

### Can I keep older backups for longer?

> This is just an overview of how to keep older snapshots longer. [See here](https://github.com/sabeechen/hassio-google-drive-backup/blob/master/hassio-google-drive-backup/GENERATIONAL_BACKUP.md) for a more in-depth explanation.

The add-on can be configured to keep [generational backups](https://en.wikipedia.org/wiki/Backup_rotation_scheme) on daily, weekly, monthly, and yearly intervals instead of just deleting the oldest snapshot. This can be useful if, for example, you've made an erroneous change but haven't noticed for several days and all the backups before the change are gone. With a configuration setting like this...

```yaml
generational_days: 3
generational_weeks: 4
generational_months: 12
generational_years: 5
```

... a snapshot will be kept for the last 3 days, the last 4 weeks, the last 12 months, and the last 5 years. Additionally, you may configure the day of the week, day of the month, and day of the year that weekly, monthly, and yearly snapshots are maintained.

```yaml
generational_days: 3

generational_weeks: 4
generational_day_of_week: "mon" # Can be 'mon', 'tue', 'wed', 'thu', 'fri', 'sat' or 'sun' (defaults to 'mon')

generational_months: 12
generational_day_of_month: 1 # Can be 1 through 31 (defaults to 1)

generational_years: 5
generational_day_of_year: 1 # can be 1 through 365 (defaults to 1)
```

- Any combination of days, weeks, months, and years can be used. They all default to 0.
- It's highly recommended to set '`days_between_snapshots: 1`' to ensure a snapshot is available for each day.
- Ensure you've set `max_snapshots_in_drive` appropriately high to keep enough snapshots (24 in the example above).
- Once this option is enabled, it may take several days or weeks to see older snapshots get cleaned up. Old snapshots will only get deleted when the number present exceeds `max_snapshots_in_drive` or `max_snapshots_in_hassio`

### I already have something that creates snapshots on a schedule. Can I use this just to backup to Google Drive?

If you set '`days_between_snapshots: 0`', then the add-on won't try to create new snapshots but will still back up any it finds to Google Drive and clean up old snapshots in both Home Assistant and Google Drive. This can be useful if you already have for example an automation that creates snapshots on a schedule.

### Can I give snapshots a different name?

The config option `snapshot_name` can be changed to give snapshots a different name or with a date format of your choosing. The default is `{type} Snapshot {year}-{month}-{day} {hr24}:{min}:{sec}`, which makes snapshots with a name like `Full Snapshot 2019-10-31 14:00:00`. Using the settings menu in the Web UI, you can see a preview of what a snapshot name will look like but you can also set it in the add-on's options. Below is the list of variables you can add to modify the name to your liking.

- `{type}`: The type of snapshot, either 'Full' or 'Partial'
- `{year}`: Year in 4 digit format (eg 2019)
- `{year_short}`: Year in 2 digit format (eg 19)
- `{weekday}`: Long day of the week (eg Monday, ..., Sunday)
- `{weekday_short}`: Short day of week (eg Mon, ... Sun)
- `{month}`: 2 digit month (eg 01, ... 12)
- `{month_long}`: Month long name (January, ... , December)
- `{month_short}`: Month long name (Jan, ... , Dec)
- `{ms}`: Milliseconds (001, ..., 999)
- `{day}`: Day of the month (01, ..., 31)
- `{hr24}`: 2 digit hour of the day (0, ..., 24)
- `{hr12}`: 2 digit hour of the day (0, ..., 12)
- `{min}`: 2 digit minute of the hour (0, ..., 59)
- `{sec}`: 2 digit second of the minute (0, ..., 59)
- `{ampm}`: am or pm, depending on the time of day
- `{version_ha}`, Home Assistant version string (eg 0.91.3)
- `{version_hassos}`: HassOS version string (eg 0.2.15)
- `{version_super}`: , Supervisor version string (eg 1.2.19)
- `{date}`: Locale aware date (eg 2019/01/01).
- `{time}`: Locale aware time (eg 02:03:04 am)
- `{datetime}`: Locale-aware datetime string
- `{isotime}`: Date and time in ISO format
- `{hostname}`: The Home Assistant machine's hostname

### Will this ever upload to Dropbox/OnDrive/FTP/SMB/MyFavoriteProtocol?

Most likely no. I started this project to solve a specific problem I had, storing snapshots in a redundant cloud provider without having to write a bunch of buggy logic and automations. It might seem like a small change to make this work with another cloud provider, but trust me. I wrote this version of it, and it's not a simple change. I don't have the time to do it.

### But Google reads my emails!

Maybe. You can encrypt your snapshots by giving a password in the add-on's options.

### Does this store any personal information?

On a matter of principle, I only keep track of and store information necessary for the add-on to function. To the best of my knowledge the scope of this is:

- You can opt-in to sending error reports from the add-on sent to a database maintained by me. This includes the full text of the error's stack trace, the error message, and the version of the add-on you're running. This helps notice problems with new releases but leaving it off (the default unless you turn it on) doesn't affect the functionality of the add-on in any way.
- Once authenticated with Google, your Google credentials are only stored locally on your Home Assistant instance. This isn't your actual username and password, only an opaque token returned from Google used to verify that you previously gave the Add-on permission to access your Google Drive. Your password is never seen by me or the add-on. You can read more about how authentication with Google is accomplished [here](https://github.com/sabeechen/hassio-google-drive-backup/blob/master/hassio-google-drive-backup/AUTHENTICATION.md).
- The add-on has access to the files in Google Drive it created, which is the 'Home Assistant Snapshots' folder and any snapshots it uploads. See the https://www.googleapis.com/auth/drive.file scope in the [Drive REST API v3 Documentation](https://developers.google.com/drive/api/v3/about-auth) for details, this is the only scope the add-on requests for your account.
- Google stores a history of information about the number of requests, number of errors, and latency of requests made by this Add-on and makes a graph of that visible to me. This is needed because Google only gives me a certain quota for requests shared between all users of the add-on, so I need to be aware if someone is abusing it.
- The Add-on is distributed as a Docker container hosted on Docker Hub, which is how almost all add-ons work. Docker keeps track of how many people have requested an image and makes that information publicly visible.

This invariably means that I have a very limited ability to see how many people are using the add-on or if it is functioning well. If you do like it, feel free to shoot me an email at [stephen@beechens.com](mailto:stephen@beechens.com) or star this repo on GitHub, it helps keep me motivated. If you run into problems or think a new feature would be nice, file an issue on GitHub.

### Can I use my own Google API information to authenticate instead of yours?

On the first "Getting Started" page of the add-on underneath the "Authenticate with Google Drive" button is a link that lets you enter your own `Client Id` and `Client Sercet` to authenticate with Google Drive. You can get back to that page by going to "Actions" -> "Reauthorize Google Drive" from the add-on's web UI if you've already connected it previously. Instructions are also provided for those who are unfamiliar with the process, it's tedious to complete but ensures the add-on's communication is only between you and Google Drive.

### Can I permanently save a snapshot so it doesn't get cleaned up?

Select "Never Delete" from the menu next to a snapshot in the add-on's Web UI. You can choose to keep it from being deleted in Home Assistant or Google Drive. When you do this, the snapshots will no longer count against the maximum number of snapshots allowed in Google Drive or Home Assistant.
Alternatively, you can move a snapshot in Google Drive out of the snapshot folder. the add-on will ignore any files that aren't in the snapshot folder. Just don't move them back in accidentally since they'll get "cleaned up" like any old snapshot after a while :)

### What do I do if I've found an error?

If the add-on runs into trouble and can't back up, you should see a big red box with the text of the error on the status webpage. This should include a link to pre-populate a new issue in GitHub, which I'd encourage you to do. Additionally, you can set the add-on config option `"verbose": true` to get information from the add-on's logs to help me with debugging.

### Will this fill up my Google Drive? Why are my snapshots so big?

You'll need to take care to ensure you don't configure this to blow up your Google Drive. You might want to consider:

- If your snapshots are HUGE, it's probably because Home Assistant by default keeps a long sensor history. Consider setting `purge_keep_days: N` in your [recorder configuration](https://www.home-assistant.io/components/recorder/) to trim it down to something more manageable, like 1 day of history.
- Some other add-ons are designed to manage large amounts of media. For example, add-ons like the Plex Media Server are designed to store media in the /share folder, and Mobile Upload folders default to a sub-folder in the addons folder. If you migrate all of your media to the Home Assistant folder structure and you don't exclude it from the backup, you _could easily chew up your entire Google Drive space in a single snapshot_.
- If you use the Google Drive Desktop sync client, you'll probably want to tell it not to sync this folder (it's available in the options).

### I want my snapshots to sync to my Desktop computer too

That's not a question but you can use [Google Drive Backup & Sync]([https://www.google.com/drive/download/) to download anything in your Google Drive to your desktop/laptop automatically.

### I configured this to only keep 4 snapshots in Drive and Home Assistant, but sometimes I can see there are 5?

The add-on will only delete an old snapshot if a new one exists to replace it, so it will create a 5th one before deleting the first. This is a reliability/disk usage compromise that favors reliability because otherwise, it would have to delete an old snapshot (leaving only 3) before it could guarantee the 4th one exists.

### Can I exclude specific sub-folders from my snapshot?

The add-on uses the supervisor to create snapshots, and the supervisor only permits you to include or exclude the 5 main folders (home assistant configuration, share, SSL, media, and local add-ons). Excluding specific subfolders, or only including specific subfolders from a snapshot isn't possible today.
