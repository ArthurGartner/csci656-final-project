function load() {
    const button = document.querySelector(".theme-toggle");

    // MediaQueryList object
    const useDark = window.matchMedia("(prefers-color-scheme: dark)");

    // Toggles the "dark-mode" class based on if the media query matches
    function toggleDarkMode(state) {
      // Older browser don't support the second parameter in the
      // classList.toggle method so you'd need to handle this manually
      // if you need to support older browsers.
      document.documentElement.classList.toggle("dark-mode", state);
      if (state)
      {
          document.querySelector(".light-theme-icon").classList.toggle("animate-sun");
          document.querySelector(".dark-theme-icon").classList.toggle("animate-moon");
      }
    }

    // Initial setting - CHANGE THIS TO INSTANT!
    //toggleDarkMode(useDark.matches);

    if (useDark.matches)
    {
      document.documentElement.classList.toggle("dark-mode", true);
      setTimeout(() => {
          document.querySelector(".dark-theme-icon").classList.toggle("animate-moon");
      }, 1000);
    }
    else
    {
        setTimeout(() => {
          document.querySelector(".light-theme-icon").classList.toggle("animate-sun");
        })
    }

    // Listen for changes in the OS settings
    useDark.addListener((evt) => toggleDarkMode(evt.matches));

    // Toggles the "dark-mode" class on click
    button.addEventListener("click", () => {
      document.documentElement.classList.toggle("dark-mode");
      document.querySelector(".light-theme-icon").classList.toggle("animate-sun");
      document.querySelector(".dark-theme-icon").classList.toggle("animate-moon");
    });
  }

  window.addEventListener("DOMContentLoaded", load);