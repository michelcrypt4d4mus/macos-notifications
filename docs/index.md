# mac-notifications
<p align="center">
  <a href="https://jorricks.github.io/mac-notifications"><img src="mac-notifications.png" alt="mac-notifications" width="600px"></a>
</p>
<p align="center">
<a href="https://www.apple.com/mac/" target="_blank">
    <img src="https://img.shields.io/badge/Platform-mac-blue" alt="Mac supported">
</a>
<a href="https://python.org" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python 3.7+ supported">
</a>
</p>

---

**Documentation**: [https://jorricks.github.io/mac-notifications/](https://jorricks.github.io/mac-notifications/)

**Source Code**: [https://github.com/Jorricks/mac-notifications](https://github.com/Jorricks/mac-notifications/)

---

**mac-notification** is a Python library to make it as easy as possible to create interactable notifications.

## Features
- Easy python interface. It's as simple as '`client.create_notification(title="Meeting starts now!", subtitle="Team Standup")`'
- Ability to reply to the notification.
- Ability to add action buttons.
- Delayed notifications.
- Automatically time out the notification listener.


## Installation
To use mac-notifications, first install it using pip:

<!-- termynal -->
```
$ pip install mac-notifications
---> 100%
Installed
```


## Requirements
Python 3.8+

Mac-notification only relies on `pyobjc`:
- The [PyObjC project](https://pyobjc.readthedocs.io/) aims to provide a bridge between the Python and Objective-C programming languages on macOS.

## Example
A simple example. Please look [in the docs](https://jorricks.github.io/mac-notifications/) for more examples.

```python

client.create_notification(
    title="Meeting starts now!",
    subtitle="Team Standup",
    icon="/Users/jorrick/zoom.png",
    action_button_str="Join zoom meeting",
    action_button_callback=partial(join_zoom_meeting, conf_number=zoom_conf_number)
)
```


## Limitations
- When you close a notification, it is possible the Python application does not get this command (This is a limitation of `pyobjc`). Therefor, to prevent it from waiting endlessly, you should define a `callback_timeout`!
- You need to keep your application running while waiting for the callback to happen.
- Currently, we are only supporting the old deprecated [user notifications](https://developer.apple.com/documentation/foundation/nsusernotification). Soon we will also make the new implementation available.