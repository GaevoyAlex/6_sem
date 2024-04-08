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
      String pair = "${a[t]} * ${b[t]}";
      List<String> stage = [pair];
      switch (t) {
        case 0:
          //0.0
          String operation = "Multiplying ${a[t]} by ${b[t][t]}";
          String partialResult = await multiplyBinaryNumbers1(a[t], b[t][t]);
          String stageResult = "Stage ${t + 1}: $operation = $partialResult";
          stage.add(stageResult);
          break;

        case 1:
          //0.1
          String operation = "Multiplying ${a[t - 1]} by ${b[t - 1][t]}";
          String partialResult =
              await multiplyBinaryNumbers1(a[t - 1], b[t - 1][t]);
          String stageResult = "Stage ${t + 1}: $operation = $partialResult";
          stage.add(stageResult);

          //1.1
          String operation1 = "Multiplying ${a[t]} by ${b[t][t + 1]}";
          String partialResult1 = await multiplyBinaryNumbers1(a[t], b[t][t]);
          String stageResult1 = "Stage ${t + 1}: $operation1 = $partialResult1";
          stage.add(stageResult1);
          break;

        default:
          break;
      }
      stages.add(stage);
    }
    setState(() {}); 
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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Arithmetic Conveyor'),
      ),
      body: Table(
        border: TableBorder.all(),
        children: [
          TableRow(
            children: [
              TableCell(child: Text('Pair')),
              TableCell(child: Text('Stage 1')),
              TableCell(child: Text('Stage 2')),
            ],
          ),
          for (var stage in stages)
            TableRow(
              children: stage.map((cell) => TableCell(child: Text(cell))).toList(),
            ),
        ],
      ),
    );
  }
}
