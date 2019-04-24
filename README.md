Rachiopy [![Build Status](https://travis-ci.org/rfverbruggen/rachiopy.svg?branch=master)](https://travis-ci.org/rfverbruggen/rachiopy) [![Coverage Status](https://coveralls.io/repos/github/rfverbruggen/rachiopy/badge.svg)](https://coveralls.io/github/rfverbruggen/rachiopy)
========
This python package provides a interface to the Rachio public API.

Usage
-----
```python
from rachiopy import Rachio

r = Rachio("authtoken")

r.person.getInfo()
```

Commands
--------
### Person

`r.person.getInfo()`

`r.person.get(id)`

### Device

`r.device.get(id)`

`r.device.getCurrentSchedule(id)`

`r.device.getEvent(id, starttime, endtime)`

`r.device.getScheduleItem(id)`

`r.device.getForecast(self, id, units)`

`r.device.stopWater(id)`

`r.device.rainDelay(id, duration)`

`r.device.on(id)`

`r.device.off(id)`

### Zone

`r.zone.start(id, duration)`

`r.zone.startMultiple(zones)`

`r.zone.get(id)`

### Schedulerule

`r.schedulerule.skip(id)`

`r.schedulerule.start(id)`

`r.schedulerule.seasonalAdjustment(id, adjustment)`

`r.schedulerule.get(id)`

### FlexSchedulerule

`r.flexschedulerule.get(id)`

### Notification

`r.notification.getWebhookEventType()`

`r.notification.getDeviceWebhook(id)`

`r.notification.postWebhook(webhook)`

`r.notification.putWebhook(webhook)`

`r.notification.deleteWebhook(id)`

`r.notification.get(id)`
