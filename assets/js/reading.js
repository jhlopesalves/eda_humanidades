const main = document.querySelector("main");
const skipLink = document.querySelector(".course-skip");

// Quarto places the include after the header. Make the skip link first in tab order.
if (skipLink && main) {
  document.body.prepend(skipLink);
  main.tabIndex = -1;
}

// Quarto's collapse control is a native disclosure button.
document.querySelector('.navbar-toggler[role="menu"]')?.removeAttribute("role");

const pageTop = document.querySelector("#quarto-back-to-top");
if (pageTop) {
  pageTop.href = "#";
  pageTop.removeAttribute("role");
}

// Quarto emits module headings as links without an href. Bootstrap still
// handles disclosure and maintains aria-expanded on both pointer controls.
for (const heading of document.querySelectorAll(
  '#quarto-sidebar .sidebar-item-text[data-bs-toggle="collapse"]:not([href])',
)) {
  const target = heading.getAttribute("data-bs-target");
  heading.tabIndex = 0;
  heading.setAttribute("role", "button");
  heading.setAttribute("aria-controls", target.slice(1));
  heading.addEventListener("keydown", (event) => {
    if (event.key === " " || event.key === "Enter") {
      event.preventDefault();
      heading.click();
    }
  });
  heading.parentElement.querySelector(".sidebar-item-toggle")?.setAttribute("aria-hidden", "true");
}

// Give keyboard users access to overflowing output in browsers that do not
// automatically add scroll containers to the tab order.
const outputSelector = [
  ".cell-output",
  ".cell-output pre",
  ".cell-code",
  ".table-responsive",
  'mjx-container[display="true"]',
].join(", ");

function updateScrollFocus(element) {
  const style = getComputedStyle(element);
  const canScroll = (overflow, length, visible) =>
    (overflow === "auto" || overflow === "scroll") && length > visible + 1;
  const overflowing =
    canScroll(style.overflowX, element.scrollWidth, element.clientWidth) ||
    canScroll(style.overflowY, element.scrollHeight, element.clientHeight);

  if (overflowing) {
    element.tabIndex = 0;
  } else {
    element.removeAttribute("tabindex");
  }
}

const scrollObserver = new ResizeObserver((entries) => {
  for (const { target } of entries) {
    updateScrollFocus(target);
  }
});

function observeOutput(selector) {
  for (const output of main.querySelectorAll(selector)) {
    if (!output.hasAttribute("tabindex")) {
      scrollObserver.observe(output);
    }
  }
}

if (main) {
  observeOutput(outputSelector);
  window.MathJax?.startup?.promise?.then(() => {
    observeOutput('mjx-container[display="true"]');
  });
}
