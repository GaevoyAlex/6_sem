import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Arithmetic Conveyor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ArithmeticConveyor(),
    );
  }
}

class ArithmeticConveyor extends StatefulWidget {
  @override
  _ArithmeticConveyorState createState() => _ArithmeticConveyorState();
}

class _ArithmeticConveyorState extends State<ArithmeticConveyor> {
  List<String> a = ["1010", "1111", "1100"];
  List<String> b = ["0011", "0101", "1010"];
  List<List<String>> stages = [];

  @override
  void initState() {
    super.initState();
    runConveyor();
  }

  void runConveyor() {
    for (int i = 0; i < a.length; i++) {
      List<String> stage = [];

      stage.add("Multiplying ${a[i]} by ${b[i]}");
      stage.add(a[i]);

      for (int k = 0; k < b[i].length; k++) {
        String partialResult = multiplyBinaryNumbers(a[i], b[i][k]);
        stage.add(partialResult);
      }

      stages.add(stage);
    }
  }

  String multiplyBinaryNumbers(String a, String b) {
    int len = a.length + b.length;
    List<int> result = List<int>.filled(len, 0);

    for (int i = a.length - 1; i >= 0; i--) {
      for (int j = b.length - 1; j >= 0; j--) {
        int product = (a.codeUnitAt(i) - '0'.codeUnitAt(0)) *
            (b.codeUnitAt(j) - '0'.codeUnitAt(0));
        int sum = product + result[i + j + 1];
        result[i + j + 1] = sum % 2;
        result[i + j] += sum ~/ 2;
      }
    }

    String resultStr = result.join();
    int index = resultStr.indexOf('1');
    return index != -1 ? resultStr.substring(index) : '0';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Arithmetic Conveyor'),
      ),
      body: SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: DataTable(
          columns: [
            DataColumn(label: Text('Input')),
            DataColumn(label: Text('Waiting')),
            for (int i = 0; i < b[0].length; i++)
              DataColumn(label: Text('Stage ${i + 1}')),
          ],
          rows: stages.map((stage) {
            return DataRow(
              cells: stage.map((cell) {
                return DataCell(Text(cell));
              }).toList(),
            );
          }).toList(),
        ),
      ),
    );
  }
}
