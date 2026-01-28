let settings = {};
let messageTimeout;

const notify = function(msg) {
  if (!msg) {
    msg = chrome.i18n.getMessage("msg_14") || "Settings saved";
  }
  const message = document.getElementById("message");
  message.textContent = msg;
  message.classList.add("show");

  if (messageTimeout) clearTimeout(messageTimeout);
  messageTimeout = setTimeout(() => {
    message.classList.remove("show");
  }, 2000);
};

const saveSettings = function() {
  const obj = {
    'enabled': settings.enabled
  };
  chrome.storage.local.set(obj, function() {
    notify();
  });
};

const updateUI = function() {
  const enabled = document.getElementById("enabled");
  const toggleContainer = document.getElementById("toggleContainer");

  if (settings.enabled) {
    enabled.checked = true;
    toggleContainer.classList.add("active");
  } else {
    enabled.checked = false;
    toggleContainer.classList.remove("active");
  }
};

const setup = function() {
  const enabled = document.getElementById("enabled");
  const toggleContainer = document.getElementById("toggleContainer");

  updateUI();

  enabled.addEventListener("change", function(e) {
    settings.enabled = e.target.checked;
    saveSettings();

    if (e.target.checked) {
      toggleContainer.classList.add("active");
    } else {
      toggleContainer.classList.remove("active");
    }
  });

  toggleContainer.addEventListener("click", function(e) {
    if (e.target !== enabled && e.target.className !== "slider") {
      enabled.checked = !enabled.checked;
      enabled.dispatchEvent(new Event("change"));
    }
  });
};

const applyLocalization = function() {
  document.querySelectorAll("[data-i18n]").forEach(element => {
    const key = element.getAttribute("data-i18n");
    const message = chrome.i18n.getMessage(key);
    if (message) {
      if (element.tagName === "INPUT" && element.type === "checkbox") {
        element.setAttribute("aria-label", message);
      } else {
        element.textContent = message;
      }
    }
  });
};

document.addEventListener('DOMContentLoaded', function() {
  chrome.runtime.sendMessage({ popupOpen: true });

  applyLocalization();

  chrome.storage.local.get(['enabled'], function(loadedSettings) {
    if (loadedSettings && typeof loadedSettings.enabled !== "undefined") {
      settings = loadedSettings;
    } else {
      settings = {
        enabled: true
      };
      chrome.storage.local.set(settings);
    }
    setup();
  });
});
