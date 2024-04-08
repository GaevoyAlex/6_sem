import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Balanced Conveyor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: BalancedConveyorPage(),
    );
  }
}

class BalancedConveyorPage extends StatelessWidget {
  final List<int> multiplicand1 = [0, 1, 1, 0, 1, 0];
  final List<int> multiplicand2 = [1, 0, 1, 1, 0, 1];
  final List<int> partialProduct = [0, 0, 0, 0, 0, 0, 0, 0, 0];

  String formatBinary(List<int> binary) {
    String formattedBinary = '';
    for (int i = 0; i < binary.length; i++) {
      formattedBinary += binary[i].toString();
      if ((i + 1) % 4 == 0 && i != binary.length - 1) {
        formattedBinary += ' ';
      }
    }
    return formattedBinary;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Balanced Conveyor'),
      ),
      body: ListView.builder(
        itemCount: 5, // Количество шагов конвейера
        itemBuilder: (context, index) {
          if (index == 0) {
            // Первый шаг: умножение со сдвигом вправо
            for (int i = 0; i < 6; i++) {
              if (multiplicand1[i] == 1) {
                for (int j = 0; j < 6; j++) {
                  partialProduct[i + j] += multiplicand2[j];
                }
              }
            }
          } else if (index == 1) {
            // Второй шаг: суммирование
            for (int i = 0; i < 8; i++) {
              // Увеличиваем до 8
              if (partialProduct[i] > 1) {
                partialProduct[i] -= 2;
                partialProduct[i + 1] += 1;
              }
            }
          }
          // Добавьте код для остальных шагов конвейера
          // ...

          return ListTile(
            title: Text('Шаг ${index + 1}'),
            subtitle: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Множимое 1: ${formatBinary(multiplicand1)}'),
                Text('Множимое 2: ${formatBinary(multiplicand2)}'),
                Text('Частичное произведение: ${formatBinary(partialProduct)}'),
              ],
            ),
          );
        },
      ),
    );
  }
}
