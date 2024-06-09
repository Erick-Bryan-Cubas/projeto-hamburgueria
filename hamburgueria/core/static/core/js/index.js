// hamburgueria/core/static/core/js/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import SimpleBottomNavigation from './components/BottomNav';

document.addEventListener('DOMContentLoaded', () => {
  ReactDOM.render(
    <SimpleBottomNavigation />,
    document.getElementById('bottom-nav-container')
  );
});
