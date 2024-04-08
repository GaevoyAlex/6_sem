import 'package:flutter/material.dart';

void main() => runApp(ArithmeticConveyorApp());

class ArithmeticConveyorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Arithmetic Conveyor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: ArithmeticConveyorPage(),
    );
  }
}

class ArithmeticConveyorPage extends StatefulWidget {
  @override
  _ArithmeticConveyorPageState createState() => _ArithmeticConveyorPageState();
}

class _ArithmeticConveyorPageState extends State<ArithmeticConveyorPage> {
  List<String> a = ["1010", "1111", "1100"];
  List<String> b = ["0011", "0101", "1010"];
  List<List<String>> stages = [];
  int currentIndex = 0;

  @override
  void initState() {
    super.initState();
    runConveyor();
  }

  void runConveyor() async {
    int takts = a.length;
    for (int t = 0; t < takts; t++) {
      List<String> stage = [];

      switch (t) {
        case 0:
          //0.0
          String pair = "${a[t]} * ${b[t]}";
          stage.add(pair);
          String operation = "Multiplying ${a[t]} by ${b[t][t]}";
          String partialResult = await multiplyBinaryNumbers1(a[t], b[t][t]);
          String stageResult = "Stage ${t + 1}: $operation = $partialResult";
          stage.add(stageResult);

        case 1:
          //0.1
          String pair = "${a[t - 1]} * ${b[t - 1]}";
          stage.add(pair);
          String operation = "Multiplying ${a[t - 1]} by ${b[t - 1][t]}";
          String partialResult =
              await multiplyBinaryNumbers1(a[t - 1], b[t - 1][t]);
          String stageResult = "Stage ${t + 1}: $operation = $partialResult";
          stage.add(stageResult);

          //1.1
          String pair1 = "${a[t]} * ${b[t]}";
          stage.add(pair1);
          String operation1 = "Multiplying ${a[t]} by ${b[t][t + 1]}";
          String partialResult1 = await multiplyBinaryNumbers1(a[t], b[t][t]);
          String stageResult1 = "Stage ${t + 1}: $operation1 = $partialResult1";
          stage.add(stageResult1);

        case 2:
        case 3:
        case 4:
        case 5:
      }
      stages.add(stage);
    }
    // for (int i = 0; i < a.length; i++) {
    //   String pair = "${a[i]} * ${b[i]}";
    //   List<String> stage = [];
    //   stage.add(pair);

    //   for (int k = 0; k < b[i].length; k++) {
    //     String operation = "Multiplying ${a[i]} by ${b[i][k]}";
    //     String partialResult = await multiplyBinaryNumbers(a[i], b[i][k]);
    //     String stageResult = "Stage ${k + 1}: $operation = $partialResult";
    //     stage.add(stageResult);
    //   }

    //   stages.add(stage);
    // }
    print(stages);
    setState(() {}); // Update the UI after all stages are completed
  }

  Future<String> multiplyBinaryNumbers1(String a, String bDigit) async {
    List<int> result = List<int>.filled(a.length + 1, 0);

    int bValue = int.parse(bDigit);

    for (int i = a.length - 1; i >= 0; i--) {
      int product = (a.codeUnitAt(i) - '0'.codeUnitAt(0)) * bValue;
      int sum = product + result[i + 1];
      result[i + 1] = sum % 2;
      result[i] += sum ~/ 2;
    }

    String resultStr = result.join();
    int index = resultStr.indexOf('1');
    return index != -1 ? resultStr.substring(index) : '0';
  }

  // Future<String> multiplyBinaryNumbers(String a, String b) async {
  //   int len = a.length + b.length;
  //   List<int> result = List<int>.filled(len, 0);

  //   for (int i = a.length - 1; i >= 0; i--) {
  //     for (int j = b.length - 1; j >= 0; j--) {
  //       int product = (a.codeUnitAt(i) - '0'.codeUnitAt(0)) *
  //           (b.codeUnitAt(j) - '0'.codeUnitAt(0));
  //       int sum = product + result[i + j + 1];
  //       result[i + j + 1] = sum % 2;
  //       result[i + j] += sum ~/ 2;
  //     }
  //   }

  //   String resultStr = result.join();
  //   int index = resultStr.indexOf('1');
  //   return index != -1 ? resultStr.substring(index) : '0';
  // }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Arithmetic Conveyor'),
      ),
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          DataTable(
            columns: [
              DataColumn(label: Text('Pair')),
              DataColumn(label: Text('Stage 1')),
              DataColumn(label: Text('Stage 2')),
              // Дополнительные столбцы, если нужно
            ],
            // DataColumn(label: Text('Pair')),
            // for (int i = 0; i < b[0].length + 5; i++)
            //   DataColumn(label: Text('Stage ${i + 1}')),

            rows: stages.map((stage) {
              return DataRow(
                cells: stage.map((cell) {
                  return DataCell(Text(cell));
                }).toList(),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
