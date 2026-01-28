const settings = {
  'isDay': true,
  'enabled': true
};

settings.get = arr => new Promise(resolve => {
  const ps = arr.reduce((p, c) => {
    p[c] = settings[c];
    return p;
  }, {});
  chrome.storage.local.get(ps, resolve);
});

const chromeStorageLocalGet = (key) => {
  return new Promise((resolve, reject) => {
    try {
      chrome.storage.local.get(key, (obj) => resolve(obj));
    } catch (err) {
      reject('Storage access error');
    }
  });
};

const chromeStorageLocalSet = (obj) => {
  return new Promise((resolve, reject) => {
    try {
      chrome.storage.local.set(obj, () => resolve());
    } catch (err) {
      reject('Storage access error');
    }
  });
};

chrome.runtime.onInstalled.addListener(function(runInfo) {
  if (runInfo.reason === "install") {
    chromeStorageLocalSet({
      'isDay': settings.isDay,
      'enabled': settings.enabled
    });
  }

  chrome.action.setBadgeBackgroundColor({ color: [240, 104, 104, 1] });
  chrome.action.setBadgeText({ text: "new" });
});

chrome.runtime.onMessage.addListener((message) => {
  if (message.popupOpen) {
    chrome.action.getBadgeText({}, function(result) {
      if (result === "new") {
        chrome.action.setBadgeText({ text: "" });
      }
    });
  }
});

chrome.storage.onChanged.addListener((changes) => {
  for (let pref in changes) {
    const storageChange = changes[pref];
  }
});
