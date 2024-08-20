let slideIndex = 0;
const images = ["/static/img/bg-1.png", "static/img/bg-2.png", "static/img/bg-3.png"];
let autoSlideInterval;
function showSlides(index) {
  let header = document.querySelector("header");
  header.style.backgroundImage = `url('${images[index]}')`;
  header.style.backgroundSize = "cover";
}
function currentSlide(index) {
  clearInterval(autoSlideInterval);
  slideIndex = index - 1;
  showSlides(slideIndex);
  autoSlideInterval = setInterval(nextSlide, 3000);
}
function nextSlide() {
  slideIndex = (slideIndex + 1) % images.length;
  showSlides(slideIndex);
}
function initSlider(
  sliderSelector,
  slideClass,
  prevButtonSelector,
  nextButtonSelector,
  slidesToShow = 4
) {
  const slider = document.querySelector(sliderSelector);
  const slides = document.querySelectorAll(slideClass);
  const prevButton = document.getElementById(prevButtonSelector);
  const nextButton = document.getElementById(nextButtonSelector);

  let currentIndex = 0;
  const totalSlides = slides.length;

  const updateSlider = () => {
    const offset = -currentIndex * (100 / slidesToShow);
    slider.style.transform = `translateX(${offset}%)`;
  };
  const nextSlideAuto = () => {
    if (currentIndex < totalSlides - slidesToShow) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateSlider();
  };
  prevButton.addEventListener("click", () => {
    if (currentIndex > 0) {
      currentIndex--;
    } else {
      currentIndex = totalSlides - slidesToShow;
    }
    updateSlider();
    resetAutoSlide();
  });
  nextButton.addEventListener("click", () => {
    if (currentIndex < totalSlides - slidesToShow) {
      currentIndex++;
    } else {
      currentIndex = 0;
    }
    updateSlider();
    resetAutoSlide();
  });
  updateSlider();
}

document.addEventListener("DOMContentLoaded", () => {
  showSlides(slideIndex);

  initSlider(".slider", ".slide", "prev", "next");
  initSlider(".slider-2", ".slide-2", "prev-2", "next-2");
  initSlider(".slider-3", ".slide-3", "prev-3", "next-3");
  initSlider(".slider-4", ".slide-4", "prev-4", "next-4");
  initSlider(".slider-5", ".slide-5", "prev-5", "next-5");
  initSlider(".slider-6", ".slide-6", "prev-6", "next-6");
});
document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".btn-choose-coffee");
  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      buttons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
    });
  });
});
if (window.innerWidth < 780) {
  let slideIndex = 0;
  const images = ["/static/img/bg-1.png", "static/img/bg-2.png", "static/img/bg-3.png"];
  let autoSlideInterval;
  function showSlides(index) {
    let header = document.querySelector("header");
    header.style.backgroundImage = `url('${images[index]}')`;
    header.style.backgroundSize = "cover";
  }
  function currentSlide(index) {
    clearInterval(autoSlideInterval);
    slideIndex = index - 1;
    showSlides(slideIndex);
    autoSlideInterval = setInterval(nextSlide, 3000);
  }
  function nextSlide() {
    slideIndex = (slideIndex + 1) % images.length;
    showSlides(slideIndex);
  }
  function initSlider(
    sliderSelector,
    slideClass,
    prevButtonSelector,
    nextButtonSelector,
    slidesToShow = 1
  ) {
    const slider = document.querySelector(sliderSelector);
    const slides = document.querySelectorAll(slideClass);
    const prevButton = document.getElementById(prevButtonSelector);
    const nextButton = document.getElementById(nextButtonSelector);

    let currentIndex = 0;
    const totalSlides = slides.length;

    const updateSlider = () => {
      const offset = -currentIndex * (100 / slidesToShow);
      slider.style.transform = `translateX(${offset}%)`;
    };
    const nextSlideAuto = () => {
      if (currentIndex < totalSlides - slidesToShow) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      updateSlider();
    };
    prevButton.addEventListener("click", () => {
      if (currentIndex > 0) {
        currentIndex--;
      } else {
        currentIndex = totalSlides - slidesToShow;
      }
      updateSlider();
      resetAutoSlide();
    });
    nextButton.addEventListener("click", () => {
      if (currentIndex < totalSlides - slidesToShow) {
        currentIndex++;
      } else {
        currentIndex = 0;
      }
      updateSlider();
      resetAutoSlide();
    });
    updateSlider();
  }

  document.addEventListener("DOMContentLoaded", () => {
    showSlides(slideIndex);

    initSlider(".slider", ".slide", "prev", "next");
    initSlider(".slider-2", ".slide-2", "prev-2", "next-2");
    initSlider(".slider-3", ".slide-3", "prev-3", "next-3");
    initSlider(".slider-4", ".slide-4", "prev-4", "next-4");
    initSlider(".slider-5", ".slide-5", "prev-5", "next-5");
    initSlider(".slider-6", ".slide-6", "prev-6", "next-6");
  });
  document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".btn-choose-coffee");
    buttons.forEach((button) => {
      button.addEventListener("click", function () {
        buttons.forEach((btn) => btn.classList.remove("active"));
        this.classList.add("active");
      });
    });
  });
}
