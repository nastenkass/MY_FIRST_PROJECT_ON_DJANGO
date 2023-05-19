var images = document.getElementsByClassName('myImage');
for (var i = 0; i < images.length; i++) {
  images[i].addEventListener('mouseover', function() {
    changeImage(this, 'hover_catalog_item_.svg');
  });
  images[i].addEventListener('mouseout', function() {
    changeImage(this, 'catalog_item_.svg');
  });
}

function changeImage(image) {
  if (!image.dataset.animating) { // Проверяем, не проигрывается ли уже анимация
    image.dataset.animating = true; // Устанавливаем флаг анимации

    image.style.transform = 'scale(0.8)';
    image.style.opacity = '0';

    setTimeout(function() {
      image.src = image.dataset.hoverSrc;
      image.style.transform = 'scale(1)';
      image.style.opacity = '1';

      delete image.dataset.animating; // Удаляем флаг анимации после завершения
    }, 400);
  }
}

function resetImage(image) {
  if (!image.dataset.animating) { // Проверяем, не проигрывается ли уже анимация
    image.dataset.animating = true; // Устанавливаем флаг анимации

    image.style.transform = 'scale(0.8)';
    image.style.opacity = '0';

    setTimeout(function() {
      image.src = image.dataset.initialSrc;
      image.style.transform = 'scale(1)';
      image.style.opacity = '1';

      delete image.dataset.animating; // Удаляем флаг анимации после завершения
    }, 400);
  }
}