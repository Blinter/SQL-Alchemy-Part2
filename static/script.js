document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        if (document.querySelector(".flashed_msgs") != undefined) {
           document.querySelector(".flashed_msgs").remove();
        }
    }, 3000);
});
