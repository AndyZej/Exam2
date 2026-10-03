

function biggestSumOfTwoElements(array) {
  // 1. Pokud je pole prázdné (0 prvků), vrátí boolean false
  if (array.length === 0) {
    return false;
  }

  // 2. Pokud obsahuje pouze 1 prvek, vrátí jeho hodnotu
  if (array.length === 1) {
    return array[0];
  }

  // 3. Seřadíme pole od největšího po nejmenší
  const sortedArray = [...array].sort((a, b) => b - a);

  // 4. Součet dvou největších prvků (první dva prvky v seřazeném poli)
  return sortedArray[0] + sortedArray[1];
}

// Příklady použití z příkladu v zadání:
console.log(biggestSumOfTwoElements([1, 2, 3, 4]));       // => 7
console.log(biggestSumOfTwoElements([]));                // => false
console.log(biggestSumOfTwoElements([76]));              // => 76
console.log(biggestSumOfTwoElements([23, 45, 17, 12]));  // => 68