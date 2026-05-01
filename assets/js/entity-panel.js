/* entity-panel.js
   Powers the entity information panel and group-of-annotations panel.
   Requires: window.ENTITY_DATA (injected by entity-panel.html via Liquid)
             #entity-panel and its child elements in the DOM
*/
(function () {
  var panel     = document.getElementById('entity-panel');
  var backBtn   = document.getElementById('ep-back-btn');
  var closeBtn  = document.getElementById('ep-close-btn');
  var titleEl   = document.getElementById('ep-title');
  var descEl    = document.getElementById('ep-description');
  var groupList = document.getElementById('ep-group-list');

  if (!panel) return;

  /* Which left-column view was active before entity panel opened */
  var _previousView  = 'gallery';
  /* Stored group keys when drilling into a single entity from a group panel */
  var _lastGroupKeys = null;

  function showPanel() {
    /* If already visible, just update content — keep _previousView unchanged */
    if (!panel.classList.contains('d-none')) return;

    var galleryView = document.getElementById('gallery-view');
    var panelView   = document.getElementById('panel-view');

    if (panelView && !panelView.classList.contains('d-none')) {
      _previousView = 'interpretive';
      panelView.classList.add('d-none');
    } else {
      _previousView = 'gallery';
      if (galleryView) galleryView.classList.add('d-none');
    }
    panel.classList.remove('d-none');
  }

  function hidePanel() {
    panel.classList.add('d-none');
    _lastGroupKeys = null;

    var galleryView = document.getElementById('gallery-view');
    var panelView   = document.getElementById('panel-view');

    if (_previousView === 'interpretive') {
      if (panelView) panelView.classList.remove('d-none');
    } else {
      if (galleryView) galleryView.classList.remove('d-none');
    }
  }

  window.openEntityPanel = function (key, type, fromGroupKeys) {
    var entity   = (window.ENTITY_DATA || {})[key] || {};
    titleEl.textContent = entity.name || key;
    descEl.innerHTML    = entity.description || '';
    descEl.classList.remove('d-none');
    groupList.classList.add('d-none');
    groupList.innerHTML = '';

    if (fromGroupKeys) {
      _lastGroupKeys = fromGroupKeys;
      backBtn.classList.remove('d-none');
    } else {
      _lastGroupKeys = null;
      backBtn.classList.add('d-none');
    }

    showPanel();
  };

  window.openGroupPanel = function (keysArray) {
    titleEl.textContent = 'Group of Annotations';
    descEl.classList.add('d-none');
    groupList.classList.remove('d-none');
    groupList.innerHTML = '';

    keysArray.forEach(function (key) {
      var entity = (window.ENTITY_DATA || {})[key] || {};
      var li     = document.createElement('li');
      var btn    = document.createElement('button');
      btn.className   = 'ep-group-btn';
      btn.textContent = entity.name || key;
      btn.addEventListener('click', function () {
        window.openEntityPanel(key, entity.type || '', keysArray);
      });
      li.appendChild(btn);
      groupList.appendChild(li);
    });

    _lastGroupKeys = keysArray;
    backBtn.classList.add('d-none');
    showPanel();
  };

  closeBtn.addEventListener('click', hidePanel);

  backBtn.addEventListener('click', function () {
    if (_lastGroupKeys) window.openGroupPanel(_lastGroupKeys);
  });
}());
