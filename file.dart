// // Импортируем библиотеку для работы с очередями
// import 'dart:collection';
// import 'dart:io';

// // Функция для перевода двоичного числа в десятичное
// int binToDec(String b) {
//   return int.parse(b, radix: 2);
// }

// // Функция для перевода десятичного числа в двоичное
// String decToBin(int n) {
//   return n.toRadixString(2);
// }

// List<String> binMul(List<String> numbers) {
//   Queue<String> queue = Queue();
//   // Выравниваем длины чисел
//   int maxLen = numbers.fold(
//       0, (max, number) => number.length > max ? number.length : max);
//   numbers = numbers.map((number) => number.padLeft(maxLen, '0')).toList();
//   // Перемножаем числа по разрядам справа налево
//   for (int i = maxLen - 1; i >= 0; i--) {
//     // Если текущий бит в числе равен 1, то добавляем в очередь число, сдвинутое влево на i позиций
//     for (String number in numbers) {
//       if (number[i] == '1') {
//         queue.add(number + "0" * (maxLen - i - 1));
//       }
//     }
//   }
//   // Инициализируем результат
//   List<String> results = [];
//   // Складываем все числа в очереди
//   while (queue.isNotEmpty) {
//     // Извлекаем первое число из очереди
//     String num = queue.removeFirst();
//     // Складываем его с результатами
//     results.add(decToBin(
//         results.fold(0, (sum, result) => sum + binToDec(result)) +
//             binToDec(num)));
//   }
//   // Возвращаем результаты
//   return results;
// }

// void printResults(List<String> numbers, List<String> results) {
//   for (int i = 0; i < numbers.length; i++) {
//     print("${numbers[i]} * ${numbers[i]} = ${results[i]}");
//   }
// }

// List<String> getInputList(String prompt) {
//   while (true) {
//     String? inp = stdin.readLineSync();
//     if (inp!.split('').every((c) => c == '0' || c == '1')) {
//       return inp.split('');
//     } else {
//       print("Ошибка: введите двоичное число");
//     }
//   }
// }

// void main() {
//   while (true) {
//     print(
//         "Введите список двоичных чисел (каждое число на новой строке, пустая строка для завершения):");
//     List<String> numbers = [];
//     while (true) {
//       String input = getInputList("> ").join('');
//       if (input.isEmpty) {
//         break;
//       } else {
//         numbers.add(input);
//       }
//     }
//     List<String> results = binMul(numbers);
//     printResults(numbers, results);
//     String? cont = stdin.readLineSync();
//     if (cont?.toLowerCase() != "да") {
//       break;
//     }
//   }
// }
void main() {
  int a = 20; // 00010100 в двоичной системе
  int b = 30;
  int c = a & b;

  print(c);
  // // Процедура умножения
  // int result = 0;
  // for (int i = 0; i < 4; i++) {
  //   if ((B & 1) == 1) {
  //     print('Такт $i: Добавляем $A, сдвинутое на $i позиций влево');
  //     result += A << i;
  //   } else {
  //     print('Такт $i: Ничего не добавляем');
  //   }
  //   B >>= 1; // Сдвигаем B на 1 бит вправо
  // }

  print("Hello");
}
