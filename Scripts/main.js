const wrapper = document.getElementById("tiles");
const entry = document.querySelector("#entry");
const title = document.querySelector("#title");
const text = document.querySelector(".bottom-entry");

const main = document.querySelector(".main");

let columns = 0,
  rows = 0,
  toggled = false;

const toggle = () => {
  toggled = !toggled;

  document.body.classList.toggle("toggled");
};

const handleOnClick = (index) => {
  text.style.display = 'none';
  toggle();
  anime({
    targets: ".tile",
    opacity: 0,
    delay: anime.stagger(50, {
      grid: [columns, rows],
      from: index,
    }),
  });
  setTimeout(() => {
    title.style.animation = "fade 2s ease forwards";
    wrapper.style.display = "none";
  }, 1000);
  setTimeout(() => {
    title.style.display = "none";
    main.style.display = "block";
    main.style.animation = "fade-in 2s ease-out forwards";
  }, 2200);
};

const createTile = (index) => {
  const tile = document.createElement("div");

  tile.classList.add("tile");

  tile.style.opacity = toggled ? 0 : 1;

  tile.onclick = (e) => handleOnClick(index);

  return tile;
};
const createTiles = (quantity) => {
  Array.from(Array(quantity)).map((tile, index) => {
    wrapper.appendChild(createTile(index));
  });
};

const createGrid = () => {
  wrapper.innerHTML = "";

  const size = document.body.clientWidth > 800 ? 100 : 50;

  columns = Math.floor(document.body.clientWidth / size);
  rows = Math.floor(document.body.clientHeight / size);

  wrapper.style.setProperty("--columns", columns);
  wrapper.style.setProperty("--rows", rows);

  createTiles(columns * rows);
};

createGrid();

window.onresize = () => createGrid();

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const header = document.querySelector("header");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
  header.classList.toggle("active");

})

document.querySelectorAll(".nav-link").forEach(n => n.addEventListener("click", () => {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}))