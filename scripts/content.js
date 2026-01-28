let isReverseOrderEnabled = false;

(function() {
  const loadReverseCSS = function() {
    const linkElement = document.createElement('link');
    linkElement.id = "reverse-order-of-threads";
    linkElement.rel = "stylesheet";
    linkElement.type = "text/css";
    linkElement.href = chrome.runtime.getURL('styles/content-style.css');
    (document.head || document.documentElement).appendChild(linkElement);
  };

  const unloadReverseCSS = function() {
    const linkElement = document.querySelector('link#reverse-order-of-threads');
    if (linkElement) {
      linkElement.remove();
    }
  };

  const init = function() {
    if (!isReverseOrderEnabled) return;
    loadReverseCSS();
    return true;
  };

  chrome.storage.local.get(["enabled"], function(items) {
    isReverseOrderEnabled = items.enabled === true;
    init();
  });

  chrome.storage.onChanged.addListener((changes) => {
    for (let pref in changes) {
      const storageChange = changes[pref];
      if (pref === "enabled") {
        switchReverseOrder(storageChange.newValue);
      }
    }
  });

  const switchReverseOrder = function(isEnabled) {
    if (isEnabled) {
      loadReverseCSS();
    } else {
      unloadReverseCSS();
    }
  };
})();
