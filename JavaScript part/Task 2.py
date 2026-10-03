// 1 - Search for tag names:
const task1EL = document.querySelectorAll('.sample_class');

function getTag(elements) {
  const result = [];
  for (let i = 0; i < elements.length; i++) {
    result.push(elements[i].tagName);
  }
  return result;
}

getTag(task1EL);

// 2 - Search for class names:
const task2EL = document.querySelector('#sample_id');

function getClass(element) {
  const result = [];
  if (element) {
    for (let i = 0; i < element.classList.length; i++) {
      result.push(element.classList[i]);
    }
  }
  return result;
}

getClass(task2EL);

// 3 - Search for text:
const task3EL = document.querySelectorAll('.sample_class_2 li');

function getInnerText(elements) {
  const result = [];
  for (let i = 0; i < elements.length; i++) {
    result.push(elements[i].innerText);
  }
  return result;
}

getInnerText(task3EL);

// 4 - Search for link addresses:
const task4EL = document.querySelectorAll('a');

function getAddress(elements) {
  const result = [];
  for (let i = 0; i < elements.length; i++) {
    const href = elements[i].getAttribute('href');
    if (href) {
      result.push(href);
    }
  }
  return result;
}

getAddress(task4EL);

// 5 - Search for child tags:
const task5EL = document.querySelector('.sample_class_3')?.children || [];

getTag(task5EL);