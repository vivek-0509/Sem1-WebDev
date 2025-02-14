// const flattenArray = function (arr) {
//   const flatten = [];

//   for (let i = 0; i < arr.length; i++) {
//     if (typeof arr[i] === "number") {
//       flatten.push(arr[i]);
//     } else if (Array.isArray(arr[i])) {
//       for (let j = 0; j < arr[i].length; j++) {
//         if (typeof arr[j] === "number") {
//           flatten.push(arr[j]);
//         } else if (Array.isArray(arr[j])) {
//           for (let k = 0; k < arr[j].length; k++) {
//             flatten.push(arr[k]);
//           }
//         }
//       }
//     }
//     return flatten;
//   }
// };

// const nestedArray = [1, [2, 3], [4, [5, 6]]];

// console.log(flattenArray(nestedArray));

const flattenArray = function (arr) {
  const flatten = [];

  for (let i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      flatten.push(arr[i]);
    } else if (Array.isArray(arr[i])) {
      // Check if it's an array
      flatten.push(...flattenArray(arr[i])); // Recursively flatten the inner array
    }
  }

  return flatten; // Return the flattened array
};

const nestedArray = [1, [2, 3], [4, [5, 6]]];

console.log(flattenArray(nestedArray));
