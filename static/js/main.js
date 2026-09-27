/**
 * Global AI Adoption in Education - Frontend Interactions & Tableau Embed Helper
 */

document.addEventListener("DOMContentLoaded", function () {
  // Live Tableau URL Tester Handling
  const urlTesterForm = document.getElementById("tableau-url-tester-form");
  const urlInput = document.getElementById("custom-tableau-url-input");
  const embedFrame = document.getElementById("tableau-active-embed-frame");
  const reloadBtn = document.getElementById("reload-viz-btn");
  const fullscreenBtn = document.getElementById("fullscreen-viz-btn");
  const embedContainer = document.querySelector(".tableau-embed-container");

  if (urlTesterForm && urlInput) {
    urlTesterForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const testUrl = urlInput.value.trim();
      if (!testUrl) return;

      // Update active URL parameter in window location to render
      const currentUrl = new URL(window.location.href);
      currentUrl.searchParams.set("url", testUrl);
      window.location.href = currentUrl.toString();
    });
  }

  // Reload Tableau Frame
  if (reloadBtn && embedFrame) {
    reloadBtn.addEventListener("click", function () {
      const src = embedFrame.src;
      embedFrame.src = "";
      setTimeout(() => {
        embedFrame.src = src;
      }, 100);
    });
  }

  // Fullscreen Toggle
  if (fullscreenBtn && embedContainer) {
    fullscreenBtn.addEventListener("click", function () {
      if (!document.fullscreenElement) {
        if (embedContainer.requestFullscreen) {
          embedContainer.requestFullscreen();
        } else if (embedContainer.webkitRequestFullscreen) {
          embedContainer.webkitRequestFullscreen();
        } else if (embedContainer.msRequestFullscreen) {
          embedContainer.msRequestFullscreen();
        }
        fullscreenBtn.innerHTML = '<i class="bi bi-fullscreen-exit"></i> Exit Fullscreen';
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
        fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen"></i> Fullscreen';
      }
    });

    document.addEventListener("fullscreenchange", function () {
      if (!document.fullscreenElement) {
        fullscreenBtn.innerHTML = '<i class="bi bi-arrows-fullscreen"></i> Fullscreen';
      }
    });
  }

  // Copy Snippet Helper
  const copyButtons = document.querySelectorAll(".btn-copy-snippet");
  copyButtons.forEach((btn) => {
    btn.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        navigator.clipboard.writeText(targetEl.innerText.trim()).then(() => {
          const originalText = this.innerHTML;
          this.innerHTML = '<i class="bi bi-check2"></i> Copied!';
          setTimeout(() => {
            this.innerHTML = originalText;
          }, 2000);
        });
      }
    });
  });
});
